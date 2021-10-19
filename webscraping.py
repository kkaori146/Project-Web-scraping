from bs4 import BeautifulSoup
import requests

url='http://www.abimad.com.br/associados/pesquisar/id_produto=/uf=#menu-top'
r=requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

soup.find('figure')