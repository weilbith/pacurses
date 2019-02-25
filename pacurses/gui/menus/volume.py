from urwid import SimpleFocusListWalker

from gui.menus.menu import Menu, FOCUS_POSITION_INTERNAL
from gui.widgets.volume_slider import VolumeSlider
from pulse_audio.information import Information
from constants.menu_names import MenuNames


class VolumeMenu(Menu):
    def __init__(self, width, state, redraw):
        info = Information()
        slider_list = [
            VolumeSlider(output, self.redraw_self, width=width)
            for output in info.output_list
        ]

        walker = SimpleFocusListWalker(slider_list)

        super(VolumeMenu, self).__init__(walker, width, state, redraw)

    @property
    def name(self):
        return MenuNames.VOLUME

    @property
    def header_text(self):
        return "Adjust input volumes:"

    @property
    def current_state(self):
        state = super(VolumeMenu, self).current_state
        state[FOCUS_POSITION_INTERNAL] = [bar.focus_position for bar in self.body]

        return state

    def load_state(self, state):
        super(VolumeMenu, self).load_state(state)

        self.body[self.focus_position].set_focus(True)

        if FOCUS_POSITION_INTERNAL in state:
            for index, position in enumerate(state[FOCUS_POSITION_INTERNAL]):
                try:
                    self.body[index].focus_position = position

                except IndexError:
                    pass

    def set_output_volume(self, output, value):
        output.volume = value

    def keypress(self, size, key):
        key = super(VolumeMenu, self).keypress(size, key)

        if key and key in ("j", "k", "down", "up"):
            self.body[self.focus_position].set_focus(True)
            step = 1 if key in ("k", "up") else -1
            try:
                self.body[self.focus_position + step].set_focus(False)
            except IndexError:
                pass

        else:
            return key
