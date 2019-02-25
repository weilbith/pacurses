from urwid import SimpleFocusListWalker, Button, AttrMap

from gui.menus.menu import Menu
from gui.abbreviation import abbreviate_text
from constants.menu_names import MenuNames
from constants.palette_names import PaletteNames


BUTTON_DECORATION_WIDTH = 2 * 2


class MainMenu(Menu):
    def __init__(self, width, state, redraw):
        buttons = []
        max_label_width = width - BUTTON_DECORATION_WIDTH

        label = abbreviate_text("Adjust Sink Volumes", max_label_width)
        button_volume = Button(label, redraw, MenuNames.VOLUME)
        buttons.append(AttrMap(button_volume, None, focus_map=PaletteNames.REVERSED))

        label = abbreviate_text("Mute Sinks", max_label_width)
        button_mute = Button(label, redraw, MenuNames.MUTE)
        buttons.append(AttrMap(button_mute, None, focus_map=PaletteNames.REVERSED))

        walker = SimpleFocusListWalker(buttons)

        super(MainMenu, self).__init__(walker, width, state, redraw)

    @property
    def name(self):
        return MenuNames.MAIN

    @property
    def header_text(self):
        return "Select:"
