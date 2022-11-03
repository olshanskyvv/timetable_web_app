from .db_filler import add_timetable_to_db
from .db_getter import get_timetable_from_db
from .parser import parse
from .searcher import find_group_url
from ..models import *


def get_timetable(user: User):
    group = user.group
    timetable = Timetable.objects.filter(group=group)
    if timetable:
        return get_timetable_from_db(group)
    else:
        timetable = parse(find_group_url(group))
        add_timetable_to_db(timetable, group)
        return timetable
