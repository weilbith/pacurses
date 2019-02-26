from pulse_audio.external import call_pacmd
from pulse_audio.output import Output
from pulse_audio.input import Input


class Information:
    def __init__(self):
        pass

    @property
    def output_list(self):
        index_list = call_pacmd(
            "list-sinks | grep 'index' | awk -F ': ' '{print $2}'"
        ).splitlines()

        return [Output(index) for index in index_list]

    @property
    def input_list(self):
        index_list = call_pacmd(
            "list-sink-inputs | grep 'index' | awk -F ': ' '{print $2}'"
        ).splitlines()

        return [Input(index) for index in index_list]
