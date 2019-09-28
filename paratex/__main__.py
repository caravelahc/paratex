import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup
from datetime import date
import calendar


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
    URL = baseURL + "presenca_plenaria_detalhes.php?id=1783"
    html = load_html(URL)
    one_day_presences = parse(html)
    visualizing_results(one_day_presences)
    
    month_URL_list = get_month_sessions()
    for monthURL in month_URL_list:
        print(baseURL + monthURL)


def load_html(url: str) -> str:
    return requests.get(url).text


def parse(html: str):
    soup = BeautifulSoup(html, "html.parser")

    aux = soup.find_all("tr")
    entries = [i for i in aux if i.find("img") is None]
    observations = [build_one_observation(entry, "20-10-2010") for entry in entries]

    return observations


def build_one_observation(tr: bs4.element.Tag, date: str) -> (str, str, str, str):
    # (Name, Presence, Justification, Date)
    td = tr.findAll("td")
    name = td[0].text

    aux = td[1]
    if aux.find("a") is None:
        presence = aux.text.replace(" ", "").strip()
        justification = "x"
    else:
        presence = aux.find("a").text.strip()
        justification = aux.find("div").text.strip()

    return (name, presence, justification, date)


# Intended to be used later on the code
# will leave this here for utility purposes for now
def visualizing_results(observations):
    df = pd.DataFrame(observations)
    df = df.rename({0: "Nome", 1: "Presenca", 2: "Justificativa", 3: "Data"}, axis=1)
    print(df.tail())


if __name__ == "__main__":
    main()
