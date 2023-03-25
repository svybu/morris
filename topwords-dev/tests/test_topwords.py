from topwords_main import count
import pytest


@pytest.mark.parametrize("input, combine, expected_output",
                         [('aaa aaa aaa bbb bbb ccc', 1, {'aaa': 3, 'bbb': 2, 'ccc': 1}),
                          ('aaa aaa aaa bbb bbb ccc', 2, {'aaa aaa': 2, 'aaa bbb': 1, 'bbb bbb': 1, 'bbb ccc': 1}),
                          ('aaa aaa aaa bbb bbb ccc', 3,
                           {'aaa aaa aaa': 1, 'aaa aaa bbb': 1, 'aaa bbb bbb': 1, 'bbb bbb ccc': 1})])
def test_count(input, combine, expected_output):
    assert count(input, combine) == expected_output


@pytest.mark.parametrize("input, combine,threshold, expected_output",
                         [('aaa aaa aaa bbb bbb ccc', 1, 2, {'aaa': 3}),
                          ('aaa aaa aaa bbb bbb ccc', 2, 2, {}),
                          ('aaa aaa aaa bbb bbb ccc', 2, 1, {'aaa aaa': 2})])
def test_count_threshold(input, combine, threshold, expected_output):
    assert count(input, combine, threshold) == expected_output
