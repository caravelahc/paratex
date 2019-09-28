from selenium import webdriver

# rodem essa bodega com 
# "python -i atum.py" ou
# "ipython -i atum.py"
# dai da pra ir rodando novos comandos no terminal
# e ir vendo como o selenium responde, eh bem top

class Atum:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://transparencia.alesc.sc.gov.br/presenca_plenaria.php'
        # self.search_bar = 'lst-ib'  # id
        # self.btn_search = 'btnK'  # name
        # self.btn_lucky = 'btnI'  # name

    def navigate(self):
        self.driver.get(self.url)

ff = webdriver.Firefox()
atum = Atum(ff)
atum.navigate()

