"""Tests for data extractor."""
from datetime import date as Date

from pytest import mark

from paratex import (
    Session,
    extract_attendance,
    fetch_sessions,
    fetch_sessions_from_interval,
)


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
    sessions = fetch_sessions(Date(2019, 8, 6))
    assert len(sessions) == 1


@mark.parametrize(
    "start_date, end_date",
    [
        (Date(2020, 5, 5), Date(2020, 5, 5)),
        (Date(2020, 5, 5), Date(2020, 10, 5)),
        (Date(2020, 5, 5), Date(2021, 10, 5)),
    ],
)
def test_fetch_sessions_from_interval(start_date: Date, end_date: Date):
    sessions = fetch_sessions_from_interval(start_date, end_date)

    assert sessions
    assert all(start_date <= session[1] <= end_date for session in sessions)
