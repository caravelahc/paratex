"""Tests for date utils."""
from datetime import date as Date
from itertools import zip_longest
from typing import Tuple

from pytest import mark

from paratex.date_utils import months_between


@mark.parametrize(
    "start, end, expected_result",
    [
        (Date(2020, 5, 5), Date(2020, 5, 5), ((5, 2020),)),
        (Date(2020, 5, 5), Date(2020, 6, 5), ((5, 2020), (6, 2020))),
        (Date(2020, 12, 5), Date(2021, 1, 5), ((12, 2020), (1, 2021))),
    ],
)
def test_months_between(start: Date, end: Date, expected_result: Tuple[str, str]):
    months = months_between(start, end)
    assert all(
        date == expected_date
        for date, expected_date in zip_longest(months, expected_result)
    )
