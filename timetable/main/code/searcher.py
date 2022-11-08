import re

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
    url = main_soup.find('a', text=re.compile(group_number.upper()))
    if url:
        return MAIN_URL + url['href']
    else:
        raise exceptions.GroupNotFound('Не удалось найти группу. Проверьте корректность записи.')
