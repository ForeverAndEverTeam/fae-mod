default persistent._fae_notifs_enabled = False

default persistent._fae_notif_sounds = True

init python in fae_notifs:
    
    import os
    import store

    FAE_WINDOW = None

    from plyer import notification


    def notify(title, message):
        title = title
        message = message
        
        if renpy.windows or renpy.linux:

            return (
                notification.notify(
                    title=title,
                    message=message,
                    app_icon=(renpy.config.gamedir + '/mod_assets/icon.ico'),
                    timeout=10
                )
            )
        else:
            return None


    if renpy.windows:

        try:

            from plyer import notification

            can_show_notifs = True
        
        except ImportError:
            can_show_notifs = False

            store.fae_utilities.log("Couldn't import plyer")

        #from plyer import notification
        if store.fae_notifs.can_show_notifs:
            
            def notifyWindows():

                title = 'Sayori'
                message = 'I have something to tell you!'

                return (
                    notification.notify(
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
    