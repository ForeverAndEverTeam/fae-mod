init -2 python in fae_versions:

    import store
    import store.fae_utilities as fae_utilities
    import store.fae_ev_data_ver as _verify_str

    version_updates = {}

    # key:version number -> v:changedIDs
    # changedIDs structure:
    #   k:oldId -> v:newId
    topics = {}


    def add_steps(version_struct):
        """
        Adds versions to the version updates dict.

        IN:
            version_struct - dict with versions in special version notation.
                Keys: version to update to, as string
                Vals: versions to update from, as string or tuple of strings
        """
        for to_ver, from_vers in version_struct.items(): # using items for py3
            to_ver_str = _vdot2vstr(to_ver)
            if _verify_str(from_vers, False):
                version_updates[_vdot2vstr(from_vers)] = to_ver_str
            else:
                # must be tuple
                for from_ver in from_vers:
                    version_updates[_vdot2vstr(from_ver)] = to_ver_str


    def clear():
        """
        Clears the update data structures
        """
        version_updates.clear()
        topics.clear()
    
    def init():

        add_steps({
            "0.1.0": "0.0.9",
            "0.0.9": "0.0.8",
            "0.0.8": "0.0.7",
            "0.0.7": "0.0.6",
            "0.0.6": "0.0.5",
            "0.0.5": "0.0.4",
            "0.0.4": "0.0.3",
            "0.0.3": "0.0.2",
            "0.0.2": "0.0.1"
        })

    
    def _vdot2vstr(version_str):

        return "v" + "_".join(version_str.split("."))





default persistent._fae_can_update = True
default persistent._fae_just_updated = False

#define fae_updater.normal = "https://github.com/repos/ForeverAndEverTeam/fae-mod/upd.json"
define fae_updater.normal = "https://redeyesteam.neocities.org/updates.json"

define fae_updater.force = False
define fae_updater.timeout = 10 # timeout default
define fae_updater._forced_updater_start_state = None

# transform for the sliding updater
transform fae_updater_slide:
    xpos 641 xanchor 0 ypos -35 yanchor 0
    linear 1.0 ypos 0 yanchor 0
    time 10.0
    linear 1.0 ypos -35 yanchor 0

image fae_update_available = "mod_assets/updateavailable.png"


