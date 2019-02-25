from urwid import Pile, Text, Divider

from gui.abbreviation import abbreviate_input, abbreviate_output
from pulse_audio.information import Information
from constants.palette_names import PaletteNames


MAPPING_OPERATOR_STRING = " -> "


class Status(Pile):
    def __init__(self, width):
        info = Information()
        length = width - 3

        rows = []
        rows.append(Text((PaletteNames.UNDERLINE, "Outputs:")))
        rows.extend(
            [
                Text(" " + abbreviate_output(output, length, with_state=True))
                for output in info.output_list
            ]
        )

        rows.append(Divider())
        rows.append(Text((PaletteNames.UNDERLINE, "Inputs:")))
        rows.extend(
            [Text(" " + abbreviate_input(input, length)) for input in info.input_list]
        )

        rows.append(Divider())
        rows.append(Text((PaletteNames.UNDERLINE, "Mapping:")))

        rows.extend(
            [
                Text(
                    " {0}{1}{2}".format(
                        input.index, MAPPING_OPERATOR_STRING, input.mapped_output_index
                    )
                )
                for input in info.input_list
            ]
        )

        super(Status, self).__init__(rows)
