import pandas as pd
import requests

from .extractor import extract_attendance


def main():
    URL = 'http://transparencia.alesc.sc.gov.br/presenca_plenaria_detalhes.php?id=1783'
    html = load_html(URL)
    session, attendance = extract_attendance(html)
    visualizing_results(
        (name, presence, justification, '19-09-2019')
        for name, (presence, justification) in attendance.items()
    )


def load_html(url: str) -> str:
    return requests.get(url).text


# Intended to be used later on the code
# will leave this here for utility purposes for now
def visualizing_results(observations):
    df = pd.DataFrame(observations)
    df = df.rename(
        {0: 'Nome', 1: 'Presenca', 2: 'Justificativa', 3: 'Data'},
        axis=1
    )
    print(df.tail())


if __name__ == '__main__':
    main()
