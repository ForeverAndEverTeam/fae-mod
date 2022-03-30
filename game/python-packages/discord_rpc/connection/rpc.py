from __future__ import absolute_import
import logging
import json
from ..codes import errorcodes
from ..codes import opcodes
from ..codes import statecodes
from ..util.utils import is_callable, json2dict, range
from .ipc import BaseConnection


_RPC_VERSION = 1


class RpcConnection(object):
    _connection = None
    _state = statecodes.Disconnected
    _app_id = None
    _last_err_code = 0
    _last_err_msg = ''
    _pipe_no = 0
    _on_connect = None
    _on_disconnect = None

    def __init__(self, app_id, pipe_no=0, log=True, logger=None, log_file=None, log_level=logging.INFO):
        self._connection = BaseConnection(log=log, logger=logger, log_file=log_file, log_level=log_level)
        self._app_id = str(app_id)
        if pipe_no in range(0, 10):
            self._pipe_no = pipe_no

    def open(self):
        if self.state == statecodes.Connected:
            self.log('debug', 'Already connected; no need to open.')
            return

        if self.state == statecodes.Disconnected:
            self.connection.open(pipe_no=self._pipe_no)
            if not self.connection.is_open:
                self.log('warning', 'Failed to open IPC connection.')
                return

        if self.state == statecodes.SentHandshake:
            did_read, data = self.read()
            if did_read:
                cmd = data.get('cmd', None)
                evt = data.get('evt', None)
                if all(x is not None for x in (cmd, evt)) and cmd == 'DISPATCH' and evt == 'READY':
                    self.state = statecodes.Connected
                    if self.on_connect is not None:
                        self.on_connect(data)
                    self.log('info', 'IPC connected successfully.')
        else:
            data = {'v': _RPC_VERSION, 'client_id': self.app_id}
            if self.connection.write(json.dumps(data), opcodes.Handshake):
                self.state = statecodes.SentHandshake
                self.log('debug', 'IPC connection sent handshake.')
            else:
                self.log('warning', 'IPC failed to send handshake.')
                self.close()

    def close(self):
        if self.on_disconnect is not None and self.state in (statecodes.Connected, statecodes.SentHandshake):
            self.on_disconnect(self._last_err_code, self._last_err_msg)
            self.log('debug', 'Attempting to close IPC connection.')
        if self.connection is not None:
            self.connection.close()
        else:
            self.log('warning', 'Called close without a connection!')
        self.state = statecodes.Disconnected

    def write(self, data):
        if isinstance(data, dict):
            data = json.dumps(data)
        if not self.connection.write(data, opcodes.Frame):
            self.log('warning', 'Failed to write frame to IPC connection.')
            self.close()
            return False
        return True

    def read(self):
        if self.state not in (statecodes.Connected, statecodes.SentHandshake):
            self.log('debug', 'We aren\'t connected, therefore we cannot read data yet.')
            return False
        while True:
            did_read, opcode, data = self.connection.read()
            self.log('debug', 'ipc.read(): read: {}, Opcode: {}, data: {}'.format(did_read, opcode, data))
            if not did_read:
                err_reason = data[0]
                if (err_reason == errorcodes.PipeClosed and not self.connection.is_open) \
                        or err_reason == errorcodes.ReadCorrupt:
                    self._last_err_code = err_reason
                    self._last_err_msg = data[1]
                    self.log('debug', 'Failed to read; Connection closed. {}'.format(data))
                    self.close()
                return False, None
            if opcode == opcodes.Close:
                data = json2dict(data)
                self._last_err_code = data.get('code', -1)
                self._last_err_msg = data.get('message', '')
                self.log('debug', 'Opcode == Close. Closing connection.')
                self.close()
                return False, None
            elif opcode == opcodes.Frame:
                data = json2dict(data)
                self.log('debug', 'Successful read: {}'.format(data))
                return True, data
            elif opcode == opcodes.Ping:
                if not self.connection.write('', opcodes.Pong):
                    self.log('warning', 'Failed to send Pong message.')
                    self.close()
            elif opcode == opcodes.Pong:
                # Discord does nothing here
                pass
            else:
                # something bad happened
                self._last_err_code = errorcodes.ReadCorrupt
                self._last_err_msg = 'Bad IPC frame.'
                self.log('warning', 'Got a bad frame from IPC connection.')
                self.close()
                return False, None

    def destroy(self):
        self.log('info', 'Destroying RPC connection.')
        self.close()
        self.connection.destroy()
        self._connection = None

    def log(self, *args):
        if self._connection is not None:
            self._connection.log(*args)

    @property
    def connection(self):
        return self._connection

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        if isinstance(state, int) and state in (statecodes.Connected, statecodes.SentHandshake,
                                                statecodes.Disconnected, statecodes.AwaitingResponse):
            self._state = state
        else:
            self.log('warning', 'Invalid state number!')

    @property
    def app_id(self):
        return self._app_id

    @property
    def is_open(self):
        return self.state == statecodes.Connected

    @property
    def on_connect(self):
        return self._on_connect

    @on_connect.setter
    def on_connect(self, callback):
        if callback is None or is_callable(callback):
            self._on_connect = callback
        else:
            self.log('warning', 'on_connect must be callable/None!')

    @property
    def on_disconnect(self):
        return self._on_disconnect

    @on_disconnect.setter
    def on_disconnect(self, callback):
        if callback is None or is_callable(callback):
            self._on_disconnect = callback
        else:
            self.log('warning', 'on_disconnect must be callable/None!')
