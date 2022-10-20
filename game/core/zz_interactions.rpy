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
