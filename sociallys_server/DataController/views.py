import datetime as dt

from django.shortcuts import render
from .models import User, Calendar, Invitation

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


"""
    below is the database interface for Calendar
"""
def createCalendar(dic, type):
    calendar = Calendar()
    user = User.objects.filter(id = dic['id'])[0]
    calendar.user_id = user
    calendar.date = dic['date']
    calendar.time = dic['time']
    calendar.info = dic['info']
    calendar.type = type
    calendar.save()

def editCalendar(original_dic, new_dic):
    user = User.objects.filter(id=original_dic['id'])[0]
    calendar = Calendar.objects.filter(user_id = user, date = original_dic['date'], time = original_dic['time'])
    calendar.user_id = user
    calendar.date = new_dic['date']
    calendar.time = new_dic['time']
    calendar.info = new_dic['info']
    calendar.save()

def deleteCalendar(dic):
    user = User.objects.filter(id = dic['id'])[0]
    Calendar.objects.filter(user_id = user, date = dic['date'], time = dic['time']).delete()

def getCalendar(dic):
    user = User.objects.filter(id=dic['id'])[0]
    calendar = {}
    for event in Calendar.objects.filter(user_id = user):
        calendar[str(event.date) +' '+ str(event.time)] = event.info

    return calendar


"""
    below is the database interface for Invitation
"""
def createInvitation(dic, invitation_type):
    user = User.objects.filter(id = dic['id'])[0]
    if 'inviter_id' in dic.keys():
        invitee = User.objects.filter(id = dic['inviter_id'])[0]
    else:
        invitee = None
    invitation = Invitation()
    invitation.user_id = user
    invitation.date = dic['date']
    invitation.time = dic['time']
    invitation.info = dic['info']
    invitation.invitee = invitee
    invitation.type = invitation_type
    invitation.save()

def editInvitation(original_dic, dic):
    user = User.objects.filter(id=original_dic['id'])[0]
    invitation = Invitation.objects.filter(user_id = user, date = original_dic['date'], time = original_dic['time'])[0]
    invitation.date = dic['date']
    invitation.time = dic['time']
    invitation.info = dic['info']

    invitee = User.objects.filter(id = dic['invitee_id'])[0]
    invitation.invitee = invitee

    invitation.save()

def deleteInvitation(dic):
    user = User.objects.filter(id = dic['id'])[0]
    Invitation.objects.filter(user_id = user, date = dic['date'], time = dic['time']).delete()





