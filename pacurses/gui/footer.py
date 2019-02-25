from urwid import Pile, GridFlow, Button, Divider, ExitMainLoop, AttrMap

from gui.status import Status
from constants.menu_names import MenuNames
from constants.palette_names import PaletteNames
from constants.button_names import ButtonNames


class Footer(Pile):
    def __init__(self, width, button_list, switch_menu):
        divider = Divider()
        line = Divider(u"―", top=1, bottom=1)
        status = Status(width)

        buttons = []

        if ButtonNames.BACK in button_list:
            button = Button("Back", switch_menu, MenuNames.MAIN)
            button = AttrMap(button, PaletteNames.REVERSED, '')
            buttons.append(button)

        if ButtonNames.HELP in button_list:
            button = Button("Help", switch_menu, MenuNames.HELP)
            button = AttrMap(button, PaletteNames.REVERSED, '')
            buttons.append(button)

        if ButtonNames.CLOSE in button_list:
            button = Button("Close", self.exit)
            button = AttrMap(button, PaletteNames.REVERSED, '')
            buttons.append(button)

        button_grid = GridFlow(buttons, 9, 2, 0, "center")

        super(Footer, self).__init__([line, status, divider, button_grid, divider])
        self.button_list_index = 3

    @property
    def button_list(self):
        return self.contents[self.button_list_index][0]

    def exit(self, _):
        raise ExitMainLoop()

    def keypress(self, size, key):
        key = super(Footer, self).keypress(size, key)

        if key and key in 'hl':
            step = 1 if key == "l" else -1

            try:
                self.focus.focus_position = self.focus.focus_position + step

            except IndexError:
                pass

        else:
            return key