init -1 python:
    
    class FAEUpdaterDisplayable(renpy.Displayable):

        import pygame
        import time
        import threading

        BUTTON_WIDTH = 120
        BUTTON_HEIGHT = 35
        BUTTON_BOT_SPACE = 50
        BUTTON_SPACING = 10

        FRAME_WIDTH = 500
        FRAME_HEIGHT = 250

        VIEW_WIDTH = 1280
        VIEW_HEIGHT = 720

        TEXT_YOFFSET = -15

        MOUSE_EVENTS = (
            pygame.MOUSEMOTION,
            pygame.MOUSEBUTTONUP,
            pygame.MOUSEBUTTONDOWN
        )

        TIMEOUT = 10

        # RETURN VALUES

        RET_VAL_RETRY_CANCEL = -4
        RET_VAL_MOVE_FOLDER = -3
        RET_VAL_CANCEL = -2
        RET_VAL_OK = -1
        RET_VAL_UPDATE = 1

        # STATES

        STATE_PRECHECK = -1

        STATE_CHECKING = 0

        STATE_BEHIND = 1

        STATE_UPDATED = 2

        STATE_TIMEOUT = 3

        STATE_NO_OK = 4

        STATE_BAD_JSON = 5

        def __init__(self, update_link, state_state=None):
            """
            Constructor
            """

            super(renpy.Displayable, self).__init__()

            self.update_link = update_link

            self.background = Solid(
                "#FFE6F47F",
                xsize=self.VIEW_WIDTH,
                ysize=self.VIEW_HEIGHT
            )

            # confirm screen (black, 70%)
            self.confirm = Solid(
                "#000000B2",
                xsize=self.FRAME_WIDTH,
                ysize=self.FRAME_HEIGHT
            )

            self._confirm_x = int((self.VIEW_WIDTH - self.FRAME_WIDTH) / 2)
            self._confirm_y = int((self.VIEW_HEIGHT - self.FRAME_HEIGHT) / 2)

            button_center_x = (
                int((self.FRAME_WIDTH - self.BUTTON_WIDTH) / 2) +
                self._confirm_x
            )
            button_center_y = (
                (self._confirm_y + self.FRAME_HEIGHT) -
                self.BUTTON_BOT_SPACE
            )

            button_left_x = (
                int(
                    (
                        self.FRAME_WIDTH -
                        (
                            (2 * self.BUTTON_WIDTH) +
                            self.BUTTON_SPACING
                        )
                    ) / 2
                ) +
                self._confirm_x
            )
            button_left_y = button_center_y

            self._button_ok = FAEButtonDisplayable.create_stb(
                _("OK"),
                False,
                button_center_x,
                button_center_y,
                self.BUTTON_WIDTH,
                self.BUTTON_HEIGHT,
                hover_sound=gui.hover_sound,
                activate_sound=gui.activate_sound
            )

            self._button_cancel = FAEButtonDisplayable.create_stb(
                _("Cancel"),
                False,
                button_left_x + self.BUTTON_WIDTH + self.BUTTON_SPACING,
                button_left_y,
                self.BUTTON_WIDTH,
                self.BUTTON_HEIGHT,
                hover_sound=gui.hover_sound,
                activate_sound=gui.activate_sound
            )

            self._button_update = FAEButtonDisplayable.create_stb(
                _("Update"),
                True,
                button_left_x,
                button_left_y,
                self.BUTTON_WIDTH,
                self.BUTTON_HEIGHT,
                hover_sound=gui.hover_sound,
                activate_sound=gui.activate_sound
            )

            self._button_retry = FAEButtonDisplayable.create_stb(
                _("Retry"),
                True,
                button_left_x,
                button_left_y,
                self.BUTTON_WIDTH,
                self.BUTTON_HEIGHT,
                hover_sound=gui.hover_sound,
                activate_sound=gui.activate_sound
            )

            self._text_checking = Text(
                _("Checking for updates..."),
                font=gui.default_font,
                size=gui.text_size,
                color="#ffe6f4",
                outlines=[]
            )
            self._text_update = Text(
                _("New update available!"),
                font=gui.default_font,
                size=gui.text_size,
                color="#ffe6f4",
                outlines=[]
            )
            self._text_noupdate = Text(
                _("No update found."),
                font=gui.default_font,
                size=gui.text_size,
                color="#ffe6f4",
                outlines=[]
            )
            self._text_timeout = Text(
                _("Connection timed out."),
                font=gui.default_font,
                size=gui.text_size,
                color="#ffe6f4",
                outlines=[]
            )
            self._text_badresponse = Text(
                _("Server returned bad response."),
                font=gui.default_font,
                size=gui.text_size,
                color="#ffe6f4",
                outlines=[]
            )
            self._text_badjson = Text(
                _("Server returned bad JSON."),
                font=gui.default_font,
                size=gui.text_size,
                color="#ffe6f4",
                outlines=[]
            )

            
            self._checking_buttons = [
                self._button_update,
                self._button_cancel,
            ]
            self._behind_buttons = self._checking_buttons
            self._updated_buttons = [self._button_ok]
            self._timeout_buttons = [
                self._button_retry,
                self._button_cancel,
            ]

            if not config.developer or start_state is None:
                start_state = self.STATE_PRECHECK
            self._state = start_state

            self._button_update.disable()

            self._prev_time = time.time()

            self._retry_clicked = False

            self._check_thread = None
            self._thread_result = list()

        
        def _checkUpdate(self):
            """
            Logical checking, setting states
            """

            if self._state == self.STATE_CHECKING:

                if len(self._thread_result) > 0:
                    self._state = self._thread_result.pop()

                    if self._state == self.STATE_BEHIND:

                        self._button_update.enable()
                
                elif time.time() - self._prev_time > self.TIMEOUT:

                    self._state = self.STATE_TIMEOUT
            
            elif self._state == self.STATE_PRECHECK:

                self._thread_result = list()
                self._check_thread = threading.thread(
                    target=FAEUpdaterDisplayable._sendRequest,
                    args=(self.update_link, self._thread_result)
                )
                self._check_thread.daemon = True
                self._check_thread.start()
                self._state = self.STATE_CHECKING
        
        @staticmethod
        def _handleRedirect(new_url):
            
            from http.client import HTTPConnection, HTTPException

            _http, double_slash, url = new_url.partition("//")
            url, single_slash, req_uri = url.partition("/")
            read_json = None
            h_conn = HTTPConnection(url)

            try:
                # make connection
                h_conn.connect()

                # get file we need
                h_conn.request("GET", single_slash + req_uri)
                server_response = h_conn.getresponse()

                if server_response.status != 200:
                    # we dont follow anymore redirects
                    return None

                read_json = server_response.read()

            except HTTPException:
                # we assume a timeout / connection error
                return None

            finally:
                h_conn.close()

            return read_json
        
        def cancel_value(self):
            """
            Gives a cancel value that should be returned when cancel is clicked

            RESULT: RET_VAL_*_CANCEL value
            """

            if self._retry_clicked:
                return self.RET_VAL_CANCEL
            return self.RET_VAL_CANCEL

        @staticmethod
        def _sendRequest(update_link, thread_result):
            """
            Sends out the http request and returns a response and stuff
            NOTE: designed to be called as a background thread
            ASSUMES:
                _thread_result
                    appends appropriate state for use
            """
            from http.client import HTTPConnection, HTTPException
            import json

            # separate the update link parts
            # (its okay to access this, main thread does not)
            _http, double_slash, url = update_link.partition("//")
            url, single_slash, json_file = url.partition("/")
            read_json = None
            h_conn = HTTPConnection(url)

            try:
                # make connection and attempt to connect
                h_conn.connect()

                # get the file we need
                h_conn.request("GET", "/" + json_file)
                server_response = h_conn.getresponse()

                # check status
                if server_response.status == 301:
                    # redirect, pull the location header and continue
                    new_url = server_response.getheader("location", None)

                    if new_url is None:
                        # we have to have the redirect location to continue
                        thread_result.append(FAEUpdaterDisplayable.STATE_NO_OK)
                        return

                    # otherwise, switch connection to the new url
                    h_conn.close()
                    read_json = FAEUpdaterDisplayable._handleRedirect(new_url)

                    if read_json is None:
                        # redirect failed too
                        thread_result.append(FAEUpdaterDisplayable.STATE_NO_OK)
                        return

                elif server_response.status != 200:
                    # didnt get an OK response
                    thread_result.append(FAEUpdaterDisplayable.STATE_NO_OK)
                    return

                else:
                    # good status, lets get the value
                    read_json = server_response.read()

            except HTTPException:
                # we assume a timeout / connection error
                thread_result.append(FAEUpdaterDisplayable.STATE_TIMEOUT)
                return

            finally:
                h_conn.close()

            # now to parse the json
            try:
                read_json = json.loads(read_json)

            except ValueError:
                # error decoding the json
                thread_result.append(FAEUpdaterDisplayable.STATE_BAD_JSON)
                return

            # now to get the pretty version
            try:
                _mod = read_json.get("Mod", None)

            except:
                # this wasnt a dict?!
                thread_result.append(FAEUpdaterDisplayable.STATE_BAD_JSON)
                return

            if _mod is None:
                # json is missing Mod
                thread_result.append(FAEUpdaterDisplayable.STATE_BAD_JSON)
                return

            latest_version = _mod.get("pretty_version", None)

            if latest_version is None:
                # json is missing pretty version
                thread_result.append(FAEUpdaterDisplayable.STATE_BAD_JSON)
                return

            # old version check
            
            # just replcae dots with underscores, prefix v
            parsed_version = "v" + latest_version.replace(".", "_")
            lv_is_old = parsed_version in store.updates.version_updates

            # okay we have a latest version, compare to the current version
            if latest_version == config.version or lv_is_old:
                # same version (or version on server is older)
                thread_result.append(FAEUpdaterDisplayable.STATE_UPDATED)

            else:
                # new version found!
                thread_result.append(FAEUpdaterDisplayable.STATE_BEHIND)

            return
        
        def render(self, width, height, st, at):
            """
            RENDER
            """

            # check states
            self._checkUpdate()

            # now render
            r = renpy.Render(width, height)

            # starting with backgrounds
            back = renpy.render(self.background, width, height, st, at)
            confirm = renpy.render(self.confirm, width, height, st, at)

            if (
                    self._state == self.STATE_CHECKING
                    or self._state == self.STATE_PRECHECK
                ):
                # checking for updates
                display_text = renpy.render(
                    self._text_checking,
                    width,
                    height,
                    st,
                    at
                )
                display_buttons = self._checking_buttons

            elif self._state == self.STATE_UPDATED:
                # no update avaiable
                display_text = renpy.render(
                    self._text_noupdate,
                    width,
                    height,
                    st,
                    at
                )
                display_buttons = self._updated_buttons

            elif self._state == self.STATE_BEHIND:
                # update available
                display_text = renpy.render(
                    self._text_update,
                    width,
                    height,
                    st,
                    at
                )
                display_buttons = self._behind_buttons

            else:
                # timed out
                # connection error
                # json error

                if self._state == self.STATE_TIMEOUT:
                    # timeout
                    display_text = renpy.render(
                        self._text_timeout,
                        width,
                        height,
                        st,
                        at
                    )

                elif self._state == self.STATE_NO_OK:
                    # connection error
                    display_text = renpy.render(
                        self._text_badresponse,
                        width,
                        height,
                        st,
                        at
                    )

                else:
                    # json error
                    display_text = renpy.render(
                        self._text_badjson,
                        width,
                        height,
                        st,
                        at
                    )

                display_buttons = self._timeout_buttons

            # render the buttons
            rendered_buttons = [
                (
                    x.render(width, height, st, at),
                    (x.xpos, x.ypos)
                )
                for x in display_buttons
            ]

            # get display text blit coords
            pw, ph = display_text.get_size()

            # now blit em all
            r.blit(back, (0, 0))
            r.blit(confirm, (self._confirm_x, self._confirm_y))
            r.blit(
                display_text,
                (
                    int((width - pw) / 2),
                    int((height - ph) / 2) + self.TEXT_YOFFSET
                )
            )
            for vis_b, xy in rendered_buttons:
                r.blit(vis_b, xy)

            # force a redraww so we keep checking udpater
            renpy.redraw(self, 1.0)

            return r
        
        def event(self, ev, x, y, st):
            """
            EVENT
            """
            if ev.type in self.MOUSE_EVENTS:

                if (
                        self._state == self.STATE_CHECKING
                        or self._state == self.STATE_PRECHECK
                    ):
                    # checking for an update state

                    if self._button_cancel.event(ev, x, y, st):
                        return self.cancel_value()

                elif self._state == self.STATE_UPDATED:
                    # no update found

                    if self._button_ok.event(ev, x, y, st):
                        return self.RET_VAL_OK

                elif self._state == self.STATE_BEHIND:
                    # found an update

                    if self._button_update.event(ev, x, y, st):
                        return self.RET_VAL_UPDATE

                    if self._button_cancel.event(ev, x, y, st):
                        return self.cancel_value()

                else:
                    # timeout state
                    # connection error state
                    # bad json state

                    if self._button_cancel.event(ev, x, y, st):
                        return self.RET_VAL_RETRY_CANCEL

                    if self._button_retry.event(ev, x, y, st):
                        # retry clicked! go back to checking
                        self._button_update.disable()
                        self._prev_time = time.time()
                        self._retry_clicked = True
                        self._state = self.STATE_PRECHECK

                renpy.redraw(self, 0)

            raise renpy.IgnoreEvent()

