SUFFIX_STRING = "..."


def abbreviate_text(text, width):
    if len(text) <= width:
        return text

    relative_length = width - len(SUFFIX_STRING)
    return text[:relative_length] + SUFFIX_STRING


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
