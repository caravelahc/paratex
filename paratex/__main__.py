import requests
from bs4 import BeautifulSoup


def main():
    URL = 'http://transparencia.alesc.sc.gov.br/presenca_plenaria_detalhes.php?id=1783'
    html = load_html(URL)
    parse(html)


def load_html(url: str) -> str:
    return requests.get(url).text


def parse(html: str):
    soup = BeautifulSoup(html, 'html.parser')

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
    pass


if __name__ == '__main__':
    main()
