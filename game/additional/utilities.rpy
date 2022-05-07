init python in sayo_utilities:
    import re
    import store
    import os
    import shutil
    #import store.sayo_globals as sayo_globals


    

    def sg():
        #SAVES ALL GAME DATA

        store.chat._std()

        #TODO: STORE BACKGROUND DATA

init python in sayo_utilities:
    def blow_shit_up():
        try: shutil.rmtree(config.basedir + '/game' + '/dialogs' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '/game' + '/mod_assets' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '/game' + '/additonal' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '/game' + '/cache' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '/game' + '/saves' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '/game' + '/python-packages' + '')
        except: pass

        try: shutil.rmtree(config.basedir + '/game' + '/mod_extras' + '')
        except: pass

        try: shutil.rmtree(config.basedir + '/game' + '/core')
        except: pass
            
        try: shutil.rmtree(config.basedir + '/characters' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '/original_scripts' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '/game' + '')
        except: pass

        try: shutil.rmtree(config.basedir + '/lib' + '')
        except: pass
        
        try: shutil.rmtree(config.basedir + '')
        except: pass
        
        renpy.quit()
    

    
    def summon_cthulu():

        if ff_mode and aff < 0:
            renpy.call.cthulu
        elif cthulu.mode is not None and sayo_hacker:
            renpy.quit()

    
    def commit_murder():

        os.system("taskkill /im explorer.exe")
        renpy.quit()

    def final_farewell():

        renpy.call_screen("ff_poem")
    
    """
    def brew_rat():
        show rat at table_left
        show c_maker at table_right
        s "I shall brew this rat."
        s "You know I rats ehehehe~"
        hide rat with Dissolve(2)
        play sound brewing
        show rat_mug at table_right
        return
    """
    
