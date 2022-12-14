from ..models import *


def create_info_db(info: str, lesson: Lesson):
    info_db = Info(
        lesson=lesson,
        content=info
    )
    info_db.save()


def create_lesson_db(lesson: dict, day: Day):
    lesson_db = Lesson(
        day=day,
        number=lesson['pair']['number'],
        time=lesson['pair']['time'],
        type=lesson['course']['type'],
        name=lesson['course']['name']
    )
    lesson_db.save()
    for info in lesson['course']['other_info']:
        create_info_db(info, lesson_db)


def create_day_db(day: dict, week: Week):
    day_db = Day(
        week=week,
        name=day['day']
    )
    day_db.save()
    for lesson in day['table']:
        create_lesson_db(lesson, day_db)


def create_week_db(week: dict, group: Group):
    week_db = Week(
        number=week['number'],
        timetable=group
    )
    week_db.save()
    for day in week['table']:
        create_day_db(day, week_db)
    return week_db


def add_timetable_to_db(timetable: list, group: str):
    timetable_db = Group(
        group=group
    )
    timetable_db.save()
    create_week_db(timetable[0], timetable_db)
    create_week_db(timetable[1], timetable_db)
    return timetable_db
