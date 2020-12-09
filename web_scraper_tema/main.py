import requests
from bs4 import BeautifulSoup

URL = 'http://frsah.ro/'

page = requests.get(url=URL)
page_content_html = BeautifulSoup(page.content, features='html.parser')

lista = page_content_html.find('div', {'class' : 'td-ss-main-content td_block_template_1'})
lista_title_html = lista.find_all('h3', {'class': 'entry-title td-module-title'})

title_list = []
for i in lista_title_html:
    paragraf =i.find('a')
    print(paragraf)
    title = paragraf.get('title') or ''
    print(title)
    title_list.append(title)

with open('output.txt', 'w', encoding='utf-8') as file:
    for elem in title_list:
        file.write(elem+'\n')

