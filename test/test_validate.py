from unittest import TestCase

from validate import tab_checker, full_tab_checker
import config as cfg

non_rest_pos = {5: 5, 4: 5}
good_rest_pos = {5: 'R', 4: 'r'}
good_line_pos = {4: '|'}
bad_rest_pos = {4: 'r', 3: 3}


class TestTabChecker(TestCase):

    def test_allow_good_tab(self):
        for pos in [non_rest_pos, good_rest_pos, good_line_pos]:
            tab_checker(pos.values(), 0, cfg.REST_CHARS, 'rest')

    def test_error_bad_tab(self):
        with self.assertRaises(AssertionError):
            tab_checker(bad_rest_pos.values(), 0, cfg.REST_CHARS, 'rest')


class TestFullTabChecker(TestCase):

    non_rest_pos = {5: 5, 4: 5}
    good_rest_pos = {5: 'R', 4: 'r'}
    good_line_pos = {4: '|'}
    bad_rest_pos = {4: 'r', 3: 3}

    def test_allow_good_tab(self):
        full_tab_checker([non_rest_pos, good_rest_pos, good_line_pos])

    def test_error_bad_tab(self):
        with self.assertRaises(AssertionError):
            full_tab_checker([non_rest_pos, good_rest_pos, good_line_pos, bad_rest_pos])
