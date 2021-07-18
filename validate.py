import config as cfg
from typing import ValuesView


def full_tab_checker(tab_list: list) -> None:
    for i, pos in enumerate(tab_list):
        tab_checker(pos.values(), i, cfg.REST_CHARS, 'rest')
        tab_checker(pos.values(), i, cfg.LINE_CHARS, 'line')
        message_checker(pos, i, 'message')


def tab_checker(vals: ValuesView, ind: int, check_chars: str, name: str) -> None:
    isins = (str(v) in check_chars for v in vals)
    if any(isins) and not all(isins):
        raise AssertionError(f"Mix of {name} and other elements found in position {ind}")


def message_checker(pos: dict, ind: int, name: str):
    if -1 in pos and len(pos) > 1:
        raise AssertionError(f"Mix of {name} and other elements found in position {ind}")
    return False
