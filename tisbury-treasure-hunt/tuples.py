"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    return tuple(azara_record[1]) == rui_record[1]


def create_record(azara_record, rui_record):
    if compare_records(azara_record,rui_record):
        return azara_record + rui_record

    return "not a match"

def clean_up(combined_record_group):
    """
    Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    lines = []
    
    for _, record in enumerate(combined_record_group):
        formatted_record = (
            f"('{record[0]}', '{record[2]}', ('{record[3][0]}', '{record[3][1]}'), '{record[4]}')"
        )
        lines.append(formatted_record)
    
    return "\n".join(lines) + "\n"
