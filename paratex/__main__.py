from datetime import date
import calendar

import pandas as pd

from .extractor import extract_attendance, Session


def add_month(sourcedate):
    month = sourcedate.month
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


def get_month_sessions() -> list:
    dt = date(2011, 4, 1)
    URL = []
    while dt < date.today():
        dt = add_month(dt)
        URL.append(f"presenca_plenaria.php?periodo={dt.month:02}-{dt.year}")
    return URL


def main():
    baseURL = "http://transparencia.alesc.sc.gov.br/"

    month_URL_list = get_month_sessions()
    for monthURL in month_URL_list:
        print(baseURL + monthURL)

def main():
    session = extract_attendance(1783)
    print(session.title)
    print(as_dataframe(session).head())


# Intended to be used later on the code. Will leave this here for utility
# purposes for now.
def as_dataframe(session: Session):
    observations = (
        (name, presence, justification, session.date)
        for name, (presence, justification) in session.attendance.items()
    )
    df = pd.DataFrame(observations)
    df = df.rename(
        {0: 'Nome', 1: 'Presenca', 2: 'Justificativa', 3: 'Data'},
        axis=1
    )
    return df


if __name__ == "__main__":
    main()
