init python:

    def enable_esc():

        global quick_menu
        quick_menu = True

    def disable_esc():
        """
        disables the escape key so you cant go to game menu
        NOTE: this also disables opening the game menu from other means
        """
        global quick_menu
        quick_menu = False

init 1 python:

    config.keymap['input_paste'] = ['ctrl_K_v']
    config.keymap['input_copy'] = ['ctrl_K_c']
    config.keymap['input_cut'] = ['ctrl_K_x']
    config.keymap['input_select_all'] = ['ctrl_K_a']
    config.keymap['input_move_select_left'] = ['ctrl_K_LEFT', 'ctrl_repeat_K_LEFT']
    config.keymap['input_move_select_right'] = ['ctrl_K_RIGHT', 'ctrl_repeat_K_RIGHT']
    config.keymap['input_move_select_home'] = ['ctrl_K_HOME']
    config.keymap['input_move_select_end'] = ['ctrl_K_END']

init 999 python in fae_inputs:
    import pygame
    pygame.scrap.init()

    setattr(renpy.display.behavior.Input, 'select_start_pos', None)
    setattr(renpy.display.behavior.Input, 'select_end_pos', 0)
    setattr(renpy.display.behavior.Input, 'select_last_end_pos', 0)
    setattr(renpy.display.behavior.Input, 'select_start_char', "\u231C")
    setattr(renpy.display.behavior.Input, 'select_end_char', "\u231F")


    def get_selected(self):

        if self.select_start_pos is None:
            return ""
        
        mark1_pos = min(self.select_start_pos, self.select_end_pos)
        mark2_pos = min(self.select_start_pos, self.select_end_pos)

        selected = self.content[mark1_pos+1:mark2_pos+1]

        return selected
    
    def remove_selected(self):

        if self.select_start_pos is None:
            return
        
        mark1_pos = min(self.select_start_pos, self.select_end_pos)
        mark2_pos = min(self.select_start_pos, self.select_end_pos)

        selected = self.get_selected()


        wo_selected = self.content[:mark1_pos+1]+self.content[mark2_pos+1:]

        self.content = wo_selected

        self.caret_pos = mark1_pos

        self.remove_selected_markers()

        return selected
    
    def selected_copy(self):

        if self.select_start_pos is None:
            return
        
        selected = self.get_selected()
        pygame.scrap.put(pygame.SCRAP_TEXT,selected)
    
    def selected_cut(self):

        cut = self.remove_selected()
        pygame.scrap.put(pygame.SCRAP_TEXT,cut)
    
    def input_paste(self):

        paste = pygame.scrap.get(pygame.SCRAP_TEXT)

        for char in paste:
            if self.allow and char not in self.allow:
                return
            if self.exclude and char in self.exclude:
                return
        
        self.content = self.content[:self.caret_pos]+paste+self.content[self.caret_pos:]

        self.caret_pos += len(paste)

        self.update_text(self.content, self.editable, check_size = True)
    
    def move_selected_left(self):
        """
            moves select_end_pos left
        """

        # check if we are starting a new selection
        if self.select_start_pos is None:

            # make sure we don't go into negative indices
            if self.caret_pos <= 0:
                return

            # set both delimiters at caret
            self.select_start_pos = self.caret_pos
            self.select_end_pos = self.caret_pos

        # stop at index 0
        if self.select_end_pos <= 0:
            return

        # all checks done, move select_end_pos to the left together with the caret
        self.select_end_pos -= 1
        self.caret_pos = self.select_end_pos

    def move_selected_right(self):
        """
            moves select_end_pos right
            works exactly as `move_select_left` except it moves it right >.>
        """
        # get lenght of content without delimiters
        length = len(get_content_wo_markers(self))

        if self.select_start_pos is None:
            if self.caret_pos >= length:
                return

            self.select_start_pos = self.caret_pos
            self.select_end_pos = self.caret_pos

        if self.select_end_pos >= length:
            return

        self.select_end_pos += 1
        self.caret_pos = self.select_end_pos+1

    def move_selected_home(self):
        """
            selects text between current caret pos to the beginning
        """
        # make sure there is something to select
        if self.caret_pos <= 0:
            return

        # if nothing's selected currently, set starting delimiter at caret pos
        if self.select_start_pos is None:
            self.select_start_pos = self.caret_pos

        # move ending delimiter and caret at the start
        self.select_end_pos = 0
        self.caret_pos = self.select_end_pos

    def move_selected_end(self):
        """
            selects text between current caret pos to the end of the text
            works almost exactly the same as `move_select_home`
        """
        # get lenght of content without delimiters
        length = len(get_content_wo_markers(self))

        if self.caret_pos >= length:
            return

        if self.select_start_pos is None:
            self.select_start_pos = self.caret_pos

        self.select_end_pos = length
        self.caret_pos = self.select_end_pos

    def move_selected_all(self):
        """
            selects all text
        """

        # get lenght of content without delimiters
        length = len(get_content_wo_markers(self))

        # check if there is anything to select
        if length <= 0:
            return

        # start selection at the beginning
        self.select_start_pos = 0

        # end at the end
        self.select_end_pos = length

    def render_selected_markers(self):
        """
            inserts delimiters into text and calls `update_text`
        """

        # check if selection has at all changed
        if self.select_end_pos == self.select_last_end_pos:
            return
        # selection has changed, update select_last_end_pos
        self.select_last_end_pos = self.select_end_pos

        # content without delimiters
        text_wo_markers = get_content_wo_markers(self)

        # select_start_pos is None so remove delimiters
        if self.select_start_pos is None:
            self.update_text(text_wo_markers, self.editable, check_size = True)
            return

        # Order positions for string indexing
        mark1_pos = min(self.select_start_pos, self.select_end_pos)
        mark2_pos = max(self.select_start_pos, self.select_end_pos)

        # insert delimiters into text
        text_w_markers = text_wo_markers[:mark1_pos]+"\u231C"+text_wo_markers[mark1_pos:mark2_pos]+"\u231F"+text_wo_markers[mark2_pos:]

        # update text
        self.update_text(text_w_markers, self.editable, check_size = True)

    def get_content_wo_markers(self):
        """
            returns content without delimiters
        """
        # If nothing is selected, return empty string
        if self.select_start_pos is None:
            return self.content

        # return content without delimiters
        #NOTE: does not change self.content
        return self.content.replace(self.select_start_char, '').replace(self.select_end_char, '')

    def remove_selected_markers(self):
        """
            removes delimiters from content
        """

        # If nothing's selected, return
        if self.select_start_pos is None:
            return

        # remove delimiters from content
        self.content = get_content_wo_markers(self)

        # make sure caret isn't outside of text bounds now that we've removed delimiters, essentially 2 characters
        length = len(self.content)
        self.caret_pos = min(length, self.select_end_pos)

        # reset selection values
        self.select_start_pos = None
        self.select_last_end_pos = None

        # update text
        self.update_text(self.content, self.editable, check_size = True)


    # Add new methods to the Input class
    setattr(renpy.display.behavior.Input, 'move_selected_left', move_selected_left)
    setattr(renpy.display.behavior.Input, 'move_selected_right', move_selected_right)
    setattr(renpy.display.behavior.Input, 'move_selected_home', move_selected_home)
    setattr(renpy.display.behavior.Input, 'move_selected_end', move_selected_end)
    setattr(renpy.display.behavior.Input, 'render_selected_markers', render_selected_markers)
    setattr(renpy.display.behavior.Input, 'remove_selected_markers', remove_selected_markers)
    setattr(renpy.display.behavior.Input, 'move_selected_all', move_selected_all)
    setattr(renpy.display.behavior.Input, 'selected_copy', selected_copy)
    setattr(renpy.display.behavior.Input, 'selected_cut', selected_cut)
    setattr(renpy.display.behavior.Input, 'input_paste', input_paste)
    setattr(renpy.display.behavior.Input, 'get_selected', get_selected)
    setattr(renpy.display.behavior.Input, 'remove_selected', remove_selected)

    # renpy's function for detecting and processing keyboard events
    map_event = renpy.display.behavior.map_event

    # `event` overwrite
    def event_ov(self, ev, x, y, st):
        """
            editted renpy's `event` method
        """
        self.old_caret_pos = self.caret_pos

        if not self.editable:
            return None

        l = len(self.content)

        raw_text = None

        if map_event(ev, "input_backspace"):
            # if something is selected, remove it
            if self.select_start_pos is not None:
                self.remove_selected()

            # if not, do normal backspace stuff
            elif self.content and self.caret_pos > 0:
                content = self.content[0:self.caret_pos-1] + self.content[self.caret_pos:l]
                self.caret_pos -= 1
                self.update_text(content, self.editable)

            renpy.display.render.redraw(self, 0)
            raise renpy.display.core.IgnoreEvent()

        elif map_event(ev, "input_enter"):
            # remove delimiters from text because we are "submiting" it
            self.remove_selected_markers()

            content = self.content

            if self.edit_text:
                content = content[0:self.caret_pos] + self.edit_text + self.content[self.caret_pos:]

            if self.value:
                return self.value.enter()

            if not self.changed:
                return content

        elif map_event(ev, "input_left"):
            # if something's selected, cancel selectiong
            if self.select_start_pos is not None:
                self.remove_selected_markers()

            # otherwise move caret left
            elif self.caret_pos > 0:
                self.caret_pos -= 1
                self.update_text(self.content, self.editable)

            renpy.display.render.redraw(self, 0)
            raise renpy.display.core.IgnoreEvent()

        elif map_event(ev, "input_right"):
            # same as left
            if self.select_start_pos is not None:
                self.remove_selected_markers()

            elif self.caret_pos < l:
                self.caret_pos += 1
                self.update_text(self.content, self.editable)

            renpy.display.render.redraw(self, 0)
            raise renpy.display.core.IgnoreEvent()

        elif map_event(ev, "input_delete"):
            # same as backspace, but delete

            if self.select_start_pos is not None:
                self.remove_selected()

            elif self.caret_pos < l:
                content = self.content[0:self.caret_pos] + self.content[self.caret_pos+1:l]
                self.update_text(content, self.editable)

            renpy.display.render.redraw(self, 0)
            raise renpy.display.core.IgnoreEvent()

        elif map_event(ev, "input_home"):
            self.caret_pos = 0
            self.update_text(self.content, self.editable)
            renpy.display.render.redraw(self, 0)
            raise renpy.display.core.IgnoreEvent()

        elif map_event(ev, "input_end"):
            self.caret_pos = l
            self.update_text(self.content, self.editable)
            renpy.display.render.redraw(self, 0)
            raise renpy.display.core.IgnoreEvent()

        # (almost) all logic handled inside funcions, no need for explaining all of them
        elif map_event(ev, "input_select_all"):
            self.move_selected_all()

        elif map_event(ev, "input_move_select_left"):
            self.move_selected_left()

        elif map_event(ev, "input_move_select_right"):
            self.move_selected_right()

        elif map_event(ev, "input_move_select_home"):
            self.move_selected_home()

        elif map_event(ev, "input_move_select_end"):
            self.move_selected_end()

        elif map_event(ev, "input_copy"):
            self.selected_copy()

        elif map_event(ev, "input_cut"):
            self.selected_cut()

        elif map_event(ev, "input_paste"):
            # if something is selected, remove it
            if self.select_start_pos is not None:
                self.remove_selected()

            # paste at caret pos
            self.input_paste()

        elif ev.type == pygame.TEXTEDITING:
            self.update_text(self.content, self.editable, check_size=True)

            raise renpy.display.core.IgnoreEvent()

        elif ev.type == pygame.TEXTINPUT:
            self.edit_text = ""
            raw_text = ev.text

        elif ev.type == pygame.KEYDOWN:

            if ev.unicode and ord(ev.unicode[0]) >= 32:
                raw_text = ev.unicode
            elif renpy.display.interface.text_event_in_queue():
                raw_text = ''

        if raw_text is not None:

            text = ""

            for c in raw_text:

                if self.allow and c not in self.allow:
                    continue
                if self.exclude and c in self.exclude:
                    continue

                text += c

            if self.length:
                remaining = self.length - len(self.content)
                text = text[:remaining]

            if text:
                # if something's typed, cancel selection
                if self.select_start_pos is not None:
                    self.remove_selected()

                content = self.content[0:self.caret_pos] + text + self.content[self.caret_pos:l]
                self.caret_pos += len(text)

                self.update_text(content, self.editable, check_size=True)

            raise renpy.display.core.IgnoreEvent()

        # if something is selected, call delimiter render function
        if self.select_start_pos is not None:
            self.render_selected_markers()
        else:
            self.remove_selected_markers()

    # overwrite original event function with our event_ov
    setattr(renpy.display.behavior.Input, 'event', event_ov)



