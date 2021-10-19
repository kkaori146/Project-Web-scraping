from bs4 import BeautifulSoup
import requests

url='http://www.abimad.com.br/associados/pesquisar/id_produto=/uf=#menu-top'
r=requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

print(soup.find('figure').h5.text)
print(soup.find('figure').find('i', class_='fa-link').next_element.next_element.text)
