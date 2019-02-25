from urwid import ListBox

from constants.menu_names import MenuNames


FOCUS_POSITION = "focus_position"
FOCUS_POSITION_INTERNAL = "focus_position_internal"


class Menu(ListBox):
    def __init__(self, body, width, state, redraw):
        self.width = width
        self.redraw = redraw

        super(Menu, self).__init__(body)

        self.load_state(state)

    @property
    def name(self):
        return MenuNames.MAIN

    @property
    def header_text(self):
        return ""

    @property
    def current_state(self):
        return MenuState({FOCUS_POSITION: self.focus_position})

    def load_state(self, state):
        if not isinstance(state, MenuState):
            raise ValueError(
                "Unknown state object type {0}. Can only load {1}!".format(
                    type(state).__name__, MenuState.__name__
                )
            )

        self.set_focus(state[FOCUS_POSITION])

    def redraw_self(self):
        self.redraw(None, self.name)

    def keypress(self, size, key):
        copy = key if key in ("down", "up") else None
        key = super(Menu, self).keypress(size, key)
        key = copy if copy else key

        if key and key in "jk":
            step = 1 if key == "j" else -1

            try:
                self.focus_position = self.focus_position + step

            except IndexError:
                pass

        return key


class MenuState(dict):
    def __init__(self, values={}):
        if FOCUS_POSITION not in values:
            raise Exception(
                "Menu state requires at least the {0} value!".format(FOCUS_POSITION)
            )

        super(MenuState, self).__init__(values)
