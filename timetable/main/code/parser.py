import re
import requests
from bs4 import BeautifulSoup as bs


def parse_info(info: list):
    for i in range(len(info)):
        info[i] = re.sub(r'\s+', ' ', info[i].text).strip()
    return info


def parse_course(course: list):
    course = {
        'type': re.sub(r'\s+', ' ', course[1].text).strip(),
        'name': re.sub(r'\s+', ' ', course[2].text).strip(),
        'other_info': parse_info(course[3].contents[1::2])
    }
    return course


def parse_lesson(lesson: list):
    lesson = {
        'pair': re.sub(r'\s+', ' ', lesson[1].text).strip().split(','),
        'course': parse_course(lesson[3].contents)
    }
    lesson['pair'] = {
        'number': lesson['pair'][0],
        'time': lesson['pair'][1].strip()
    }
    return lesson


def parse_table(table: list):
    for i in range(len(table)):
        table[i] = parse_lesson(table[i].contents)
    return table


def parse_day(day: list):
    day = {
        'day': day[1].text.strip('\r\n ').split()[0],
        'table': parse_table(day[3].contents[1::2])
    }
    return day


def parse_timetable(timetable: list):  # list of two weeks
    for i in range(2):
        timetable[i] = [tag.contents for tag in timetable[i].contents[1::2]]
        for j in range(len(timetable[i])):
            timetable[i][j] = parse_day(timetable[i][j])
    return timetable


def parse(table_url: str):
    request = requests.get(table_url)
    table_soup = bs(request.text, 'html.parser')
    weeks_set = table_soup.find_all('div', class_='timetable__grid_md')
    two_weeks = [weeks_set[0], weeks_set[1]]
    return parse_timetable(two_weeks)
