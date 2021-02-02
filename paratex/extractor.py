"""Attendance extractor module."""
import calendar
from dataclasses import dataclass
from datetime import date as Date
from typing import Dict, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


@dataclass
class Session:
    title: str
    date: Date
    attendance: Dict[str, Tuple[str, Optional[str]]]

    @staticmethod
    def make_url(session_id: int):
        BASE_URL = "http://transparencia.alesc.sc.gov.br/presenca_plenaria_detalhes.php"
        return f"{BASE_URL}?id={session_id}"


def extract_attendance(session_id: int) -> Session:
    """
    Extracts every parliamentary's attendance in a given ALESC's meeting
    attendance HTML page.
    """
    html = load_html(Session.make_url(session_id))
    soup = BeautifulSoup(html, "html.parser")

    title, date = find_session_header(soup)
    date = date_from_str(date)

    att_table = find_attendance_table(soup)

    attendance = {}

    for parliamentary, state in iter_rows(att_table):
        parliamentary = parliamentary.text.strip()
        url = state.find("a")
        if url is None:
            presence = state.text.strip()
            justification = None
        else:
            presence = state.find("a").text.strip()
            justification = state.find("div").text.strip()
        attendance[parliamentary] = (presence, justification)

    return Session(title, date, attendance)


def fetch_sessions_from_interval(
    start: Optional[Date] = None, end: Optional[Date] = None
) -> List[Tuple[str, str]]:
    """
    Retrieves a list of given period's session ids and their dates. The period
    comprehends only month/year, so day is ignored. If period is ommited, then
    last available period is used. If end is ommited use current date as end.
    """

    if end is None and start is not None:
        end = Date.today()

    if end.year < start.year or (end.year == start.year and end.month < start.month):
        raise ValueError("End date must be after start date")

    url = "http://transparencia.alesc.sc.gov.br/presenca_plenaria.php"
    query = ""
    sessions = list()

    if start is None and end is None:
        sessions.append(fetch_session(url))
    else:
        for delta_year in range(end.year - start.year):
            if delta_year == 0:
                for month in range(start.month, 13):
                    query = f"?periodo={month:02}-{start.year}"
                    sessions.append(fetch_session(url + query))
            elif delta_year == (end.year - start.year):
                for month in range(1, end.month + 1):
                    query = f"?periodo={month:02}-{end.year}"
                    sessions.append(fetch_session(url + query))
            else:
                for month in range(1, 13):
                    query = f"?periodo={month:02}-{start.year + delta_year}"
                    sessions.append(fetch_session(url + query))

    return sessions


def fetch_session(url: str) -> List[Tuple[str, str]]:
    """
    Accesses a session's attendance page URL and returns the attendance table
    columns.
    """
    html = load_html(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"summary": "Presença dos Deputados"})

    if table is not None:
        rows = table.findAll("tr", {"style": "text-align: center;"})

        date_href_tuples = []
        for tr in rows:
            tds = tr.findAll("td")
            session_date = date_from_str(tds[2].text)
            session_id = tds[3].find("a").attrs["href"].split("id=")[1]
            date_href_tuples.append((session_id, session_date))

        return date_href_tuples
    else:
        return []


def load_html(url: str) -> str:
    return requests.get(url).text


def date_from_str(s: str, delim: str = "/") -> Date:
    d, m, y = map(int, s.split(delim))
    return Date(y, m, d)


def iter_rows(table: Tag):
    """Iter through a HTML table's rows."""
    trs = table.find_all("tr")
    for tr in trs:
        yield tr.find_all("td")


def find_session_header(soup: BeautifulSoup) -> Tuple[str, str]:
    """Retrieves title and date from a session's attendance page."""
    title, date = soup.find(id="conteudo").h3.text.split("-")
    return title.strip(), date.strip()


def find_attendance_table(soup: BeautifulSoup) -> Tag:
    return soup.find(id="conteudo").table


def advance_month(date: Date) -> Date:
    month = date.month
    year = date.year + month // 12
    month = month % 12 + 1
    day = min(date.day, calendar.monthrange(year, month)[1])
    return Date(year, month, day)


def get_month_sessions_urls() -> List[str]:
    starting_date = Date(2011, 4, 1)
    URL = []
    BASE_URL = "http://transparencia.alesc.sc.gov.br/"
    while starting_date < Date.today():
        starting_date = advance_month(starting_date)
        URL.append(
            f"{BASE_URL}/presenca_plenaria.php?"
            f"periodo={starting_date.month:02}-{starting_date.year}"
        )
    return URL
