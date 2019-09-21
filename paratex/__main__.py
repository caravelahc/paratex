import requests


def main():
    URL = 'http://transparencia.alesc.sc.gov.br/presenca_plenaria_detalhes.php?id=1783'
    load_html(URL)


def load_html(url: str) -> str:
    return requests.get(url).text


if __name__ == '__main__':
    main()
