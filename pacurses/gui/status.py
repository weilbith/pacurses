from urwid import Pile, Text, Divider

from gui.abbreviation import abbreviate_text, abbreviate_two_text
from pulse_audio.information import Information
from constants.palette_names import PaletteNames


ENUMERATION_PREFIX_WIDTH = 3


class Status(Pile):
    def __init__(self, width):
        info = Information()
        rows = []
        max_enumeration_item_length = width - ENUMERATION_PREFIX_WIDTH - 3

        rows.append(Text((PaletteNames.UNDERLINE, "Outputs:")))

        for output in info.output_list:
            state = "{0}%{1}".format(output.volume, " (muted)" if output.muted else "")
            name, state = abbreviate_two_text(
                output.name, state, max_enumeration_item_length
            )
            itemize_dot = "⊙" if info.output_default_index == output.index else "·"
            text = " {0} {1} - {2}".format(itemize_dot, name, state)
            rows.append(Text(text))

        rows.append(Divider())
        rows.append(Text((PaletteNames.UNDERLINE, "Inputs:")))

        for input in info.input_list:
            application, media = abbreviate_two_text(
                input.application, input.media, max_enumeration_item_length
            )
            text = " · {0} - {1}".format(application, media)
            rows.append(Text(text))

        super(Status, self).__init__(rows)
