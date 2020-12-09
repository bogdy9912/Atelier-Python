
def filter_rows_td(row_td):

    row_td_class = row_td.get('class') or []
    row_td_classes_set = set(row_td_class)
    # print(row_td_class)

    custom_classes = {'poz', 'echipa', 'punct'}
    set_intersection = row_td_classes_set.intersection(custom_classes)
    has_my_class = len(set_intersection) > 0

    # is_position_td = 'poz' in row_td_class
    # is_team_td = 'echipa' in row_td_class

    has_image = row_td.find('img') is not None
    is_without_class = len(row_td_class) == 0
    return has_my_class or has_image or is_without_class


def map_team_data(team_data):
    if team_data.text != '':
        return team_data.text

    return team_data.find('img').get('data-src')

def get_team_from_table(html_row):
    # print('html_row: ', html_row)
    rows_tds = html_row.findAll('td')
    # print(rows_tds[0])

    rows_tdsr = list(filter(filter_rows_td, rows_tds))
    # print(rows_tdsr[0].text)
    team_data = list(map(map_team_data, rows_tdsr))

    print(team_data)
    return team_data
