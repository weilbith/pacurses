from urwid import SimpleFocusListWalker, RadioButton

from gui.menus.menu import Menu
from gui.abbreviation import abbreviate_output
from constants.menu_names import MenuNames
from pulse_audio.information import Information


RADIO_BUTTON_WIDTH = 4


class DefaultMenu(Menu):

    def __init__(self, width, state, redraw):
        info = Information()
        length = width - RADIO_BUTTON_WIDTH - 2
        radio_buttons = []
        group = []

        for output in info.output_list:
            name = abbreviate_output(output, length)
            radio_button = RadioButton(
                group,
                name,
                state=output.default,
                on_state_change=self.set_default_output,
                user_data=output
            )

            radio_buttons.append(radio_button)

        walker = SimpleFocusListWalker(radio_buttons)

        super(DefaultMenu, self).__init__(walker, width, state, redraw)

    @property
    def name(self):
        return MenuNames.DEFAULT

    @property
    def header_text(self):
        return "Select the default output:"

    def set_default_output(self, _, value, output):
        output.default = value
        self.redraw_self()

