import requests
from bs4 import BeautifulSoup
from handlers.extract_data_table import get_team_from_table

URL = 'https://lpf.ro/liga-1'

page = requests.get(URL)
soup = BeautifulSoup(page.content, features='html.parser')

table = soup.find('div', {'id': 'clasament_ajax'}).find('table')

table_rows = table.find_all('tr', {'class': 'echipa_row'})
# print(len(table_rows))

# print(table_rows[0])
teams = map(get_team_from_table, table_rows)
# print('teams: ', list(teams))

for i in table_rows:
    get_team_from_table(i)
