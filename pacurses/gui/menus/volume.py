from urwid import SimpleFocusListWalker

from gui.menus.menu import Menu, FOCUS_POSITION_INTERNAL
from gui.widgets.volume_slider import VolumeSlider
from pulse_audio.information import Information
from constants.menu_names import MenuNames
from constants.sink_types import SinkTypes


class VolumeMenu(Menu):
    def __init__(self, width, state, redraw, sink_type=SinkTypes.OUTPUT):
        info = Information()

        sink_list = (
            info.output_list if sink_type == SinkTypes.OUTPUT else info.input_list
        )

        slider_list = [
            VolumeSlider(sink, self.redraw_self, width=width)
            for sink in sink_list
        ]

        walker = SimpleFocusListWalker(slider_list)

        super(VolumeMenu, self).__init__(walker, width, state, redraw, sink_type)

    @property
    def name(self):
        return MenuNames.VOLUME

    @property
    def header_text(self):
        return f"Adjust {self.sink_type.name.lower()} volumes:"

    @property
    def current_state(self):
        state = super(VolumeMenu, self).current_state
        state[FOCUS_POSITION_INTERNAL] = [bar.focus_position for bar in self.body]

        return state

    def load_state(self, state):
        super(VolumeMenu, self).load_state(state)

        try:
            self.body[self.focus_position].set_focus(True)

        except IndexError:
            pass

        if FOCUS_POSITION_INTERNAL in state:
            for index, position in enumerate(state[FOCUS_POSITION_INTERNAL]):
                try:
                    self.body[index].focus_position = position

                except IndexError:
                    pass

    def set_sink_volume(self, sink, value):
        sink.volume = value

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
