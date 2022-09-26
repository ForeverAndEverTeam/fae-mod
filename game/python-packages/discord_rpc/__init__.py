from __future__ import absolute_import, print_function
"""
Python Rich Presence library for Discord
"""
from .util.backoff import Backoff
from copy import deepcopy
import logging
from threading import Lock, Thread
from .connection.rpc import RpcConnection
from .util.utils import get_process_id, is_callable, iter_items, iter_keys, is_python3, bytes, unicode, is_linux, \
    is_windows, get_executable_path
from .util.types import Int32, Int64
import json
import time
try:
    from Queue import Queue
    from Queue import Empty as QueueEmpty
except ImportError:
    try:
        from queue import Queue
        from queue import Empty as QueueEmpty
    except ImportError:
        # we somehow can't import either python Queue's
        # create a fake Queue class that'll do nothing
        # and without killing the program
        from .util.utils import DummyQueue as Queue
        from .util.utils import Empty as QueueEmpty
from os import path, makedirs
if not is_python3():
    import requests
else:
    from urllib.request import urlopen, Request
from os import environ, system
from sys import stderr
if is_windows():
    if is_python3():
        import winreg
    else:
        import _winreg as winreg


VERSION = "1.3.0"
PROJECT_URL = "https://gitlab.com/somberdemise/discord-rpc.py"

DISCORD_REPLY_NO = 0
DISCORD_REPLY_YES = 1
DISCORD_REPLY_IGNORE = 2


_discord_rpc = None
_auto_update_connection = False
_update_thread = None
_connection_lock = Lock()
_http_rate_limit = None


