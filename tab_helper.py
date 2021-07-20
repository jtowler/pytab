LINE = [{6: 'l'}]
NEWLINE = LINE + [{6: 'N'}]
REST = {6: 'r'}


def section_builder(components: list, separator: list = LINE, title: str = None) -> list:
    interleaved = [] if title is None else [{-1: title}]
    for component in components:
        interleaved += component + separator
    return interleaved
