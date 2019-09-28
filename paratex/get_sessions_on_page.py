import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup

def load_html(url: str) -> str:
    return requests.get(url).text

URL = 'http://transparencia.alesc.sc.gov.br/presenca_plenaria.php'
html = load_html(URL)

soup = BeautifulSoup(html, 'html.parser')

oi = soup.find('table', {'summary': "Presença dos Deputados"})

ola = oi.findAll('tr', {'style': "text-align: center;"})

date_href_tuples = []
for tr in ola:
    tds = tr.findAll('td')
    date = tds[2].text
    href = tds[3].find('a').attrs['href']
    date_href_tuples.append((date, href))

print(date_href_tuples)