class _DiscordRpc(object):
    connection = None
    _time_call = time.time
    _just_connected = False
    _just_disconnected = False
    _got_error = False
    _was_joining = False
    _was_spectating = False
    _spectate_secret = ''
    _join_secret = ''
    _last_err = [0, '']
    _last_disconnect = [0, '']
    __presence_lock = Lock()
    __handler_lock = Lock()
    __send_queue = Queue(8)
    __join_ask_queue = Queue(8)
    __connected_user = {
        'id': None,
        'username': None,
        'discriminator': None,
        'avatar': None,
    }
    __current_presence = None
    __pid = 0
    __nonce = 1
    __reconnect_time = Backoff(500, 60000)
    __next_connect = None
    __callbacks = {
        'ready': None,
        'disconnected': None,
        'joinGame': None,
        'spectateGame': None,
        'joinRequest': None,
        'error': None,
    }
    __registered_handlers = {
        'joinGame': False,
        'spectateGame': False,
        'joinRequest': False,
    }
    __http_rate_limit = None

    def __init__(self, app_id, pid=None, pipe_no=0, log=True, logger=None, log_file=None, log_level=logging.INFO,
                 callbacks=None):
        if pid is not None:
            if not isinstance(pid, int):
                raise TypeError('PID must be of int type!')
            self.__pid = pid
        else:
            self.__pid = get_process_id()
        if callbacks:
            self.set_callbacks(**callbacks)
        if self.connection is not None:
            return

        self.connection = RpcConnection(app_id, pipe_no=pipe_no, log=log, logger=logger, log_file=log_file,
                                        log_level=log_level)
        self.connection.on_connect = self._on_connect
        self.connection.on_disconnect = self._on_disconnect

    def shutdown(self):
        if self.connection is None:
            self._log('debug', 'Connection hasn\'t been established or recently shutdown; ignoring.')
            return
        self.connection.on_connect = None
        self.connection.on_disconnect = None
        self.__callbacks = {
            'ready': None,
            'disconnected': None,
            'joinGame': None,
            'spectateGame': None,
            'joinRequest': None,
            'error': None,
        }
        self.connection.destroy()

    def run_callbacks(self):
        if self.connection is None:
            return

        was_disconnected = self._just_disconnected
        self._just_disconnected = False
        is_connected = self.connection.is_open

        if is_connected:
            with self.__handler_lock:
                if was_disconnected:
                    self._run_callback('disconnected', self._last_disconnect[0], self._last_disconnect[1])

        if self._just_connected:
            with self.__handler_lock:
                self._run_callback('ready', self.current_user)
            self._just_connected = False

        if self._got_error:
            with self.__handler_lock:
                self._run_callback('error', self._last_err[0], self._last_err[1])
            self._got_error = False

        if self._was_joining:
            with self.__handler_lock:
                self._run_callback('joinGame', self._join_secret)
            self._was_joining = False

        if self._was_spectating:
            with self.__handler_lock:
                self._run_callback('spectateGame', self._spectate_secret)
            self._was_spectating = False

        users = list()
        with self.__handler_lock:
            if not self.__join_ask_queue.empty():
                # instead of trying to use a guesstimated value (qsize),
                # grab data w/o blocking, and break when it raises the "empty" error
                while True:
                    try:
                        user = self.__join_ask_queue.get(False)
                        users.append(deepcopy(user))
                        # just in case
                        self.__join_ask_queue.task_done()
                    except QueueEmpty:
                        break
            if len(users) > 0:
                self._run_callback('joinRequest', users)
                self._log('debug', "Users requesting to join: {}".format(users))
            else:
                self._log('debug', "No users requesting to join game.")

        if not is_connected and was_disconnected:
            with self.__handler_lock:
                self._run_callback('disconnected', self._last_disconnect[0], self._last_disconnect[1])

    def update_connection(self):
        if self.connection is None:
            return

        if not self.connection.is_open:
            if self.__next_connect is None:
                self.__next_connect = self.time_now()
            if self.time_now() >= self.__next_connect:
                self.update_reconnect_time()
                self._log('debug', 'Next connection in {} seconds.'.format(self.__next_connect - self.time_now()))
                self.connection.open()
        else:
            # reads
            while True:
                did_read, data = self.connection.read()
                if not did_read:
                    break
                evt = data.get('evt')
                nonce = data.get('nonce')
                if nonce is not None:
                    err_data = data.get('data', dict())
                    if evt is not None and evt == 'ERROR':
                        self._last_err = [err_data.get('code', 0), err_data.get('message', '')]
                        self._got_error = True
                else:
                    if evt is None:
                        self._log('debug', 'No event sent by Discord.')
                        continue
                    read_data = data.get('data', dict())
                    if evt == 'ACTIVITY_JOIN':
                        self._join_secret = read_data.get('secret', '')
                        self._was_joining = True
                    elif evt == 'ACTIVITY_SPECTATE':
                        self._spectate_secret = read_data.get('secret', '')
                        self._was_spectating = True
                    elif evt == 'ACTIVITY_JOIN_REQUEST':
                        user = read_data.get('user', None)
                        uid = user.get('id', None)
                        uname = user.get('username', None)
                        discrim = user.get('discriminator', None)
                        if any(x is None for x in (uid, uname, discrim)):
                            # something is wrong with Discord (or we need to update this library)
                            self._log('warning', 'Discord failed to send required data for join request!')
                            continue
                        # the avatar hash to grab from https://cdn.discordapp.com/
                        # can be None/empty string
                        avatar = user.get('avatar', None)
                        if not self.__join_ask_queue.full():
                            user_data = {'id': uid,
                                         'username': uname,
                                         'discriminator': discrim,
                                         'avatar': avatar}
                            self.__join_ask_queue.put(user_data)
            # writes
            if self.__current_presence is not None and len(self.__current_presence) > 0:
                with self.__presence_lock:
                    if self.connection.write(self.__current_presence):
                        # only erase if we successfully wrote
                        self.__current_presence = None
                        self._log('debug', 'Wrote presence data to IPC.')
            if not self.__send_queue.empty():
                # instead of trying to use a guesstimated value (qsize),
                # grab data w/o blocking, and break when it raises the "empty" error
                while True:
                    try:
                        # attempt to grab data
                        sdata = self.__send_queue.get(False)
                        # apparently, we don't care for the write results, according to Discord's library
                        self.connection.write(sdata)
                        # just in case
                        self.__send_queue.task_done()
                    except QueueEmpty:
                        self._log('debug', 'Wrote queue of send data to IPC.')
                        break

    def __presence_to_json(self, **kwargs):
        """Creates json rich presence info."""
        # See https://discordapp.com/developers/docs/rich-presence/how-to#updating-presence-update-presence-payload
        # for max values for payload
        if self.pid <= 0:
            raise AttributeError('PID is required for payload!')
        rp = dict()
        rp['cmd'] = 'SET_ACTIVITY'
        rp['args'] = dict()
        # I don't really know why PID is required, but alright
        rp['args']['pid'] = int(self.pid)

        rp['args']['activity'] = dict()

        state = kwargs.get('state', None)
        if state is not None and len(state) > 0:
            rp['args']['activity']['state'] = str(state[:128])

        details = kwargs.get('details', None)
        if details is not None and len(details) > 0:
            rp['args']['activity']['details'] = str(details[:128])

        # NOTE: Sending endTimestamp will always have the time displayed as "remaining" until the given time.
        # Sending startTimestamp will show "elapsed" as long as there is no endTimestamp sent.
        start_timestamp = kwargs.get('start_timestamp', None)
        end_timestamp = kwargs.get('end_timestamp', None)
        # we do int calculations beforehand, in case it turns out that the number ends up as 0
        if start_timestamp is not None:
            start_timestamp = Int64(int(start_timestamp)).get_number()
        if end_timestamp is not None:
            end_timestamp = Int64(int(end_timestamp)).get_number()
        if any(x for x in (start_timestamp, end_timestamp)):
            rp['args']['activity']['timestamps'] = dict()
            # start_timestamp != None && start_timestamp != 0
            if start_timestamp:
                rp['args']['activity']['timestamps']['start'] = start_timestamp
            # same for end
            if end_timestamp:
                rp['args']['activity']['timestamps']['end'] = end_timestamp

        large_image_key = kwargs.get('large_image_key', None)
        large_image_text = kwargs.get('large_image_text', None)
        small_image_key = kwargs.get('small_image_key', None)
        small_image_text = kwargs.get('small_image_text', None)
        if any(x is not None and len(x) > 0 for x in
               (large_image_key, large_image_text, small_image_key, small_image_text)):
            rp['args']['activity']['assets'] = dict()
            if large_image_key is not None and len(large_image_key) > 0:
                rp['args']['activity']['assets']['large_image'] = str(large_image_key[:128]).lower()
            if large_image_text is not None and len(large_image_text) > 0:
                rp['args']['activity']['assets']['large_text'] = str(large_image_text[:128])
            if small_image_key is not None and len(small_image_key) > 0:
                rp['args']['activity']['assets']['small_image'] = str(small_image_key[:128]).lower()
            if small_image_text is not None and len(small_image_text) > 0:
                rp['args']['activity']['assets']['small_text'] = str(small_image_text[:128])

        party_id = kwargs.get('party_id', None)
        party_size = kwargs.get('party_size', None)
        party_max = kwargs.get('party_max', None)
        # we do int calculations beforehand, in case it turns out that the number ends up as 0
        if party_size is not None:
            party_size = Int32(int(party_size)).get_number()
        if party_max is not None:
            party_max = Int32(int(party_max)).get_number()
        # for some reason, Discord does partySize || partyMax, but then requires partySize & partyMax > 0...
        # we shall correct that by throwing an all()
        if (party_id is not None and len(party_id) > 0) or all(x for x in (party_size, party_max)):
            rp['args']['activity']['party'] = dict()
            if party_id is not None and len(party_id) > 0:
                rp['args']['activity']['party']['id'] = str(party_id[:128])
            if party_size and party_max:
                rp['args']['activity']['party']['size'] = [party_size, party_max]

        # match_secret = kwargs.get('match_secret', None)    # deprecated
        join_secret = kwargs.get('join_secret', None)
        spectate_secret = kwargs.get('spectate_secret', None)
        # if any(x is not None and len(x) > 0 for x in (match_secret, join_secret, spectate_secret)):
        if any(x is not None and len(x) > 0 for x in (join_secret, spectate_secret)):
            rp['args']['activity']['secrets'] = dict()
            # if match_secret is not None and len(match_secret) > 0:
            #    rp['args']['secrets']['match'] = str(match_secret[:128])
            if join_secret is not None and len(join_secret) > 0:
                rp['args']['activity']['secrets']['join'] = str(join_secret[:128])
            if spectate_secret is not None and len(spectate_secret) > 0:
                rp['args']['activity']['secrets']['spectate'] = str(spectate_secret[:128])

        # rp['args']['instance'] = bool(kwargs.get('instance', False))   # deprecated
        rp['nonce'] = str(self.nonce)
        self.__nonce += 1

        self._log('debug', 'Presence data to be written: {}'.format(rp))
        return json.dumps(rp)

    def update_presence(self, **kwargs):
        """
        :param kwargs:      kwargs must consist of any of the following:
                            (optional) state (string)
                            (optional) details (string)
                            (optional) start_timestamp (int)
                            (optional) end_timestamp (int)
                            (optional) large_image_key (string, lowercase)
                            (optional) large_image_text (string)
                            (optional) small_image_key (string, lowercase)
                            (optional) small_image_text (string)
                            (optional) party_id (string)
                            (optional) party_size (int), party_max (int) (both are required if using either)
                            (optional) join_secret (string)
                            (optional) spectate_secret (string)
                            Note: see here https://discordapp.com/developers/docs/rich-presence/how-to#updating-presence
                            Note 2: We do not use deprecated parameters at this time
        :return:            N/A
        """
        json_data = self.__presence_to_json(**kwargs)
        with self.__presence_lock:
            self.__current_presence = json_data

    def clear_presence(self):
        self.update_presence()

    def respond(self, user_id, reply):
        if self.connection is None or not self.connection.is_open:
            self._log('warning', 'Cannot reply to discord user {}; connection not established!'.format(user_id))
            return
        response = dict()
        if reply == DISCORD_REPLY_YES:
            cmd = 'SEND_ACTIVITY_JOIN_INVITE'
        else:
            cmd = 'CLOSE_ACTIVITY_JOIN_REQUEST'
        response['cmd'] = cmd
        response['args'] = dict()
        response['args']['user_id'] = str(user_id)
        response['nonce'] = str(self.nonce)
        self.__nonce += 1
        if not self.__send_queue.full():
            self.__send_queue.put(json.dumps(response))
            self._log('debug', 'Queued reply: {}'.format(response))
        else:
            self._log('warning', 'Cannot reply to discord user {}; send queue is full!')

    def last_error(self):
        return self._last_err[0], self._last_err[1]

    def last_disconnect(self):
        return self._last_disconnect[0], self._last_disconnect[1]

    def update_reconnect_time(self):
        current_time = self.time_now()
        delay = self.__reconnect_time.next_delay() / 1000
        self.__next_connect = current_time + delay
        self._log('debug', 'Updating next connect to {}. Current time: {}, delay: {}'.format(self.__next_connect,
                                                                                             current_time,
                                                                                             delay))

    def set_callbacks(self, **kwargs):
        for name, callback_info in iter_items(kwargs):
            self.set_callback(name, callback_info)

    def set_callback(self, callback_name, callback):
        callback_name = callback_name.strip()
        if callback_name in ('ready', 'disconnected', 'joinGame', 'spectateGame', 'joinRequest', 'error'):
            if callback and not is_callable(callback):
                raise TypeError('Callback must be callable! Callback name: {}, callback: {}'.format(callback_name,
                                                                                                    callback))
            self.__callbacks[callback_name] = callback

    def update_handlers(self):
        for handler in iter_keys(self.__registered_handlers):
            if handler == 'joinGame':
                event = 'ACTIVITY_JOIN'
            elif handler == 'spectateGame':
                event = 'ACTIVITY_SPECTATE'
            elif handler == 'joinRequest':
                event = 'ACTIVITY_JOIN_REQUEST'
            else:
                # unknown handler
                self._log('warning', 'Unknown handler name "{}".'.format(handler))
                continue
            if not self.__registered_handlers[handler] and self.__callbacks[handler] is not None:
                if not self.__register_event(event):
                    self._log('warning', 'Unable to register event "{}"'.format(event))
                else:
                    self._log('info', "Registered handler {}".format(handler))
            elif self.__registered_handlers[handler] and self.__callbacks[handler] is None:
                if not self.__unregister_event(event):
                    self._log('warning', 'Unable to unregister event "{}"'.format(event))
                else:
                    self._log('debug', 'Unregistered event {}'.format(event))

    def _run_callback(self, callback_name, *args):
        callback_name = callback_name.strip()
        if callback_name in self.__callbacks:
            if self.__callbacks[callback_name] is not None:
                callback = self.__callbacks[callback_name]
                if len(args) > 0:
                    callback(*args)
                else:
                    callback()
            else:
                self._log('debug', 'No callback set for event "{}"'.format(callback_name))
        else:
            self._log('debug', 'No such event name "{}"'.format(callback_name))

    def _log(self, *args):
        if self.connection is not None:
            self.connection.log(*args)

    def _on_connect(self, data):
        self.update_handlers()
        self._log('debug', 'Data received: {}'.format(data))
        user_data = data.get('data', None)
        if user_data is not None:
            user = user_data.get('user', None)
            uid = user.get('id', None)
            uname = user.get('username', None)
            if any(x is None for x in (uid, uname)):
                self._log('warning', 'Discord failed to send current user data.')
            else:
                discrim = user.get('discriminator', None)   # i'm not sure why this can be None for current user, but
                                                            # not others...
                avatar = user.get('avatar', None)
                self.__connected_user['id'] = uid
                self.__connected_user['username'] = uname
                self.__connected_user['discriminator'] = discrim
                self.__connected_user['avatar'] = avatar
                self._log('debug', 'Current discord user: {}'.format(self.__connected_user))
        else:
            self._log('warning', 'Discord failed to send current user data.')
        self._just_connected = True
        self.__reconnect_time.reset()

    def _on_disconnect(self, err, msg):
        self._just_disconnected = True
        self._last_disconnect = [err, msg]
        self.__registered_handlers['joinGame'] = False
        self.__registered_handlers['joinRequest'] = False
        self.__registered_handlers['spectateGame'] = False
        self.update_reconnect_time()

    def __register_event(self, event):
        data = dict()
        data['nonce'] = str(self.nonce)
        self.__nonce += 1
        data['cmd'] = 'SUBSCRIBE'
        data['evt'] = event
        if not self.__send_queue.full():
            self.__send_queue.put(json.dumps(data))
            return True
        return False

    def __unregister_event(self, event):
        data = dict()
        data['nonce'] = str(self.nonce)
        self.__nonce += 1
        data['cmd'] = 'UNSUBSCRIBE'
        data['evt'] = event
        if not self.__send_queue.full():
            self.__send_queue.put(json.dumps(data))
            return True
        return False

    @property
    def got_error(self):
        return self._got_error

    @property
    def was_joining(self):
        return self._was_joining

    @property
    def was_spectating(self):
        return self._was_spectating

    @property
    def current_user(self):
        return deepcopy(self.__connected_user)

    @property
    def spectate_secret(self):
        return self._spectate_secret

    @property
    def join_secret(self):
        return self._join_secret

    @property
    def pid(self):
        return self.__pid

    @property
    def nonce(self):
        return self.__nonce

    @property
    def time_now(self):
        return self._time_call

    @time_now.setter
    def time_now(self, callback):
        if is_callable(callback):
            self._time_call = callback
        else:
            self._log('warning', 'time_now must be callable!')

    @property
    def app_id(self):
        if self.connection is not None:
            return self.connection.app_id
        else:
            return '0xDEADBEEF'


