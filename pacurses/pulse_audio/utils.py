from constants.sink_types import SinkTypes
from pulse_audio.output import Output
from pulse_audio.input import Input


def get_sink_type(sink):
    if isinstance(sink, Output):
        return SinkTypes.OUTPUT

    elif isinstance(sink, Input):
        return SinkTypes.INPUT

    else:
        raise Exception(f"Was not able to detect the SinkType for the sink {sink}!")
