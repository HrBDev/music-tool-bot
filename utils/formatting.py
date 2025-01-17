def pretty_print_size(number_of_bytes: float) -> str:
    """Pretty print file sizes


    **Keyword arguments:**
     - number_of_bytes (float) -- Number of bytes to convert

    **Returns:**
     A human-readable file size
    """
    units = [
        (1 << 50, ' PB'),
        (1 << 40, ' TB'),
        (1 << 30, ' GB'),
        (1 << 20, ' MB'),
        (1 << 10, ' KB'),
        (1, (' byte', ' bytes')),
    ]

    for factor, suffix in units:
        if number_of_bytes >= factor:
            break

    amount = int(number_of_bytes / factor)

    if isinstance(suffix, tuple):
        singular, multiple = suffix

        if amount == 1:
            suffix = singular
        else:
            suffix = multiple

    return str(amount) + suffix


def convert_seconds_to_human_readable_form(seconds: int) -> str:
    """Convert seconds to human-readable time format, e.g. 02:30

    **Keyword arguments:**
     - seconds (int) -- Seconds to convert

    **Returns:**
     Formatted string
    """
    if seconds <= 0:
        return "00:00"

    minutes = int(seconds / 60)
    remainder = seconds % 60

    minutes_formatted = str(minutes) if minutes >= 10 else "0" + str(minutes)
    seconds_formatted = str(remainder) if remainder >= 10 else "0" + str(remainder)

    return f"{minutes_formatted}:{seconds_formatted}"
