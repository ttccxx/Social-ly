from .models import User, Calendar


def organize(calendar):
    events = {}
    for event in calendar:
        if event.date not in events.keys():
            events[event.date] = {}
            events[event.date][event.time] = event.info
        else:
            events[event.date][event.time] = event.info

    # for key in events.keys():
    #     events[key] = sort(events[key])

    return events


def check_conflict(session_key, date, time):
    user = User.objects.filter(session_key=session_key)[0]
    calendar = Calendar.objects.filter(user=user, date=date, time=time)
    if calendar.count() != 0:
        return calendar[0].get_key_str()
    return "ok"


# test
def check_user(session_key):
    calendar = Calendar.objects.filter(session_key=session_key)
    if calendar.count() != 0:
        return False
    return True


def create_user(session_key):
    user = User()
    user.session_key = session_key
    user.save()


def create_calendar(session_key, date, time, thing, place):
    calendar = Calendar()
    user = User.objects.filter(session_key=session_key)[0]
    calendar.user = user
    calendar.event_key = user.new_event()
    calendar.date = date
    calendar.time = time
    calendar.thing = thing
    calendar.place = place
    user.save()
    calendar.save()
    return calendar.get_key_str()


def edit_calendar(session_key, event_key, date, time, thing, place):
    user = User.objects.filter(session_key=session_key)[0]
    calendar = Calendar.objects.filter(event_key=event_key)[0]
    calendar.user_id = user
    calendar.date = date
    calendar.time = time
    calendar.thing = thing
    calendar.place = place
    calendar.save()


def delete_calendar(session_key, event_key):
    user = User.objects.filter(session_key=session_key)[0]
    event_key = int(event_key)
    Calendar.objects.filter(user=user, event_key=event_key).delete()


def get_calendar(session_key):
    dic = {}
    user = User.objects.filter(session_key=session_key)[0]
    for calendar in Calendar.objects.filter(user=user):
        date = calendar.get_date_str()
        if date not in dic:
            dic[date] = []
        dic[date].append(calendar.json_dic())
    return dic
