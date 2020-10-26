import pytmx


def load_map(map_file: str):
    """
    Returns loaded map

    :return tmx map_data:
    """
    map_data = pytmx.load_pygame(map_file)
    return map_data