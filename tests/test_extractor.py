'''Tests for data extractor.'''
import pytest

from paratex import extract_attendance
from paratex.extractor import find_session_header


DEFAULT_ID = 1783


def test_title():
    assert extract_attendance(session_id=DEFAULT_ID)
