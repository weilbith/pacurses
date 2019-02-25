from urwid import SimpleFocusListWalker, CheckBox

from gui.menus.menu import Menu
from gui.abbreviation import abbreviate_text
from constants.menu_names import MenuNames
from pulse_audio.information import Information


CHECKBOX_WIDTH = 4


class MuteMenu(Menu):

    def __init__(self, width, state, redraw):
        info = Information()
        checkboxes = []

        for output in info.output_list:
            name = abbreviate_text(output.name, width - CHECKBOX_WIDTH - 2)
            checkbox = CheckBox(
                name,
                state=output.muted,
                on_state_change=self.mute_output,
                user_data=output
            )

            checkboxes.append(checkbox)

        walker = SimpleFocusListWalker(checkboxes)

        super(MuteMenu, self).__init__(walker, width, state, redraw)

    @property
    def name(self):
        return MenuNames.MUTE

    @property
    def header_text(self):
        return "(Un)Check a sink to (un)mute:"

    def mute_output(self, _, bool, output):
        output.muted = bool
        self.redraw_self()
