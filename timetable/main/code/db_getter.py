from ..models import *


def get_lesson_from_db(lesson: Lesson):
    lesson_dict = {
        'pair': {
            'number': lesson.number,
            'time': lesson.time
        },
        'course': {
            'type': lesson.type,
            'name': lesson.name,
            'other_info': [str(info) for info in lesson.info_set.all()]
        }
    }
    return lesson_dict


def get_day_from_db(day: Day):
    day_dict = {
        'day': day.name,
        'table': [get_lesson_from_db(lesson) for lesson in day.lesson_set.all()]
    }
    return day_dict


def get_week_from_db(week: Week):
    days = week.day_set.all()
    week_list = [get_day_from_db(day) for day in days]
    return week_list


def get_timetable_from_db(group: str):
    table = Timetable.objects.get(group=group)
    timetable = [
        {'table': get_week_from_db(table.week1), 'number': 1},
        {'table': get_week_from_db(table.week2), 'number': 2},
    ]
    return timetable
