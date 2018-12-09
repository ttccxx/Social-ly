from django.shortcuts import render
from .models import User, Calendar

# Create your views here.

#sort calendar

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


def checkConflict(id, date, time):
    user = User.objects.filter(id = id)[0]
    calendar = Calendar.objects.filter(user_id = user, date = date, time = time)
    if calendar.count() != 0:
        return False
    return True

# test
def checkUserConflict(id):
    calendar = Calendar.objects.filter(id = id)
    if calendar.count() != 0:
        return False
    return True

def createUser(id, image = None):
    user = User()
    user.id = id
    user.image = image
    user.save()

def createCalendar(id, date, time, info):
    calendar = Calendar()
    user = User.objects.filter(id = id)[0]
    calendar.user_id = user
    calendar.date = date
    calendar.time = time
    calendar.info = info
    calendar.save()

def editCalendar(id, date, time, info):
    user = User.objects.filter(id=id)[0]
    calendar = Calendar.objects.filter(user_id = user, date = date, time = time)
    calendar.user_id = user
    calendar.date = date
    calendar.time = time
    calendar.info = info
    calendar.save()

def deleteCalendar(id, date, time):
    user = User.objects.filter(id = id)[0]
    Calendar.objects.filter(user_id = user, date = date, time = time).delete()

def getCalendar(id):
    user = User.objects.filter(id=id)[0]
    return Calendar.objects.filter(user_id = user)








