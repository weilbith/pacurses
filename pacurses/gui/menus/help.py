from urwid import SimpleFocusListWalker, Text, Divider

from gui.menus.menu import Menu
from constants.menu_names import MenuNames
from constants.palette_names import PaletteNames


class HelpMenu(Menu):
    def __init__(self, _, width, state, redraw, sink_type=None):
        text = []

        text.append(Text((PaletteNames.UNDERLINE, "1. Section")))
        text.append(Text("Was sollte man auch sonst mehr haben wollen,ich weiss wes auch nicht"))

        text.append(Divider())

        text.append(Text((PaletteNames.UNDERLINE, "2. Section")))
        text.append(Text("Was sollte man auch sonst mehr haben wollen,ich weiss wes auch nicht"))

        walker = SimpleFocusListWalker(text)

        super(HelpMenu, self).__init__(walker, sink_type, width, state, redraw)

    @property
    def name(self):
        return MenuNames.HELP

    @property
    def header_text(self):
        return "Help"

