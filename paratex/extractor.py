'''Attendance extractor module.'''
from dataclasses import dataclass
from datetime import date as Date
from typing import Dict, List, Optional, Tuple
import calendar

from bs4 import BeautifulSoup
from bs4.element import Tag
import requests


@dataclass
class Session:
    title: str
    date: Date
    attendance: Dict[str, Tuple[str, Optional[str]]]

    @staticmethod
    def make_url(session_id: int):
        BASE_URL = (
            'http://transparencia.alesc.sc.gov.br/'
            'presenca_plenaria_detalhes.php'
        )
        return f'{BASE_URL}?id={session_id}'


def extract_attendance(session_id: int) -> Session:
    '''
    Extracts every parliamentary's attendance in a given ALESC's meeting
    attendance HTML page.
    '''
    html = load_html(Session.make_url(session_id))
    soup = BeautifulSoup(html, 'html.parser')

    title, date = find_session_header(soup)
    date = date_from_str(date)

    att_table = find_attendance_table(soup)

    attendance = {}

    for parliamentary, state in iter_rows(att_table):
        parliamentary = parliamentary.text.strip()
        url = state.find('a')
        if url is None:
            presence = state.text.strip()
            justification = None
        else:
            presence = state.find('a').text.strip()
            justification = state.find('div').text.strip()
        attendance[parliamentary] = (presence, justification)

    return Session(title, date, attendance)


def fetch_sessions(period: Optional[Date] = None) -> List[Tuple[str, str]]:
    '''
    Retrieves a list of given period's session ids and their dates. The period
    comprehends only month/year, so day is ignored. If period is ommited, then
    last available period is used.
    '''
    url = 'http://transparencia.alesc.sc.gov.br/presenca_plenaria.php'

    if period is not None:
        url += f'?periodo={period.month}-{period.year}'

    html = load_html(url)

    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', {'summary': "Presença dos Deputados"})
    rows = table.findAll('tr', {'style': "text-align: center;"})

    date_href_tuples = []
    for tr in rows:
        tds = tr.findAll('td')
        session_date = date_from_str(tds[2].text)
        session_id = tds[3].find('a').attrs['href'].split('id=')[1]
        date_href_tuples.append((session_id, session_date))

    return date_href_tuples


def load_html(url: str) -> str:
    return requests.get(url).text


def date_from_str(s: str, delim: str = '/') -> Date:
    d, m, y = map(int, s.split(delim))
    return Date(y, m, d)


def iter_rows(table: Tag):
    '''Iter through a table's rows.'''
    trs = table.find_all('tr')
    for tr in trs:
        yield tr.find_all('td')


def find_session_header(soup: BeautifulSoup) -> Tuple[str, str]:
    '''Retrieves title and date from session page.'''
    title, date = soup.find(id='conteudo').h3.text.split('-')
    return title.strip(), date.strip()


def find_attendance_table(soup: BeautifulSoup) -> Tag:
    return soup.find(id='conteudo').table


def advance_month(date: Date) -> Date:
    month = date.month
    year = date.year + month // 12
    month = month % 12 + 1
    day = min(date.day, calendar.monthrange(year, month)[1])
    return Date(year, month, day)


def get_month_sessions_urls() -> List[str]:
    dt = Date(2011, 4, 1)
    URL = []
    BASE_URL = 'http://transparencia.alesc.sc.gov.br/'
    while dt < Date.today():
        dt = advance_month(dt)
        URL.append(
            f'{BASE_URL}/presenca_plenaria.php?'
            f'periodo={dt.month:02}-{dt.year}'
        )
    return URL
