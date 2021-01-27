"""Tests for data extractor."""
from datetime import date as Date

import pytest

from paratex import Session, extract_attendance, fetch_sessions
from paratex.extractor import find_session_header


def default_session() -> Session:
    return extract_attendance(session_id=1783)


def test_title_extraction():
    assert default_session().title == "85ª Sessão Ordinária"


def test_date_extraction():
    assert default_session().date == Date(2019, 9, 19)


def test_sample_attendance_extraction():
    session = default_session()

    KNOWN_ATTENDANCES = {
        "Paulinha": ("Presente", None),
        "Ada De Luca": (
            "Outras",
            "Reunião do inventário referente ao falecimento de seu esposo.",
        ),
    }

    for parliamentary, attendance in KNOWN_ATTENDANCES.items():
        assert session.attendance[parliamentary] == attendance


def test_fetch_sessions_length():
    sessions = fetch_sessions(period=Date(2019, 8, 1))
    assert len(sessions) == 11


def test_fetch_sessions_dates():
    session_dates = [
        session_date for _, session_date in fetch_sessions(period=Date(2019, 8, 1))
    ]

    KNOWN_DATES = [
        Date(2019, 8, 28),
        Date(2019, 8, 27),
        Date(2019, 8, 22),
        Date(2019, 8, 21),
        Date(2019, 8, 20),
        Date(2019, 8, 15),
        Date(2019, 8, 14),
        Date(2019, 8, 13),
        Date(2019, 8, 8),
        Date(2019, 8, 7),
        Date(2019, 8, 6),
    ]

    for date in KNOWN_DATES:
        assert any(date == session_date for session_date in session_dates)
