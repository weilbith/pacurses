from pulse_audio.information import Information


ABBREVIATION_SUFFIX_STRING = "..."
DEFAULT_PREFIX_STRING = "*"


def abbreviate_text(text, length):
    if len(text) <= length:
        return text

    relative_length = length - len(ABBREVIATION_SUFFIX_STRING)
    return text[:relative_length] + ABBREVIATION_SUFFIX_STRING


def abbreviate_two_text(text_one, text_two, total_length):
    length_each_text = int(total_length / 2)
    text_one_length = len(text_one)
    text_two_length = len(text_two)

    if text_one_length < length_each_text:
        return (text_one, abbreviate_text(text_two, total_length - text_one_length))

    if text_two_length < length_each_text:
        return (abbreviate_text(text_one, total_length - text_two_length), text_two)

    return (
        abbreviate_text(text_one, length_each_text),
        abbreviate_text(text_two, length_each_text),
    )


def abbreviate_output(output, length, with_state=False):
    info = Information()
    default_output_prefix = DEFAULT_PREFIX_STRING if output.index == info.output_default_index else " "
    name = "{0}{1} {2}".format(output.index, default_output_prefix, output.name)
    length = length - len(default_output_prefix) - 3

    if not with_state:
        return abbreviate_text(name, length)

    else:
        state = "{0}%{1}".format(output.volume, " (muted)" if output.muted else "")
        name, state = abbreviate_two_text(name, state, length)
        return "{0} - {1}".format(name, state)


def abbreviate_input(input, length):
    concatenation_length = len(str(input.index)) + 6
    application, media = abbreviate_two_text(
        input.application, input.media, length - concatenation_length
    )

    return "{0}  {1} - {2}".format(input.index, application, media)

