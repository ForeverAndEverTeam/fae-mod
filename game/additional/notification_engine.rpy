default persistent._fae_notifs_enabled = False

default persistent._fae_notif_sounds = True

init python in fae_notifs:
    
    import os
    import store

    FAE_WINDOW = None

    if renpy.windows:



        try:

            import plyer

            can_show_notifs = True
        
        except ImportError:
            can_show_notifs = False

        #from plyer import notification
        if store.fae_notifs.can_show_notifs:
            
            def notifyWindows():

                title = 'Sayori'
                message = 'I have something to tell you!'
                #icon = (renpy.config.gamedir + '\\mod_assets\\' + 'Logo.png')
                #icon = 'icon.ico'

                return (
                    plyer.notification.notify(
                        title=title,
                        message=message,
                        app_icon=(renpy.config.gamedir + '/mod_assets/icon.ico'),
                        timeout=10
                    )
                )
 
                
    elif renpy.linux:

        try:
            import plyer

            can_show_notifs = True
        
        except ImportError:
            can_show_notifs = False
        
        if store.fae_notifs.can_show_notifs:

            def notifyLinux():

                title = 'Sayori'
                message = 'I have something to tell you!'

                return (
                    plyer.notification.notify(
                        title=title,
                        message=message,
                        app_icon=(renpy.config.gamedir + '/mod_assets/icon.ico'),
                        timeout=10
                    )
                )
                
            
    else:
        store.fae_notifs.can_show_notifs = False

        store.fae_utilities.fae_log.warning("Cannot detect current session type, disabling notifications.")
    
    
    
