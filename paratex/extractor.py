'''Attendance extractor module.'''
from typing import Dict, Tuple
from bs4 import BeautifulSoup
from bs4.element import Tag


def extract_attendance(html: str) -> Tuple[str, Dict[str, str]]:
    '''Extracts every parliamentary's attendance in a given ALESC's meeting
    attendance HTML page.'''
    soup = BeautifulSoup(html, 'html.parser')

    session_title = find_session_title(soup)
    att_table = find_attendance_table(soup)

    attendance = {}

    for parliamentary, state in iter_rows(att_table):
        attendance[parliamentary] = state

    return session_title, attendance


def find_session_title(soup: BeautifulSoup) -> str:
    return soup.find(id='conteudo').h3.text


def find_attendance_table(soup: BeautifulSoup) -> Tag:
    return soup.find(id='conteudo').table


def iter_rows(table: Tag):
    '''Iter through a table's rows.'''
    trs = table.find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        yield (td.text.strip() for td in tds)
