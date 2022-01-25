import requests
from bs4 import BeautifulSoup

searchWord = input("O que voce quer pesquisar no Mercado Livre: ")

response = requests.get('https://lista.mercadolivre.com.br/'+ searchWord)

site = BeautifulSoup(response.text, 'html.parser')

listaDeProdutos = site.find('section', attrs={'class':'ui-search-results ui-search-results--without-disclaimer'})

produtos = listaDeProdutos.findAll('li', attrs={'class':'ui-search-layout__item'})


for i in produtos:
    print('#####################')
    prodName = i.find('h2', attrs={'class', 'ui-search-item__title'})
    prodPrice = i.find('span', attrs={'class', 'price-tag-fraction'})
    print(prodName.text)
    print(prodPrice.text + "Reais")
    print('#####################')
 
'''
#####################
Multilaser Flip Vita Dual SIM 32 MB azul 32 MB RAM
168
#####################
#####################
Xiaomi Poco M3 Dual SIM 128 GB power black 4 GB RAM
1.200
#####################
#####################
LG K61 Dual SIM 128 GB branco 4 GB RAM
1.226
#####################
#####################
Xiaomi Poco M3 Dual SIM 64 GB power black 4 GB RAM
1.119
#####################
'''