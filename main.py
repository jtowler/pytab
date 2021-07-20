import config as cfg
import tab
from validate import full_tab_checker


def is_spec(pos: dict, check: str) -> bool:
    for note in pos.values():
        if str(note) not in check:
            return False
    return True


def is_message(pos: dict):
    return -1 in pos


def read_tab_list(tab_list: list) -> list:
    lines = []
    for pos in tab_list:
        if is_spec(pos, cfg.REST_CHARS):
            lines.append([cfg.REST_FILL for _ in cfg.STRING_RANGE])
        elif is_spec(pos, cfg.LINE_CHARS):
            lines.append([cfg.LINE_FILL for _ in cfg.STRING_RANGE])
        elif is_spec(pos, cfg.NEWLINE_CHARS):
            lines.append([cfg.NEWLINE_FILL for _ in cfg.STRING_RANGE])
        elif is_message(pos):
            lines.append(pos[-1])
        else:
            lines.append([str(pos[i]) if i in pos else cfg.BLANK_CHAR
                          for i in cfg.STRING_RANGE])
    return lines


def format_tab(lines: list) -> list:
    all_staves = []
    if type(lines[0]) == str:
        stave = []
    else:
        stave = [f'{string}|' for string in cfg.TUNING]

    for line in lines:
        if type(line) == str:
            all_staves += stave + [line]
            stave = [f'{string}|' for string in cfg.TUNING]

        elif all(string == cfg.NEWLINE_FILL for string in line):
            all_staves += stave
            stave = [f'{string}|' for string in cfg.TUNING]

        else:

            fill_len = max(map(len, line))
            for i, a in enumerate(line):
                stave[i] += cfg.BLANK_CHAR + a.rjust(fill_len, cfg.BLANK_CHAR)

    return all_staves + stave


def display(stave: list) -> None:
    for i, s in enumerate(stave):
        print(s)


if __name__ == '__main__':
    full_tab_checker(tab.full_tab)
    tabs = read_tab_list(tab.full_tab)
    formatted_tabs = format_tab(tabs)
    display(formatted_tabs)