class _UpdateConnection(Thread):
    def run(self):
        global _discord_rpc
        global _connection_lock
        while True:
            time.sleep(1)
            with _connection_lock:
                if _discord_rpc is None:
                    # we have shut down, break and return
                    break
                _discord_rpc.update_connection()
                _discord_rpc.run_callbacks()


def initialize(app_id, pid=None, callbacks=None, pipe_no=0, time_call=None, auto_update_connection=False,
               log=True, logger=None, log_file=None, log_level=logging.INFO,
               auto_register=False, steam_id=None, command=None):
    """
    Initializes and connects to the Discord Rich Presence RPC
    :param app_id:          The Client ID from Discord (see https://github.com/discordapp/discord-rpc#basic-usage)
                            (NOTE: Must be a string)
    :param pid:             The main program ID (is automatically set if not passed)
    :param callbacks:       The callbacks and any extra args to run when events are fired ('ready', 'disconnected',
                                                                                           'joinGame', 'spectateGame',
                                                                                           'joinRequest', 'error')
    :param time_call:       The time function to call for epoch seconds (defaults to time.time())
    :param auto_update_connection:  Do you want the library to automagically update the connection for you?
                                    (defaults to False)
    :param log:         Do we want to use logging for the RPC connection (defaults to True)
    :param logger:      Your own logger to use (must be already set up) (defaults to automatically setting one up
                            internally)
    :param log_file:    The location of where the log file should reside (defaults to stdout only, ignored if
                            rpc_logger is used)
    :param log_level:   The log level to use (defaults to logging.INFO)
    :param pipe_no:         The pipe number to use in the RPC connection (must be 0-10, default 0)
    :param auto_register:   Do you want us to auto-register your program (defaults to False) (NOTE: currently does
                            nothing)
    :param steam_id:        The applications steam ID for auto-register (defaults to regular program registration, or
                            nothing if auto_register is False) (NOTE: Also does nothing currently)
    :param command:         The command to use for protocol registration (ex: /path/to/file --discord)
    :return:                N/A
    """
    global _discord_rpc
    global _auto_update_connection
    global _update_thread

    if _discord_rpc is not None:
        # don't initialize more than once
        return
    if auto_register:
        register_game(app_id=app_id, steam_id=steam_id, command=command)
    _discord_rpc = _DiscordRpc(app_id, pid=pid, pipe_no=pipe_no, log=log, logger=logger, log_file=log_file,
                               log_level=log_level, callbacks=callbacks)
    if time_call is not None:
        _discord_rpc.time_now = time_call

    if auto_update_connection:
        _auto_update_connection = True
        _update_thread = _UpdateConnection()
        _update_thread.start()