init -1 python:
    
    def init_qabs():

        config.keymap["dlg"] = ["t", "T"]
        config.keymap["music"] = ["m", "M"]
        config.keymap["games"] = ["g", "G"]
        config.keymap["Mute"] = ["shift_m", "shift_M"]
        #config.keymap["inc_musicvol"] = [
        #    "shift_K_PLUS","K_EQUALS","K_KP_PLUS"
        #]
        #config.keymap["dec_musicvol"] = [
        #    "K_MINUS","shift_K_UNDERSCORE","K_KP_MINUS"
        #]

        config.underlay.append(
            renpy.Keymap(dlg=dlg)
        )

        config.underlay.append(
            renpy.Keymap(music=music_init)
        )

        config.underlay.append(
            renpy.Keymap(games=mg)
        )

        config.underlay.append(
            renpy.Keymap(Mute=fae_music.mute())
        )
        #config.underlay.append(
        #    renpy.Keymap(inc_musicvol=inc_vol)
        #)
        #config.underlay.append(
        #    renpy.Keymap(dec_musicvol=red_vol)
        #)
    

init -50 python:

    def fae_reg_keymap(keymap_name, keymap_label, *keys):

        if not renpy.has_label(keymap_label):
            fae_utilities.log("[ERROR]: Attempted to register label for label that doesn't exist.", fae_utils.SEVERITY_WARN)
        
        fae_reg_keymap_key(
            keymap_name,
            lambda: renpy.call_in_new_context(keymap_label),
            *keys
        )

    def fae_reg_keymap_key(keymap_name, keymap_action, *keys):

        if keymap_name in config.keymap:
            fae_utilities.log("ERROR: Attempted to register a new keymap under an existing name. Ignoring.", fae_utilities.SEVERITY_WARN)
            return
        
        if not callable(keymap_action):
            fae_utilities.log("ERROR: keymap action provided is not callable. Ignoring...", fae_utilities.SEVERITY_WARN)
            return
    
        config.keymap[keymap_name] = keys

        config.underlay.append(renpy.Keymap(**{keymap_name: keymap_action}))



