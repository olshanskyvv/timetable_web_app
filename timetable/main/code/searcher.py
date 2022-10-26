from bs4 import BeautifulSoup as bs
import requests

from . import exceptions

MAIN_URL = "https://rut-miit.ru"
URL_TEMPLATE = "https://rut-miit.ru/timetable"
group = "УИС-212"


def find_group_url(group_number: str):
    request = requests.get(URL_TEMPLATE)
    if request.status_code != 200:
        raise exceptions.ConnectionFault('Не удалось выполнить запрос на сайт с расписанием. Повторите позже.')
    main_soup = bs(request.text, 'html.parser')
    groups_tables = main_soup.find_all('a')
    needed_table_url = ''
    for ref in groups_tables:
        if group_number.upper() in ref.text:
            needed_table_url = MAIN_URL + ref['href']
            break
    if needed_table_url == MAIN_URL + '/':
        raise exceptions.GroupNotFound('Не удалось найти группу. Проверьте корректность записи.')
    return needed_table_url
