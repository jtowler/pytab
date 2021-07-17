import config as cfg
import tab


def is_spec(pos: dict, check: str) -> bool:
    for note in pos.values():
        if str(note) not in check:
            return False
    return True


def read_tab_list(tab_list: list) -> list:
    lines = []
    for pos in tab_list:
        if is_spec(pos, cfg.REST_NOTES):
            lines.append([cfg.REST_FILL for i in cfg.STRING_RANGE])
        elif is_spec(pos, cfg.LINE_NOTES):
            lines.append([cfg.LINE_FILL for i in cfg.STRING_RANGE])
        else:
            lines.append([str(pos[i]) if i in pos else cfg.BLANK_CHAR
                          for i in cfg.STRING_RANGE])
    return lines


def format_tab(lines: list) -> list:
    stave = [f'{string}|' for string in cfg.TUNING]
    for line in lines:
        fill_len = max(map(len, line))
        for i, a in enumerate(line):
            stave[i] += cfg.BLANK_CHAR + a.rjust(fill_len, cfg.BLANK_CHAR)
    return stave


def display(stave: list) -> None:
    for s in stave:
        print(s)


if __name__ == '__main__':
    tabs = read_tab_list(tab.riff1)
    formatted_tabs = format_tab(tabs)
    display(formatted_tabs)