init python in fae_updater:
    import store

    def checkUpdate():

        import time
        import os
        import shutil

        curr_time = time.time()

        update_link = regular

        last_updated = renpy.game.persistent._update_last_checked.get(update_link, 0)

        if last_updated > curr_time:
            last_updated = 0
        

        game_update = os.path.normcase(renpy.config.basedir + "/game/update")
        ddlc_update = os.path.normcase(renpy.config.basedir + "/update")
        base_update = os.path.normcase(renpy.config.basedir)

        if os.access(game_update, os.F_OK):
            try:
                if os.access(ddlc_update, os.F_OK):
                    shutil.rmtree(ddlc_update)
                
                shutil.move(game_update, base_update)
                can_update = renpy.store.updater.can_update()
            
            except:
                can_update = False
        
        else:
            can_update = renpy.store.updater.can_update()
        

        renpy.game.persistent._fae_can_update = can_update

        if force:
            check_wait = 0
        else:
            check_wait = 3600 * 24
        
        if curr_time-last_updated > check_wait and can_update:
            return update_link

        return None



init 10 python:

    def _fae_backgroundUpdateCheck():

        import time
        import store.fae_updater as fae_updater

        update_link = fae_updater.checkUpdate()

        if not update_link:
            return

        thread_result = list()
        FAEUpdaterDisplayable._sendRequest(update_link, thread_result)

        if len(thread_result) > 0:
            
            state = thread_result.pop()

            if state == FAEUpdaterDisplayable.STATE_BEHIND:

                renpy.show(
                    "fae_update_available",
                    at_list=[fae_updater_slide],
                    layer="front",
                    zorder = 18,
                    tag="faeupdateroverlay"
                )

        return

    def fae_backgroundUpdateCheck():

        import threading

        the_thread = threading.Thread(
            target=_fae_backgroundUpdateCheck
        )
        the_thread.daemon = True
        the_thread.start()


