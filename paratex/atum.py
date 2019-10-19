'''rodem essa bodega com
"python -i atum.py" ou
dai da pra ir rodando novos comandos no terminal
e ir vendo como o selenium responde, eh bem top

instalando geckodriver
https://askubuntu.com/questions/851401/where-to-find-geckodriver-needed-by-selenium-python-package
'''
from selenium import webdriver


class Atum:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://transparencia.alesc.sc.gov.br/presenca_plenaria.php'

        # formas de colocar as coisas que a gente quer de verdade
        # assim que a gente descobrir como elas se parecem
        # self.search_bar = 'lst-ib'  # id
        # self.btn_search = 'btnK'  # name
        # self.btn_lucky = 'btnI'  # name

    def navigate(self):
        self.driver.get(self.url)


if __name__ == '__main__':
    ff = webdriver.Firefox()
    atum = Atum(ff)
    atum.navigate()
