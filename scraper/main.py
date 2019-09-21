import requests
from bs4 import BeautifulSoup

r = requests.get('http://transparencia.alesc.sc.gov.br/presenca_plenaria_detalhes.php?id=1783')
soup = BeautifulSoup(r.text, 'html.parser')

# all presences are on a tr tag
aux = soup.find_all('tr')

# other positions are intended values
# these ones, however, are bugs
some_image = aux[0]
header = aux[1]

# we seem to have 2 options:
# 1- find a better way to prevent these from entering
#     aux, in the find_all operation
# 2- removing bugs after creating the list

# after beating my head onto rocks for4 hour straight if found this:
correct_entries = [i for i in aux if i.find('img') == None]

# it works because the incorrect stuff have images
# enjoy