init python in fae_windows:
    
    import os
    import store

    FAE_WINDOW = None

    WIN_NOTIF_HANDLER = None

    HWND = None

    if renpy.windows:

        import sys
        sys.path.append(renpy.config.gamedir + '\\python-packages\\')

        try:
            import win32

            WIN_NOTIF_HANDLER = win32.NotifManager(
                renpy.config.name,
                os.path.join(renpy.config.gamedir, "mod_assets/fae_icon.ico"),
                on_dismiss=lambda: (
                    focusFAEWindow(),
                    _unflashFAEWindow_Windows(),
                    WIN_NOTIF_MANAGER.clear()
                ),
                on_lmb_click=lambda: (
                    focusFAEWindow(),
                    _unflashFAEWindow_Windows(),
                    WIN_NOTIF_MANAGER.clear()
                ),
                on_rmb_click=lambda: (
                    _unflashFAEWindow_Windows(),
                    WIN_NOTIF_MANAGER.clear()
                )
            )

        except Exception:

            store.fae_utilities.fae_log.warning("Couldn't import win32")

    elif renpy.linux:

        session_type = os.environ.get("XDG_SESSION_TYPE")

        #Wayland is not supported, disable wrs
        if session_type in ("wayland", None) or os.environ.get("WAYLAND_DISPLAY"):


            store.fae_notifs.can_show_notifs = False
            
            store.fae_utilities.fae_log.warning("Wayland is not yet supported, disabling notifications.")

        elif session_type == "x11" or os.environ.get("DISPLAY"):
            try:
                import Xlib

                from Xlib.display import Display
                from Xlib.error import BadWindow

                __display = Display()
                __root = __display.screen().root

            except Exception:
                store.fae_notifs.can_show_notifs = False
                

                store.fae_utilities.fae_log.warning("Xlib failed to be imported, disabling notifications.")

        else:
            store.fae_notifs.can_show_notifs = False
            

            store.fae_utilities.fae_log.warning("Cannot detect current session type, disabling notifications.")


    #Fallback Const Defintion
    DEF_MOUSE_POS_RETURN = (0, 0)


    def __getActiveWindow_Linux():

        if not store.fae_notifs.can_show_notifs:
            return None

        NET_ACTIVE_WINDOW = __display.intern_atom("_NET_ACTIVE_WINDOW")

        # Perform nullchecks on property getters, just in case.
        active_winid_prop = __root.get_full_property(NET_ACTIVE_WINDOW, 0)

        if active_winid_prop is None:
            return None

        active_winid = active_winid_prop.value[0]

        try:
            return __display.create_resource_object("window", active_winid)
        except Xlib.error.XError:
            return None

    def __getFAEWindowLinux():

        if not store.fae_notifs.can_show_notifs:
            return None

        NET_CLIENT_LIST_ATOM = __display.intern_atom('_NEW_CLIENT_LIST', False)

        try:
            winid_list = __root.get_full_property(NET_CLIENT_LIST_ATOM, 0).value

            for winid in winid_list:
                win = __display.create_resource_object("window", winid)
                transient_for = win.get_wm_transient_for()
                winname = win.get_wm_name()

                if transient_for is None and winname and store.fae_getWindowTitle() == winname:
                    return win

        except BadWindow:
            return None

    def __getFAEWindowHWND_Windows() -> int|None:
       
        global HWND

        #Verify we can actually do this before doing anything
        if store.fae_notifs.can_show_notifs:
            if HWND is None:
                try:
                    HWND = win32.get_hwnd_by_title(store.fae_getWindowTitle())
                except Exception:
                    HWND = None
        else:
            HWND = None

        return HWND

    def __getAbsoluteGeometry_Linux(win):
        
        #If win is None, then we should just return a None here
        if win is None:
            # This handles some odd issues with setting window on Linux
            win = _setFAEWindow_Linux()
            if win is None:
                return None

        try:
            geom = win.get_geometry()
            (x, y) = (geom.x, geom.y)

            while True:
                parent = win.query_tree().parent
                pgeom = parent.get_geometry()
                x += pgeom.x
                y += pgeom.y
                if parent.id == __root.id:
                    break
                win = parent

            return (x, y, geom.width, geom.height)

        except Xlib.error.BadDrawable:
            #In the case of a bad drawable, we'll try to re-get the FAE window to get a good one
            _setFAEWindow_Linux()
            return None

    def _setFAEWindow_Linux():
        """
        Sets the FAE_WINDOW global on Linux systems
        OUT:
            the window object
        """
        global FAE_WINDOW

        if renpy.linux:
            FAE_WINDOW = __getFAEWindow_Linux()

        else:
            FAE_WINDOW = None

        return FAE_WINDOW

    #Next, the active window handle getters
    def _getActiveWindowHandle_Windows() -> str:
        """
        Funtion to get the active window on Windows systems

        OUT:
            string representing the active window handle

        ASSUMES: OS IS WINDOWS (renpy.windows)
        """
        try:
            # win32 can return None
            return win32.get_active_window_title() or ""
        except Exception:
            return ""

    def _getActiveWindowHandle_Linux() -> str:
        """
        Funtion to get the active window on Linux systems

        OUT:
            string representing the active window handle

        ASSUMES: OS IS LINUX (renpy.linux)
        """
        NET_WM_NAME = __display.intern_atom("_NET_WM_NAME")
        active_winobj = __getActiveWindow_Linux()

        if active_winobj is None:
            return ""

        try:
            # Subsequent method calls might raise BadWindow exception if active_winid refers to nonexistent window.
            active_winname_prop = active_winobj.get_full_property(NET_WM_NAME, 0)

            if active_winname_prop is not None:
                active_winname = unicode(active_winname_prop.value, encoding = "utf-8")
                return active_winname.replace("\n", "")

            else:
                return ""

        except BadWindow:
            return ""

    def _getActiveWindowHandle_OSX() -> str:
        """
        Gets the active window on macOS

        NOTE: This currently just returns an empty string, this is because we do not have active window detection
        for MacOS
        """
        return ""

    def _flashFAEWindow_Windows():
        """
        Tries to flash FAE window
        """
        hwnd = __getFAEWindowHWND_Windows()
        if hwnd:
            win32.flash_window(
                hwnd,
                count=None,
                caption=False,
                tray=True
            )

    def _unflashFAEWindow_Windows():
        """
        Tries to stop flashing FAE window
        """
        hwnd = __getFAEWindowHWND_Windows()
        if hwnd:
            win32.unflash_window(hwnd)

    def _flashFAEWindow_Linux():
        """
        Tries to flash FAE window
        """

    def _flashFAEWindow_OSX():
        """
        Tries to flash FAE window
        """

    def _focusFAEWindow_Windows():
        """
        Tries to set focus on FAE window
        """
        hwnd = __getFAEWindowHWND_Windows()
        if hwnd:
            win32.set_active_window(hwnd)

    def _focusFAEWindow_Linux():
        """
        Tries to set focus on FAE window
        """

    def _focusFAEWindow_OSX():
        """
        Tries to set focus on FAE window
        """

    #Notif show internals
    def _tryShowNotification_Windows(title, body):
        """
        Tries to push a notification to the notification center on Windows.
        If it can't it should fail silently to the user.
        IN:
            title - notification title
            body - notification body
        OUT:
            bool. True if the notification was successfully sent, False otherwise
        """
        try:
            return WIN_NOTIF_MANAGER.send(title, body)
        except Exception:
            return False

    def _tryShowNotification_Linux(title, body):
        """
        Tries to push a notification to the notification center on Linux.
        If it can't it should fail silently to the user.
        IN:
            title - notification title
            body - notification body
        OUT:
            bool - True, representing the notification's success
        """
        # Single quotes have to be escaped.
        # Since single quoting in POSIX shell doesn't allow escng,
        # we have to close the quotation, insert a literal single quote and reopen the quotation.
        body  = body.replace("'", "'\\''")
        title = title.replace("'", "'\\''") # better safe than sorry
        os.system("notify-send '{0}' '{1}' -a 'Monika' -u low".format(title, body))
        return True

    def _tryShowNotification_OSX(title, body):
        """
        Tries to push a notification to the notification center on macOS.
        If it can't it should fail silently to the user.
        IN:
            title - notification title
            body - notification body
        OUT:
            bool - True, representing the notification's success
        """
        os.system('osascript -e \'display notification "{0}" with title "{1}"\''.format(body, title))
        return True

    #Mouse Position related funcs
    def _getAbsoluteMousePos_Windows():
        """
        Returns an (x, y) co-ord tuple for the mouse position
        OUT:
            tuple representing the absolute position of the mouse
        """
        if store.fae_notifs.can_show_notifs:
            #Try except here because we may not have permissions to do so
            try:
                cur_pos = tuple(win32.get_screen_mouse_pos())
            except Exception:
                cur_pos = DEF_MOUSE_POS_RETURN

        else:
            cur_pos = DEF_MOUSE_POS_RETURN

        return cur_pos

    def _getAbsoluteMousePos_Linux():
        """
        Returns an (x, y) co-ord tuple represening the absolute mouse position
        """
        mouse_data = __root.query_pointer()._data
        return (mouse_data["root_x"], mouse_data["root_y"])

    #Window position related
    def _getFAEWindowPos_Windows():
        """
        Gets the window position for FAE as a tuple of (left, top, right, bottom)
        OUT:
            tuple representing window geometry or None if the window's hWnd could not be found
        """
        hwnd = __getFAEWindowHWND_Windows()

        if hwnd is None:
            return None

        try:
            rect = win32.get_window_rect(hwnd)
        except Exception:
            return None

        # Windows may return incorrect geometry (-32k seems to be the limit),
        # in this case we return None
        if rect.top_left.x <= -32000 and rect.top_left.y <= -32000:
            return None

        return (rect.top_left.x, rect.top_left.y, rect.bottom_right.x, rect.bottom_right.y)

    def _getFAEWindowPos_Linux():
        """
        Returns (x1, y1, x2, y2) relative to the top-left of the screen.
        OUT:
            tuple representing (left, top, right, bottom) of the window bounds, or None if not possible to get
        """
        geom = __getAbsoluteGeometry_Linux(FAE_WINDOW)

        if geom is not None:
            return (
                geom[0],
                geom[1],
                geom[0] + geom[2],
                geom[1] + geom[3]
            )
        return None

    def getMousePosRelative():
        """
        Gets the mouse position relative to the FAE window.
        Returned as a set of coordinates (0, 0) being within the FAE window, (1, 0) being to the left, (0, 1) being above, etc.
        OUT:
            Tuple representing the location of the mouse relative to the FAE window in terms of coordinates
        """
        pos_tuple = getFAEWindowPos()

        if pos_tuple is None:
            return (0, 0)

        left, top, right, bottom = pos_tuple

        mouse_x, mouse_y = getMousePos()
        # NOTE: This is so we get correct pos in fullscreen
        if mouse_x == 0:
            mouse_x = 1
        if mouse_y == 0:
            mouse_y = 1

        half_fae_window_width = (right - left)/2
        half_fae_window_height = (bottom - top)/2

        # Sanity check since we'll divide by these,
        # Can be zeros in some rare cases: #9088
        if half_fae_window_width == 0 or half_fae_window_height == 0:
            return (0, 0)

        mid_fae_window_x = left + half_fae_window_width
        mid_fae_window_y = top + half_fae_window_height

        fae_window_to_cursor_x_comp = mouse_x - mid_fae_window_x
        fae_window_to_cursor_y_comp = mouse_y - mid_fae_window_y

        #Divide to handle the middle case
        fae_window_to_cursor_x_comp = int(float(fae_window_to_cursor_x_comp)/half_fae_window_width)
        fae_window_to_cursor_y_comp = -int(float(fae_window_to_cursor_y_comp)/half_fae_window_height)

        #Now return the unit vector direction
        return (
            fae_window_to_cursor_x_comp/abs(fae_window_to_cursor_x_comp) if fae_window_to_cursor_x_comp else 0,
            fae_window_to_cursor_y_comp/abs(fae_window_to_cursor_y_comp) if fae_window_to_cursor_y_comp else 0
        )

    def isCursorInFAEWindow():
        """
        Checks if the cursor is within the FAE window
        OUT:
            True if cursor is within the fae window (within x/y), False otherwise
            Also returns True if we cannot get window position
        """
        return getMousePosRelative() == (0, 0)

    def isCursorLeftOfFAEWindow():
        """
        Checks if the cursor is to the left of the FAE window (must be explicitly to the left of the left window bound)
        OUT:
            True if cursor is to the left of the window, False otherwise
            Also returns False if we cannot get window position
        """
        return getMousePosRelative()[0] == -1

    def isCursorRightOfFAEWindow():
        """
        Checks if the cursor is to the right of the FAE window (must be explicitly to the right of the right window bound)
        OUT:
            True if cursor is to the right of the window, False otherwise
            Also returns False if we cannot get window position
        """
        return getMousePosRelative()[0] == 1

    def isCursorAboveFAEWindow():
        """
        Checks if the cursor is above the FAE window (must be explicitly above the window bound)
        OUT:
            True if cursor is above the window, False otherwise
            False as well if we're unable to get a window position
        """
        return getMousePosRelative()[1] == 1

    def isCursorBelowFAEWindow():
        """
        Checks if the cursor is above the FAE window (must be explicitly above the window bound)
        OUT:
            True if cursor is above the window, False otherwise
            False as well if we're unable to get a window position
        """
        return getMousePosRelative()[1] == -1

    #Fallback functions because Mac
    def return_true():
        """
        Literally returns True
        """
        return True

    def return_false():
        """
        Literally returns False
        """
        return False

    #Finally, we set vars accordingly to use the appropriate functions without needing to run constant runtime checks
    if renpy.windows:
        _window_get = _getActiveWindowHandle_Windows
        _tryShowNotif = _tryShowNotification_Windows
        getFAEWindowPos = _getFAEWindowPos_Windows
        getMousePos = _getAbsoluteMousePos_Windows
        flashFAEWindow = _flashFAEWindow_Windows
        focusFAEWindow = _focusFAEWindow_Windows

    elif renpy.linux:
        _window_get = _getActiveWindowHandle_Linux
        _tryShowNotif = _tryShowNotification_Linux
        getFAEWindowPos = _getFAEWindowPos_Linux
        getMousePos = _getAbsoluteMousePos_Linux
        flashFAEWindow = _flashFAEWindow_Linux
        focusFAEWindow = _focusFAEWindow_Linux

    else:
        _window_get = _getActiveWindowHandle_OSX
        _tryShowNotif = _tryShowNotification_OSX
        flashFAEWindow = _flashFAEWindow_OSX
        focusFAEWindow = _focusFAEWindow_OSX

        #Because we have no method of testing on Mac, we'll use the dummy function for these
        getFAEWindowPos = store.dummy
        getMousePos = store.dummy

        #Now make sure we don't use these functions so long as we can't validate Mac
        # isCursorAboveFAEWindow = return_false
        # isCursorBelowFAEWindow = return_false
        # isCursorLeftOfFAEWindow = return_false
        # isCursorRightOfFAEWindow = return_false
        # isCursorInFAEWindow = return_true

