import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup

def main():
    URL = 'http://transparencia.alesc.sc.gov.br/presenca_plenaria_detalhes.php?id=1783'
    html = load_html(URL)
    one_day_presences = parse(html)
    visualizing_results(one_day_presences)


def load_html(url: str) -> str:
    return requests.get(url).text


def parse(html: str):
    soup = BeautifulSoup(html, 'html.parser')

    aux = soup.find_all('tr')
    entries = [i for i in aux if i.find('img') is None]
    observations = [build_one_observation(entry, '20-10-2010') for entry in entries]
    
    return observations

def build_one_observation(tr: bs4.element.Tag, date:str) -> (str, str, str, str):
    # (Name, Presence, Justification, Date)
    td = tr.findAll('td') 
    name = td[0].text
    
    aux =  td[1]
    if aux.find('a') == None:
        presence = aux.text.replace(" ", "").strip()
        justification = 'x'
    else:
        presence = aux.find('a').text.strip()
        justification = aux.find('div').text.strip()
        
    return (name, presence, justification, date)


# Intended to be used later on the code
# will leave this here for utility purposes for now
def visualizing_results(observations):
    df = pd.DataFrame(observations)
    df = df.rename({0:'Nome', 1:'Presenca', 2:'Justificativa', 3:'Data'}, axis=1)
    print(df.tail())


if __name__ == '__main__':
    main()
