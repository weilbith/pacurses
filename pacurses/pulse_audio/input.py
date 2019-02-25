from pulse_audio.external import call_pacmd


class Input():

    def __init__(self, index):
        self.index = index

    @property
    def media(self):
        return self.get_info('media.name =', '"')

    @property
    def application(self):
        return self.get_info('application.name = ', '"')

    def get_info(self, filter, split):
        command = "list-sink-inputs"
        command += "| grep -A 30 'index: {0}'".format(self.index)
        command += "| grep '{0}'".format(filter)
        command += "| awk -F '{0}'".format(split) + " '{print $2}'"

        information = call_pacmd(command)

        return information.splitlines()[0] if information else information