init -894 python:

    def _fae_getBadFiles():

        import os

        return [
            os.path.join(root, file)
            for root, dirs, files in os.walk(os.path.join(config.gamedir,'mod_assets'))
                for file in files
                    if file.endswith(".new")
            ]
    
    def fae_cleanBadUpdateFiles():

        import shutil
        files = _fae_getBadFiles()
        for file in files:
            shutil.move(file, file[:-4])
    
    if renpy.game.persistent._fae_just_updated:

        fae_cleanBadUpdateFiles()

        renpy.game.persistent._fae_just_updated = False


label fae_updater_steam:
    s "I can't run it when you use steam."

    return

label fae_updater_rpy:

    s "There are rpy files in your game."

    s "Shall I remove them for you?"

    menu:

        "Yes please":
            call fae_rpy_file_delete()


            jump update_now
        
        "No thanks":
            s "Okay!"
    return


label forced_update_now:
    $ fae_updater.force = True

    if store.fae_globals.is_steam:

        call fae_updater_steam

        return

    elif fae_hasRPYFiles():

        call fae_updater_rpy

        return


label update_now:

    $ import time

    if store.fae_globals.is_steam:
        return

    if renpy.showing("faeupdateroverlay", layer="overlay"):
        hide faeupdateroverlay
    
    $ update_link = store.fae_updater.checkUpdate()

    if not persistent._fae_can_update:

        python:
            no_update_dialog = (
                "Error: Failed to move 'update/' folder. Please manually " +
                "move the update folder from 'game/' to the base 'ddlc/' " +
                "directory and try again."
            )

        call screen dialog(message=no_update_dialog, ok_action=Return())
        return FAEUpdaterDisplayable.RET_VAL_MOVE_FOLDER

    elif update_link:

        python:
            ui.add(FAEUpdaterDisplayable(
                update_link,
                start_state=fae_updater._forced_updater_start_state
            ))
            updater_selection = ui.interact()
        
        if updater_selection > 0:

            $ persistent._fae_just_updated = True

            stop background
            stop music

            call quit
            $ renpy.save_persistent
            window hide
            $ updater.update(update_link, restart=True)

            jump confirm_quit
        
        else:
            $ persistent._update_last_checked[update_link] = time.time()

        return updater_selection
    return