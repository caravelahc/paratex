'''Attendance extractor module.'''
from bs4 import BeautifulSoup


def extract_attendance(html: str):
    soup = BeautifulSoup(html, 'html.parser')

    session_title = find_title(soup)
    att_table = find_attendance_table(soup)

    attendance = {}

    for parliamentary, state in iter_rows(att_table):
        print(f'{parliamentary}: {state}')

    return session_title, attendance


def parse(html: str):
    # all presences are on a tr tag
    aux = soup.find_all('tr')

    # we seem to have 2 options:
    # 1- find a better way to prevent these from entering
    #     aux, in the find_all operation
    # 2- removing bugs after creating the list

    # after beating my head onto rocks for 4 hour straight if found this:
    correct_entries = [i for i in aux if i.find('img') is None]

    # it works because the incorrect stuff have images
    # enjoy

    correct_entries  # Just to avoid unused warning - WIP
