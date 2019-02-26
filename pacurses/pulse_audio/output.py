from pulse_audio.external import call_pacmd


class Output():

    def __init__(self, index):
        self.index = index
        self.step = int(self.get_info('volume steps', split=': ')) / 100
        self.base = int(self.get_info('^\\s\\+volume: ', column=3))

    @property
    def name(self):
        return self.get_info('alsa.card_name = ', split='"')

    @property
    def volume(self):
        return int(self.base / self.step)

    @volume.setter
    def volume(self, value):
        new_base = int(value * self.step)
        call_pacmd(f"set-sink-volume {self.index} {new_base}")

    @property
    def muted(self):
        return self.get_info('muted', split=': ') == 'yes'

    @muted.setter
    def muted(self, value):
        call_pacmd(f"set-sink-mute {self.index} {value}")

    @property
    def default(self):
        return self.get_info('index: ', split=' ', column=1) == '*'

    @default.setter
    def default(self, value):
        if value:
            call_pacmd(f"set-default-sink {self.index}")

    def get_info(self, filter, split=' ', column=2):
        command = "list-sinks"
        command += f"| grep -A 38 'index: {self.index}'"
        command += f"| grep '{filter}'"
        command += "| awk -F '" + split + "' '{print $" + str(column) + "}'"

        information = call_pacmd(command)

        return information.splitlines()[0] if information else information
