import urwid
from urwid import (
    Divider,
    Frame,
    LineBox,
    Padding,
    Overlay,
    SolidFill,
    MainLoop,
    ExitMainLoop,
)

from gui.header import Header
from gui.menus.menu import Menu, MenuState, FOCUS_POSITION
from gui.menus.utils import get_menu
from gui.footer import Footer
from gui.palette import palette

from constants.menu_names import MenuNames
from constants.button_names import ButtonNames
from constants.palette_names import PaletteNames


PADDING_WIDTH = 2


class App:
    def __init__(self, dimensions):
        self._dimenstions = dimensions
        self.states = {}
        self.last_menu_name = None

        self.header = Header()
        self.menu = Divider()
        self.footer = Divider()
        self.frame = Frame(self.menu, header=self.header, footer=self.footer)

        self.switch_menu(None, MenuNames.MAIN)

    @property
    def width(self):
        return self._dimenstions[0]

    @property
    def height(self):
        return self._dimenstions[1]

    @property
    def inner_width(self):
        return self.width - 2 * PADDING_WIDTH - 2

    def switch_menu(self, _, menu_name):
        # TODO help zeugs.
        menu_name = (
            self.last_menu_name
            if isinstance(self.menu, Menu)
            and self.menu.name == MenuNames.HELP
            and self.last_menu_name
            else menu_name
        )

        self.last_menu_name = self.menu.name if menu_name == MenuNames.HELP else None

        if menu_name not in MenuNames:
            raise ValueError("Unkown menu '{0}'!".format(menu_name))

        if isinstance(self.menu, Menu):
            self.states[self.menu.name] = self.menu.current_state

        state = (
            self.states[menu_name]
            if menu_name in self.states
            else MenuState({FOCUS_POSITION: 0})
        )

        self.menu = get_menu(menu_name)(self.inner_width, state, self.switch_menu)
        self.header.text = self.menu.header_text
        self.frame.body = self.menu

        button_list = []
        button_list.extend([ButtonNames.BACK] if menu_name != MenuNames.MAIN else [])
        button_list.extend([ButtonNames.HELP] if menu_name != MenuNames.HELP else [])

        self.update_footer(button_list=button_list)

    def update_footer(self, button_list=[]):
        button_list.extend([ButtonNames.CLOSE])
        self.footer = Footer(self.inner_width, button_list, self.switch_menu)
        self.frame.footer = self.footer

    def global_input(self, key):
        if key == "q":
            if self.menu.name == MenuNames.MAIN:
                self.header.text = (
                    PaletteNames.WARNING,
                    "Press 'Q' to close the application!",
                )

            else:
                self.switch_menu(None, MenuNames.MAIN)

        if key == "Q":
            raise ExitMainLoop()

        if key == "H":
            self.switch_menu(None, MenuNames.HELP)

        if key == "tab":
            if self.frame.focus_position == 'body':
                self.frame.focus_position = 'footer'

            else:
                last_index = len(self.footer.button_list.cells) - 1
                position = self.footer.button_list.focus_position

                if position == last_index:
                    self.frame.focus_position = 'body'
                    self.footer.button_list.focus_position = 0

                else:
                    self.footer.button_list.focus_position = position + 1

    def start(self):
        padding = Padding(
            self.frame,
            left=PADDING_WIDTH,
            right=PADDING_WIDTH,
            width=self.inner_width,
            min_width=self.inner_width,
        )

        box = urwid.LineBox(padding, title="pacurses")

        overlay = Overlay(
            box,
            SolidFill(" "),
            align="center",
            width=self.width,
            valign="middle",
            height=self.height,
        )

        loop = MainLoop(overlay, palette=palette, unhandled_input=self.global_input)
        loop.run()


App((40, 25)).start()