init -10 python in fae_interactions:

    import ccmath.ccmath as cmath

    import store
    import store.fae_sprites as fae_sprites
    import store.fae_utilities as fae_utilities


    class FAEClickZoneMgr(object):

        def __init__(self):
            self._zoom_cz = {}

            self._zones = {}

        
        def __contains__(self, item):
            return item in self._zones

        def __getitem__(self, key):

            return self.get(key, fae_sprites.zoom_level)

        def __iter__(self):
            for zone_key in self._zones:
                yield zone_key, self[zone_key]
        
        def add(self, zone_key, cz):

            if zone_key in self._zones:
                return

            self._zones[zone_key] = cz

            cz_d = self._zoom_cz.get(fae_sprites.default_zoom_level, {})
            cz_d[zone_key] = cz
            self._zoom_cz[fae_sprites.default_zoom_level] = cz_d
        
        def _cz_iter(self):

            for zl, zl_d in self._zoom_cz.items():
                for zone_key, cz in zl_d.items():
                    yield zone_key, zl, cz
        
        def _debug(self, value):

            for zk, zl, cz in self._cz_iter():
                cz._debug_back = value
        

        def get(self, zone_key, zl):

            if zl not in self._zoom_cz:
                self.zoom_to(zl)
            
            return self._zoom_cz.get(zl, {}).get(zone_key, None)

        def remove(self, zone_key):

            if zone_key not in self._zones:
                return

            self._zones.pop(zone_key)

            for zone_d in self._zoom_cz.values():
                if zone_key in zone_d:
                    zone_d.pop(zone_key)
        
        def set_disables(self, zone_key, value):

            for zl_d in self._zoom_cz.values():
                cz - zl_d.get(zone_key, None)
                if cz is not None:
                    cz.disabled = value
        

        def zoom_to(self, zoom_level):

            zl_set = self._zoom_cz.get(zoom_level, {})

            for zone_key, cz in self._zones.items():

                if zone_key not in zl_set:
                    new_cz = store.FAEClickZone.copyfrom(
                        cz,
                        vx_list_zoom(zoom_level, cz.corners)
                    )
                    zl_set[zone_key] = new_cz
            
            self._zoom_cz[zoom_level] = zl_set
    

    ZONE_CHEST = "chest"
    ZONE_CHEST_1_L = "chest-1-l"
    ZONE_CHEST_1_M = "chest-1-m"
    ZONE_CHEST_1_R = "chest-1-r"
    ZONE_HEAD = "head"
    ZONE_NOSE = "nose"
    ZONE_EYE_E_L = "eye-e-l"
    ZONE_EYE_E_R = "eye-e-r"
    ZONE_MOUTH_A = "mouth-a"

    cz_defs = {
        ZONE_CHEST: [
            (514, 453), # (her) right top
            (491, 509),
            (489, 533),
            (493, 551),
            (506, 573),
            (525, 588),
            (541, 592),
            (650, 586), # middle below apex
            (709, 592),
            (761, 592),
            #(787, 580),
            (790, 585),
            #(806, 559),
            (810, 560),
            (813, 536),
            (813, 517),
            (789, 453),
        ],
        ZONE_CHEST_1_R: [
            (514, 453), # (her) right top
            (491, 509),
            (489, 533),
            (493, 551),
            (498, 555), # (her) right to arm
            (508, 498),
            (515, 453),
        ],
        ZONE_CHEST_1_M: [
            (568, 453), # (her) right top
            (568, 590), # (her) right bottom
            (650, 586), # middle below apex
            (728, 592), # (her) left bottom
            (735, 453), # (her) left top
        ],
        ZONE_CHEST_1_L: [
            (782, 453), # (her) left top
            (784, 474),
            (790, 516),
            (801, 570), # (her) left to arm
            (810, 560),
            (813, 536),
            (813, 517),
            (789, 453),
        ],
        ZONE_HEAD: [
            (634, 68-100),
            (597, 73-100),
            (552, 91-100),
            (540, 94-100),
            (531, 4),
            (517, 42),
            (498, 80),
            (486, 144),
            (708, 144),
            (778, 178),
            (792, 129),
            (792, 80),
            (777, 30),
            (751, 99-100),
            (690, 71-100),
        ],
        ZONE_NOSE: [
            (629, 240),
            (623, 252),
            (629, 258),
            (633, 252),
        ],
    }


    FOCAL_POINT = (640, 750)
    FOCAL_POINT_UP = (640, 740)

    ZOOM_INC_PER = 0.04

    def get_vx(zone_enum):

        return cz_defs.get(zone_enum, [])

    def z_vx_list_zoom(zoom_level, zone_enum):

        vx_list = cz_defs.get(zone_enum, None)
        if vx_list is None:
            return []

        return vx_list_zoom(zoom_level, vx_list)

    def vx_list_zoom(zoom_level, vx_list):

        if zoom_level == fae_sprites.default_zoom_level:
            return list(vx_list)

        return _vx_list_zoom(
            zoom_level,
            vx_list,
            zoom_level < fae_sprites.default_zoom_level
        )

    def _vx_list_zoom(zoom_level, vx_list, zoom_out):
       
        if zoom_out:
            zoom_diff = fae_sprites.default_zoom_level - zoom_level
            per_mod = -1 * (zoom_diff * ZOOM_INC_PER)
            xfc, yfc = FOCAL_POINT
            yfc_offset = 0

        else:
            zoom_diff = zoom_level - fae_sprites.default_zoom_level
            per_mod = zoom_diff * ZOOM_INC_PER
            xfc, yfc = FOCAL_POINT_UP
            yfc_offset = -1 * zoom_diff * fae_sprites.y_step

        # now process all pts
        new_vx_list = []
        for xcoord, ycoord in vx_list:
            # first, normalize the pt to origin
            xcoord -= xfc
            ycoord -= (yfc + yfc_offset)

            # now convert the pt into polar coords
            radius, angle = cmath.polar(xcoord, ycoord)

            # modify the radius by the appropraite percent val
            radius += (radius * per_mod)

            # convert the new polar coord back into regular coords
            new_x, new_y = cmath.rect(radius, angle)

            # unnormalize to get the real x, y and save
            new_vx_list.append((
                int(new_x + xfc),
                int(new_y + yfc)
            ))

        return new_vx_list


