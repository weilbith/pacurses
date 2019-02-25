import subprocess


def call_pactl(command):
    return (
        subprocess.Popen(
            "pactl {0}".format(command), shell=True, stdout=subprocess.PIPE
        )
        .stdout.read()
        .decode("utf-8")
    )
