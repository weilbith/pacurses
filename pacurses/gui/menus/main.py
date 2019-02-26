from urwid import SimpleFocusListWalker, Button, AttrMap

from gui.menus.menu import Menu
from gui.abbreviation import abbreviate_text
from constants.menu_names import MenuNames
from constants.palette_names import PaletteNames


BUTTON_DECORATION_WIDTH = 2 * 2


class MainMenu(Menu):
    def __init__(self, width, state, redraw):
        self.redraw = redraw
        self.max_label_width = width - BUTTON_DECORATION_WIDTH

        buttons = []
        buttons.append(self.create_menu_button("Adjust Sink Volumes", MenuNames.VOLUME))
        buttons.append(self.create_menu_button("Mute Sinks", MenuNames.MUTE))
        buttons.append(self.create_menu_button("Set Default Sink", MenuNames.DEFAULT))

        walker = SimpleFocusListWalker(buttons)

        super(MainMenu, self).__init__(walker, width, state, redraw)

    @property
    def name(self):
        return MenuNames.MAIN

    @property
    def header_text(self):
        return "Select:"

    def create_menu_button(self, label, menu_name):
        label = abbreviate_text(label, self.max_label_width)
        button = Button(label, self.redraw, menu_name)
        decorated_button = AttrMap(button, None, focus_map=PaletteNames.REVERSED)
        return decorated_button
