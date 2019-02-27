from urwid import ProgressBar

from gui.abbreviation import abbreviate_text


TEXT_PREFIX_WIDTH = 7  # In maximum 3 digits plus percentage character and minus.


class NamedProgressBar(ProgressBar):
    def __init__(
        self, normal, complete, current=0, done=None, satt=None, name="", width=20
    ):
        self.name = name
        self.max_text_length = width - TEXT_PREFIX_WIDTH
        done = (int(current / 100) + 1) * 100 if not done else done
        super(NamedProgressBar, self).__init__(normal, complete, current, done, satt)

    def get_text(self):
        name = abbreviate_text(self.name, self.max_text_length)
        return f"{self.current}% - {name}"
