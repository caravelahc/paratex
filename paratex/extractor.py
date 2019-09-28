'''Attendance extractor module.'''
from dataclasses import dataclass
from typing import Dict, Optional, Tuple

from bs4 import BeautifulSoup
from bs4.element import Tag
import requests


@dataclass
class Session:
    title: str
    date: str
    attendance: Dict[str, Tuple[str, Optional[str]]]


def url_from_id(session_id: int):
    BASE_URL = (
        'http://transparencia.alesc.sc.gov.br/'
        'presenca_plenaria_detalhes.php'
    )
    return f'{BASE_URL}?id={session_id}'


def load_html(url: str) -> str:
    return requests.get(url).text


def extract_attendance(session_id: int) -> Tuple[str, Dict[str, str]]:
    '''Extracts every parliamentary's attendance in a given ALESC's meeting
    attendance HTML page.'''
    html = load_html(url_from_id(session_id))
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


def find_session_header(soup: BeautifulSoup) -> Tuple[str, str]:
    '''Retrieves title and date from session page.'''
    title, date = soup.find(id='conteudo').h3.text.split('-')
    date = date.replace('/', '-')
    return title.strip(), date.strip()


def find_attendance_table(soup: BeautifulSoup) -> Tag:
    return soup.find(id='conteudo').table


def iter_rows(table: Tag):
    '''Iter through a table's rows.'''
    trs = table.find_all('tr')
    for tr in trs:
        yield tr.find_all('td')
