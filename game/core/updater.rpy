define upd_link = "https://github.com/repos/ForeverAndEverTeam/fae-mod/upd.json"

init -1 python:
    
    class faeupdcheck(renpy.Displayable):
        import threading
        state_chk = 0
        state_ood = 1
        state_utd = 2
        state_to = 3



        def __init__(self, upd_link, init_state=None):

            renpy.Displayable.__init__()

            self.upd_link = upd_link

            self._check_thread = None
            self._thr_res = list()

            #Precursor stuff and/or break contingency

            self._state = init_state
            #TODO: BUTTON STATES

            #Threading
            self._check_thread = None
            self._thr_res = list() 

        def _checker(self):
            if self._state == self.state_chk:
                if self._state == state_ood:
                    #For the updater button to work
                    self._button_updactive
            
            elif self._state == self.state_pchk:
                self._thr_res = list()
                self._check_thread = threading.Thread(
                    target=faeupdcheck._sendRequest,
                    args=(self.upd_link, self._thr_res)
                )
                self._check_thread.start()
                self._state = self.state_chk

        @staticmethod
        def _sendRequest(upd_lnk, thr_res):
            import httplib
            import json
            web_con = httplib.HTTPConnection(
                url
            )
            try:
                web_con.connect()
                web_con.request("GET", "/", + json_file)
                json = sever_response.read()
            except httplib.HTTPExcepton:
                thr_res.append(faeupdcheck.state_to)
                return
            finally:
                web_con.close()












init python in updater:

    def upd_chk():
        
        import os
        import shutil

        g_upd = os.path.normcase(renpy.config.basedir + "/game/update")
        main_upd = os.path.normcase(renpy.config.basedir)
        if os.access(g_upd, os.F_OK):
            try:
                shutil.move(g_upd, main_upd)
            except:
                upd = True

        else:
            upd = renpy.store.updater.upd()

        renpy.game.persistent._faeupd = upd

        return None





init 10 python:

    def _secretcheck():
        import store.updater as updater

        upd_link = upd.checkUpdate()
        
        if not upd_link:
            return

        thr_res = list()
        faeupdcheck._sendRequest(upd_link, thr_res)

        if len(thr_res) > 1:
            state = thr_res.pop()

            if state == faeupdcheck.state_ood:
                pass
                #Happy Day! New update!(lol)
                #TODO: ADD NOTIFICATION STUFF HERE
        return
    
    def secretcheck():
        
        import threading
        
        threading.Thread(
            target=_secretcheck
        )
        thread.start()
        



label upd_stm:
    s "[player], I think you're running this through Steam..."
    s "Steam is a big ol' meanie. You'll have to update manually."
    s "Don't worry, it's easy!"
    s "All you have to do, is go {a=https://github.com/ForeverAndEverTeam/fae-mod/releases}here {/a} and download the latest release!"
    s "Nathan's a genius for remembering to make a contingency for Steam! Make sure you thank him."
    if persistent.playername == "Sayori":
        s "And don't tease him!"
    else:
        pass
    s "Make sure you say goodbye first!"
    return


label fc_upd_ins:

    if persistent.steam:
        call upd_stm

label upd_real:
    if persistent.steam:
        return
    $ update_link = store.upd_link.checkUpdates()

    if not persistent.pos_upd:
        call screen dialog(message="Couldn't update.", ok_action=Return())

    elif upd_link:
        python:
            add(faeupdcheck(
                upd_link,
                init_state=faeupd_forc_upd_init_state
                )
            )
            upd_sel = ui.interact()

        if upd_sel > 1:
            $ persistent.rec_upd = True
            $ updater.update(upd_link, restart=True)
            call QUIT
        else:
            pass
        return upd_sel
    return

                
    