def shutdown():
    """
    Shuts down the Discord Rich Presence connection
    :return:    N/A
    """
    global _discord_rpc
    global _auto_update_connection
    global _connection_lock
    if _discord_rpc is not None:
        with _connection_lock:
            _discord_rpc.shutdown()
            # make sure user/programmer doesn't try to call stuff afterwards on 'discord_rpc'
            _discord_rpc = None
        if _auto_update_connection and _update_thread is not None:
            _update_thread.join()
        # always set to False
        _auto_update_connection = False


def run_callbacks():
    """
    Runs the rich presence callbacks
    :return:    N/A
    """
    global _discord_rpc
    if _discord_rpc is not None:
        _discord_rpc.run_callbacks()


def update_connection():
    """
    Updates the rich presence connection
    :return:    N/A
    """
    global _discord_rpc
    global _auto_update_connection
    if _discord_rpc is not None and not _auto_update_connection:
        _discord_rpc.update_connection()


def update_presence(**kwargs):
    """
    :param kwargs:  kwargs must consist of any of the following:
                    (optional) state (string)
                    (optional) details (string)
                    (optional) start_timestamp (int)
                    (optional) end_timestamp (int)
                    (optional) large_image_key (string, lowercase)
                    (optional) large_image_text (string)
                    (optional) small_image_key (string, lowercase)
                    (optional) small_image_text (string)
                    (optional) party_id (string)
                    (optional) party_size (int), party_max (int) (both are required if using either)
                    (optional) join_secret (string)
                    (optional) spectate_secret (string)
                    Note: see here https://discordapp.com/developers/docs/rich-presence/how-to#updating-presence
                    Note 2: We do not use deprecated parameters at this time
    :return:     N/A
    """
    global _discord_rpc
    if _discord_rpc is not None:
        _discord_rpc.update_presence(**kwargs)


