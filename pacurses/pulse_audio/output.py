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
        call_pacmd("set-sink-volume {0} {1}".format(self.index, new_base))

    @property
    def muted(self):
        return self.get_info('muted', split=': ') == 'yes'

    @muted.setter
    def muted(self, value):
        call_pacmd("set-sink-mute {0} {1}".format(self.index, value))

    def get_info(self, filter, split=' ', column=2):
        command = "list-sinks"
        command += "| grep -A 38 'index: {0}'".format(self.index)
        command += "| grep '{0}'".format(filter)
        command += "| awk -F '" + split + "' '{print $ " + str(column) + "}'"

        information = call_pacmd(command)

        return information.splitlines()[0] if information else information
