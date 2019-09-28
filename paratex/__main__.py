import pandas as pd
import requests

from .extractor import extract_attendance, Session


def main():
    URL = 'http://transparencia.alesc.sc.gov.br/presenca_plenaria_detalhes.php?id=1783'
    html = load_html(URL)
    session = extract_attendance(html)
    print(session.title)
    print(as_dataframe(session).head())


def load_html(url: str) -> str:
    return requests.get(url).text


# Intended to be used later on the code
# will leave this here for utility purposes for now
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


if __name__ == '__main__':
    main()