def clear_presence():
    """
    Clears the rich presence data last sent
    :return:    N/A
    """
    global _discord_rpc
    if _discord_rpc is not None:
        _discord_rpc.clear_presence()


def respond(user_id, response):
    """
    Respond to a discord user
    :param user_id:     The Discord user's snowflake ID (the '64 char' long one or so)
    :param response:    The response to send to the user (one of type DISCORD_REPLY_NO, DISCORD_REPLY_YES,
                        DISCORD_REPLY_IGNORE)
    :return:    N/A
    """
    global _discord_rpc
    if _discord_rpc is not None:
        _discord_rpc.respond(user_id, response)


def download_profile_picture(user_id, discriminator, avatar_hash=None, cache_dir="cache", default_dir="default",
                             cert_file=None, game_name=None, game_version=None, game_url=None):
    """
    Download a discord user's profile picture.
    :param user_id:         The discord user's ID
    :param discriminator:   The discord user's discriminator; required and used for when avatar_hash is None
    :param avatar_hash:     (optional) The discord user's avatar hash. NOTE: if None, defaults to a default avatar image
    :param cache_dir:       (optional) Path to store the profile picture
    :param default_dir:     (optional) The path within the cache_dir to use for default avatars
    param cert_file:        (optional) The path to the cacert file to use
    :param game_name:       (optional) The name of the game that is running
    :param game_version:    (optional) The game's version number
    :param game_url:        (optional) The game's website
    :return:                Path to profile picture, or None
    """
    global _http_rate_limit
    if avatar_hash is None:
        url = "https://cdn.discordapp.com/embed/avatars/{}.png".format(int(discriminator) % 5)
        # NOTE: we default to "./cache/default/" if no path specified
        # NOTE 2: we use a "default" directory to save disk space and download calls in the long run
        download_folder = path.join(cache_dir, default_dir)
    else:
        url = "https://cdn.discordapp.com/avatars/{}/{}.jpg?size=2048".format(user_id, avatar_hash)
        # NOTE: we default to "./cache/user_id/" if no path specified
        download_folder = path.join(cache_dir, user_id)
    if not path.exists(download_folder):
        makedirs(download_folder, 0o755)
    if avatar_hash is not None:
        avatar_file = path.join(download_folder, avatar_hash) + '.jpg'
    else:
        avatar_file = path.join(download_folder, str(int(discriminator) % 5)) + '.png'
    if path.exists(avatar_file):
        # technically, we downloaded it, so no need to worry about downloading
        return avatar_file
    # we check this after just in case we already have a cached image
    if _http_rate_limit is not None:
        if not _http_rate_limit > time.time():
            return None
    # we're required to have a ua string
    ua_str = "discord-rpc.py ({url}, {version})".format(url=PROJECT_URL, version=VERSION)
    if game_name is not None and isinstance(game_name, (bytes, unicode)) and game_name.strip() != '':
        # if we have a game name, append that
        ua_str += ' {}'.format(game_name)
        if all((x is not None and isinstance(x, (bytes, unicode)) and x.strip() != '') for x in (game_version,
                                                                                                 game_url)):
            # if we have both a url and version number, append those too
            ua_str += " ({url}, {version}".format(url=game_url, version=game_version)
    headers = {'User-Agent': ua_str}
    if is_python3():
        if cert_file is not None:
            r = Request(
                url,
                data=None,
                headers=headers,
                cafile=cert_file
            )
        else:
            r = Request(
                url,
                data=None,
                headers=headers
            )
        req = urlopen(r)
        status_code = req.getcode()
    else:
        if cert_file is not None:
            req = requests.get(url, headers=headers, verify=cert_file)
        else:
            req = requests.get(url, headers=headers)
        status_code = req.status_code
    if status_code != 200:
        if status_code == 404:
            # nonexistent avatar/hash; return None
            return None
        if 'X-RateLimit-Reset' in req.headers:
            _http_rate_limit = int(req.headers['X-RateLimit-Reset'])
        else:
            try:
                if is_python3():
                    data = req.read()
                    json_data = json.loads(data.decode(req.info().get_content_charset('utf-8')))
                else:
                    json_data = req.json()
                if 'retry_after' in json_data:
                    _http_rate_limit = time.time() + (int(json_data['retry_after']) / 1000.0)
            except Exception:
                pass
        if _http_rate_limit is None:
            # try again in 15 min (Discord shouldn't kill us for waiting 15 min anyways...)
            _http_rate_limit = time.time() + (15 * 60)
        return None
    with open(avatar_file, 'wb') as f:
        if is_python3():
            f.write(req.read())
        else:
            f.write(req.content)
    return avatar_file


