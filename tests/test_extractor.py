'''Tests for data extractor.'''
import pytest

from paratex import extract_attendance, Session
from paratex.extractor import find_session_header


def default_session() -> Session:
    return extract_attendance(session_id=1783)


def test_title_extraction():
    assert default_session().title == '85ª Sessão Ordinária'


def test_date_extraction():
    assert default_session().date == '19-09-2019'


def test_sample_attendance_extraction():
    session = default_session()

    KNOWN_ATTENDANCES = {
        'Paulinha': ('Presente', None),
        'Ada De Luca': (
            'Outras',
            'Reunião do inventário referente ao falecimento de seu esposo.'
        ),
    }

    for parliamentary, attendance in KNOWN_ATTENDANCES.items():
        assert session.attendance[parliamentary] == attendance