init -9 python:

    class FAEZoomableInteractable(renpy.Displayable):

        ZONE_ACTION_NONE = 0
        ZONE_ACTION_RET = 1
        ZONE_ACTION_JUMP = 2
        ZONE_ACTION_END = 3
        ZONE_ACTION_RST = 4

        def __init__(
                self,
                cz_manager,
                zone_actions=None,
                zone_order=None,
                start_zoom=None,
                debug=False
        ):

            if zone_actions is None:
                zone_actions = {}
            if zone_order is None:
                zone_order = []
            if start_zoom is None:
                start_zoom = store.fae_sprites.zoom_level

            self._cz_man = cz_manager
            self.zones_stat = {}
            self._zones_action = zone_actions
            self._zones_order = zone_order
            self._zones_unorder = {}

            self._last_zoom_level = start_zoom

            self._end_int = None
            self._rst_int = False
            self._jump_to = None
            self._zk_click = None
            self._ret_val = None

            self._debug = debug
            if debug:
                self._cz_man._debug(True)

            self._build_zones()

            super(FAEZoomableInteractable, self).__init__()

        def add_zone(self, zone_key, cz):

            if zone_key in self._cz_man:
                return

            self._cz_man.add(zone_key, cz)
            if zone_key not in self._zones_order:
                self._zones_unorder[zone_key] = None
            if zone_key not in self.zones_stat:
                self.zones_stat[zone_key] = 0

        
        def adjust_for_zoom(self):

            if self._last_zoom_level == store.fae_sprites.zoom_level:
                return

            self._zone_zoom(store.fae_sprites.zoom_level)
            self._last_zoom_level = store.fae_sprites.zoom_level
        

        def _build_zones(self):

            for zone_key, cz in self._cz_man:
                self.zones_stat[zone_key] = 0
                if zone_key not in self._zones_order:
                    self._zones_unorder[zone_key] = None
        

        def check_click(self, ev, x, y, st):

            for zone_key, cz in self.zone_iter():
                if cz.event(ev, x, y, st) is not None:
                    return zone_key
            
            return None

        def check_over(self, x, y):

            for zone_key, cz in self.zone_iter():
                if cz._isOverMe(x, y):
                    return zone_key
            
            return None

        def clicks(self, zone_key):

            return self.zones_stat.get(zone_key, 0)

        def disable_zone(self, zone_key):

            self._cz_man.set_disabled(zone_key, True)

        def enable_zone(self, zone_key):

            self._cz_man.set_disabled(zone_key, False)
        
        def event(self, ev, x, y, st):

            self.event_begin(ev, x, y, st)
            return self.event_end(ev, x, y, st)

        def event_begin(self, ev, x, y, st):

            self.adjust_for_zoom()

            self._rst_int = False
            self._end_int = None
            self._jump_to = None
            self._ret_val = None

            self._zk_click = self.click_check(ev, x, y, st)
            if self._zk_click is not None:
                self.zones_stat[self._zk_click] += 1
                self._ret_val = self.zone_action(self._zk_click)
            
            return self._zk_click
        
        def event_end(self, ev, x, y, st):

            if self._jump_to is not None:
                renpy.jump(self._jump_to)
            
            if self._rst_int:
                renpy.restart_interaction()
            
            else:
                renpy.end_interaction(self._end_int)
            
            return self._ret_val

        def remove_zone(self, zone_key):

            self._cz_man.remove(zone_key)
            if zone_key in self._zones_unorder:
                self._zones_unorder.pop(zone_key)
        
        def render(self, width, height, st, at):
            """
            By default, we will not render unless debug mode is on
            """
            r = renpy.Render(width, height)

            if not self._debug:
                return r

            renders = []

            # render in reverse zone order for visual clarity
            for zone_key, cz in self.zone_iter_r():
                if not cz.disabled:
                    renders.append(renpy.render(cz, width, height, st, at))

            for render in renders:
                r.blit(render, (0, 0))

            return r

        def zone_action(self, zone_key):

            action = self._zones_action.get(zone_key, None)
            if action is None:
                # return zone key
                return zone_key

            if isinstance(action, str):
                if renpy.has_label(action):
                    # label to jump to
                    self._jump_to = action

                # otherwise return like zone key
                return action

            if action == 1:
                # end interaction
                self._end_int = True

            elif action == 2:
                # restart interaction
                self._rst_int = True

            # othewise, do nothing
            return None

        def zone_iter(self):

            for zone_key in self._zones_order:
                cz = self._cz_man[zone_key]
                if cz is not None:
                    yield zone_key, cz

            for zone_key in self._zones_unorder:
                yield zone_key, self._cz_man[zone_key]

        def zone_iter_r(self):

            for zone_key in self._zones_unorder:
                yield zone_key, self._cz_man[zone_key]

            for zone_key in self._zones_order:
                cz = self._cz_man[zone_key]
                if cz is not None:
                    yield zone_key, cz

        def _zone_zoom(self, zoom_level):
            
            self._cz_man.zoom_to(zoom_level)

