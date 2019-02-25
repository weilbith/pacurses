from urwid import ProgressBar

from gui.abbreviation import abbreviate_text


TEXT_PREFIX_WIDTH = 7  # In maximum 3 digits plus percentage character and minus.


class NamedProgressBar(ProgressBar):
    def __init__(
        self,
        normal,
        complete,
        current=0,
        done=100,
        satt=None,
        name="",
        width=20,
    ):
        self.name = name
        self.max_text_length = width - TEXT_PREFIX_WIDTH
        super(NamedProgressBar, self).__init__(normal, complete, current, done, satt)

    def get_text(self):
        name = abbreviate_text(self.name, self.max_text_length)
        name = " - {0}".format(name) if self.name else ""

        percentage = min(100, max(0, int(self.current * 100 / self.done)))
        percentage = "{0}%".format(str(percentage))

        return percentage + name