init python:
    #List of notif quips (used for topic alerts)
    #Windows/Linux
    fae_win_notif_quips = [
        "[player], I want to talk to you about something.",
        "Are you there, [player]?",
        "Can you come here for a second?",
        "[player], do you have a second?",
        "I have something to tell you, [player]!",
        "Do you have a minute, [player]?",
        "I've got something to talk about, [player]!",
    ]

    #OSX, since no active window detection
    fae_other_notif_quips = [
        "I've got something to talk about, [player]!",
        "I have something to tell you, [player]!",
        "Hey [player], I want to tell you something.",
        "Do you have a minute, [player]?",
    ]


    #START: Utility methods
    def fae_canCheckActiveWindow():
        """
        Checks if we can check the active window (simplifies conditionals)
        """
        return (
            store.fae_notifs.can_show_notifs
            and (persistent._fae_notifs_enabled or persistent._fae_enable_notifications)
        )

    def fae_getActiveWindowHandle():
        """
        Gets the active window name
        OUT:
            The active window handle if found. If it is not possible to get, we return an empty string
        NOTE: THIS SHOULD NEVER RETURN NONE
        """
        if fae_notifs.can_show_notifs and fae_canCheckActiveWindow():
            return store.fae_notifs._window_get()
        return ""

        #TODO: Remove this alias at some point
        fae_getActiveWindow = fae_getActiveWindowHandle

    def fae_display_notif(
        title: str,
        body: list[str],
        group: str|None = None,
        skip_checks: bool = False,
        flash_window: bool = False
    ) -> bool:
        """
        Notification creation method

        IN:
            title - Notification heading text
            body - A list of items which would go in the notif body (one is picked at random)
            group - Notification group (for checking if we have this enabled)
                (Default: None)
            skip_checks - Whether or not we skips checks
                (Default: False)
            flash_window - do we want to flash the FAE window (tray icon)

        OUT:
            bool indicating status (notif shown or not (by check))

        NOTE:
            We only show notifications if:
                1. We are able to show notifs
                2. FAE isn't the active window
                3. User allows them
                4. And if the notification group is enabled
                OR if we skip checks. BUT this should only be used for introductory or testing purposes.
        """
        #First we want to create this location in the dict, but don't add an extra location if we're skipping checks
        if persistent._fae_notifs_notif_filters.get(group) is None and not skip_checks:
            persistent._fae_notifs_notif_filters[group] = False

        notif_success = False

        if (
            skip_checks
            or (
                fae_notifs.can_show_notifs
                and ((renpy.windows and not fae_isFocused()) or not renpy.windows)
                and fae_notifsEnabledForGroup(group)
            )
        ):
            #Now we make the notif
            notif_success = fae_notifs._tryShowNotif(
                renpy.substitute(title),
                renpy.substitute(renpy.random.choice(body))
            )
            if notif_success:
                # Flash the window if needed
                if flash_window:
                    fae_notifs.flashFAEWindow()

                #Play the notif sound if we have that enabled and notif was successful
                if persistent._fae_notification_sounds:
                    renpy.sound.play("mod_assets/sounds/effects/notif.wav")

        #Now we return true if notif was successful, false otherwise
        return notif_success

    def fae_isFocused():
        """
        Checks if FAE is the focused window
        """
        #TODO: Mac vers (if possible)
        return store.fae_notifs.can_show_notifs and fae_getActiveWindowHandle() == store.fae_getWindowTitle()

    def fae_isInActiveWindow(regexp, active_window_handle=None):
        """
        Checks if ALL keywords are in the active window name
        IN:
            regexp:
                Regex pattern to identify the window
            active_window_handle:
                String representing the handle of the active window
                If None, it's fetched
                (Default: None)
        """

        #Don't do work if we don't have to
        if not store.fae_notifs.can_show_notifs:
            return False

        #Otherwise, let's get the active window
        if active_window_handle is None:
            active_window_handle = fae_getActiveWindowHandle()

        return bool(re.findall(regexp, active_window_handle))

    def fae_clearNotifs():
        """
        Clears all tray icons (also action center on win10)
        """
        if renpy.windows:
            fae_notifs.WIN_NOTIF_MANAGER.clear()

    def fae_checkForWindowReacts():
        """
        Runs through events in the windowreact_db to see if we have a reaction, and if so, queue it
        """
        #Do not check anything if we're not supposed to
        if not persistent._fae_notifs_windowreacts_enabled or not store.fae_notifs.can_show_notifs:
            return

        active_window_handle = fae_getActiveWindowHandle()
        for ev_label, ev in fae_notifs.windowreact_db.items():
            if (
                Event._filterEvent(ev, unlocked=True, aff=store.fae_curr_affection)
                and ev.checkConditional()
                and fae_isInActiveWindow(ev.category[0], active_window_handle)
                and ((not store.fae_globals.in_idle_mode) or (store.fae_globals.in_idle_mode and ev.show_in_idle))
                and fae_notifsEnabledForGroup(ev.rules.get("notif-group"))
            ):
                FAEEventList.queue(ev_label)
                ev.unlocked = False

                #Add the blacklist
                if "no_unlock" in ev.rules:
                    fae_addBlacklistReact(ev_label)

    def fae_resetWindowReacts(excluded=persistent._fae_notifs_no_unlock_list):
        """
        Runs through events in the windowreact_db to unlock them
        IN:
            List of ev_labels to exclude from being unlocked
        """
        for ev_label, ev in fae_notifs.windowreact_db.items():
            if ev_label not in excluded:
                ev.unlocked=True

    def fae_updateFilterDict():
        """
        Updates the filter dict with the groups in the groups list for the settings menu
        """
        for group in store.fae_notifs._groups_list:
            if persistent._fae_notifs_notif_filters.get(group) is None:
                persistent._fae_notifs_notif_filters[group] = False

    def fae_addBlacklistReact(ev_label):
        """
        Adds the given ev_label to the no unlock list
        IN:
            ev_label: eventlabel to add to the no unlock list
        """
        if renpy.has_label(ev_label) and ev_label not in persistent._fae_notifs_no_unlock_list:
            persistent._fae_notifs_no_unlock_list.append(ev_label)

    def fae_removeBlacklistReact(ev_label):
        """
        Removes the given ev_label to the no unlock list if exists
        IN:
            ev_label: eventlabel to remove from the no unlock list
        """
        if renpy.has_label(ev_label) and ev_label in persistent._fae_notifs_no_unlock_list:
            persistent._fae_notifs_no_unlock_list.remove(ev_label)

    def fae_notifsEnabledForGroup(group):
        """
        Checks if notifications are enabled, and if enabled for the specified group
        IN:
            group: notification group to check
        """
        return persistent._fae_enable_notifications and persistent._fae_notifs_notif_filters.get(group,False)

    def fae_unlockFailedWRS(ev_label=None):
        """
        Unlocks a wrs again provided that it showed, but failed to show (failed checks in the notif label)
        NOTE: This should only be used for wrs that are only a notification
        IN:
            ev_label: eventlabel of the wrs
        """
        if (
            ev_label
            and renpy.has_label(ev_label)
            and ev_label not in persistent._fae_notifs_no_unlock_list
        ):
            fae_unlockEVL(ev_label,"WRS")

    def fae_prepForReload():
        """
        Handles clearing wrs notifs and unregistering the wndclass to allow 'reload' to work properly
        ASSUMES: renpy.windows
        """
        store.fae_clearNotifs()


    
    


