"""Utility methods to deal with date objects"""
from datetime import date as Date
from typing import Iterator, Tuple


def months_between(start: Date, end: Date) -> Iterator[Tuple[str, str]]:
    """Get the months from a start date to a end date.

    Returns:
        Iterator over tuples containing the month and its year, respectively
    """
    current_month = start.month
    current_year = start.year
    while current_year < end.year or (
        current_year == end.year and current_month <= end.month
    ):
        yield current_month, current_year
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