def register_game(app_id, steam_id=None, command=None):
    """
    Registers a protocol Discord can use to run your game.
    :param app_id:      The Client ID from Discord (see https://github.com/discordapp/discord-rpc#basic-usage)
                        (NOTE: Must be a string)
    :param steam_id:    The applications steam ID for auto-register (defaults to regular program registration)
    :param command:     The command to use for protocol registration (ex: /path/to/file --discord)
    :return:
    """
    if command is None and steam_id is None and (is_windows() or is_linux()):
        command = get_executable_path()
    if is_linux():
        # linux is the easiest
        if steam_id:
            command = "xdg-open steam://rungameid/{}".format(steam_id)
        home = environ.get('HOME')
        if home is None or home.strip() == '':
            # no home? no registration!
            return
        file_contents = "[Desktop Entry]\nName=Game {app_id}\nExec={command} %u\nType=Application\n" + \
                        "NoDisplay=true\nCategories=Discord;Games;\nMimeType=x-scheme-handler/discord-{app_id};\n"
        file_contents = file_contents.format(app_id=app_id, command=command)
        if home.endswith('/'):
            home = home[:-1]
        # we don't really need to here, but oh well
        path_location = path.join(home, ".local", "share", "applications")
        if not path.exists(path_location):
            makedirs(path_location, 0o700)
        with open(path.join(path_location, "discord-{}.desktop".format(app_id)), 'w') as f:
            f.write(file_contents)
        sys_call = "xdg-mime default discord-{0}.desktop x-scheme-handler/discord-{0}".format(app_id)
        if system(sys_call) < 0:
            print("Failed to register mime handler!", file=stderr)
    elif is_windows():
        def read_key(reg_path, name):
            try:
                root_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_READ)
                value, reg_type = winreg.QueryValueEx(root_key, name)
                winreg.CloseKey(root_key)
                return value
            except WindowsError:
                return None

        def write_key(reg_path, name, value):
            try:
                # I know this can return a key if it exists, but oh well
                winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)
                root_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
                winreg.SetValueEx(root_key, name, 0, winreg.REG_SZ, value)
                winreg.CloseKey(root_key)
                return True
            except WindowsError:
                return False

        if steam_id:
            tmp = read_key(r"Software\Valve\Steam", "SteamExe")
            if tmp is not None and tmp.strip() != '':
                command = "\"{}\" steam://rungameid/{}".format(tmp.replace("/", "\\"), steam_id)

        protocol_desc = "URL:Run game {} protocol".format(app_id)
        protocol_path = r"Software\Classes\{}".format("discord-{}".format(app_id))
        if not write_key(protocol_path, None, protocol_desc):
            # failed to write the key
            print("Error writing description!", file=stderr)
        if not write_key(protocol_path, "URL Protocol", None):
            print("Error writing description!", file=stderr)
        if not write_key(protocol_path + r"\DefaultIcon", None, get_executable_path()):
            print("Error writing key!", file=stderr)
        if not write_key(protocol_path + r"\shell\open\command", None, command):
            print("Error writing command!", file=stderr)
    else:
        # assume Mac OSX here
        def register_url(aid):
            # TODO: figure out a feasable way to get this to work
            print("Url registration under Mac OSX unimplemented. Cannot create for app ID {}".format(aid), file=stderr)

        def register_command(aid, cmd):
            home = path.expanduser("~")
            if home is None or home.strip() == '':
                return
            discord_path = path.join(home, "Library", "Application Support", "discord", "games")
            if not path.exists(discord_path):
                makedirs(discord_path)
            with open(path.join(discord_path, "{}.json".format(aid)), 'w') as f:
                f.write("{\"command\": \"{}\"}".format(cmd))

        if steam_id:
            command = "steam://rungameid/{}".format(steam_id)
        if command:
            register_command(app_id, command)
        else:
            register_url(app_id)


__all__ = ['DISCORD_REPLY_NO', 'DISCORD_REPLY_YES', 'DISCORD_REPLY_IGNORE', 'initialize', 'shutdown', 'run_callbacks',
           'update_connection', 'update_presence', 'clear_presence', 'respond', 'VERSION', 'PROJECT_URL',
           'download_profile_picture', 'register_game']
