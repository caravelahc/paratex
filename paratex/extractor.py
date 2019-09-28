'''Attendance extractor module.'''
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from bs4 import BeautifulSoup
from bs4.element import Tag
import requests


@dataclass
class Session:
    title: str
    date: str
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


def last_sessions() -> List[Tuple[str, str]]:
    '''
    Retrieves a list of last month's session ids and their dates.
    '''
    url = 'http://transparencia.alesc.sc.gov.br/presenca_plenaria.php'
    html = load_html(url)

    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', {'summary': "Presença dos Deputados"})
    rows = table.findAll('tr', {'style': "text-align: center;"})

    date_href_tuples = []
    for tr in rows:
        tds = tr.findAll('td')
        date = tds[2].text
        session_id = tds[3].find('a').attrs['href'].split('id=')[1]
        date_href_tuples.append((date, session_id))

    return date_href_tuples


def load_html(url: str) -> str:
    return requests.get(url).text


def iter_rows(table: Tag):
    '''Iter through a table's rows.'''
    trs = table.find_all('tr')
    for tr in trs:
        yield tr.find_all('td')


def find_session_header(soup: BeautifulSoup) -> Tuple[str, str]:
    '''Retrieves title and date from session page.'''
    title, date = soup.find(id='conteudo').h3.text.split('-')
    date = date.replace('/', '-')
    return title.strip(), date.strip()


def find_attendance_table(soup: BeautifulSoup) -> Tag:
    return soup.find(id='conteudo').table
