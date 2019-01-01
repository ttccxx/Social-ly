from .models import User, Calendar, Invitation


def check_conflict(session_key, date, time):
    user = User.objects.filter(session_key=session_key)[0]
    calendar = Calendar.objects.filter(user=user, date=date, time=time)
    if calendar.count() != 0:
        return {'eventKey': calendar[0].get_key_str(), 'type': calendar[0].get_type_str()}
    return "ok"

def check_edit_conflict(session_key, event_key, date, time):
    user = User.objects.filter(session_key=session_key)[0]
    calendar = Calendar.objects.filter(user=user, date=date, time=time)
    if (calendar.count() == 1 and calendar[0].event_key == event_key) or calendar.count() == 0:
        return "ok"
    return calendar[0].get_key_str()


def check_user(session_key):
    user = User.objects.filter(session_key=session_key)
    if user.count() != 0:
        return True
    return False

def create_user(session_key):
    user = User.objects.filter(session_key=session_key)
    if user.count() != 0:
        return;
    user = User()
    user.session_key = session_key
    user.save()

def get_event_key(session_key):
    user = User.objects.filter(session_key=session_key)[0]
    event_key = user.new_event()
    user.save()
    return event_key

def set_name(dic):
    user = User.objects.filter(session_key=dic['sessionKey'])[0]
    user.name = dic['name']
    user.save()

"""
    below is the database interface for Calendar
"""
def create_calendar(dic):
    calendar = Calendar()
    user = User.objects.filter(session_key=dic['sessionKey'])[0]
    calendar.user = user
    calendar.event_key = dic['eventKey']
    calendar.date = dic['date']
    calendar.time = dic['time']
    calendar.thing = dic['thing']
    calendar.place = dic['place']
    calendar.type = dic['type']
    calendar.save()
    return calendar.get_key_str()


def edit_calendar(dic):
    user = User.objects.filter(session_key=dic['sessionKey'])[0]
    calendar = Calendar.objects.filter(event_key=dic['eventKey'])[0]
    calendar.user_id = user
    calendar.date = dic['date']
    calendar.time = dic['time']
    calendar.thing = dic['thing']
    calendar.place = dic['place']
    calendar.save()


def delete_calendar(dic):
    user = User.objects.filter(session_key=dic['sessionKey'])[0]
    Calendar.objects.filter(user=user, event_key=dic['eventKey']).delete()


def get_calendar(dic):
    user = User.objects.filter(session_key=dic['sessionKey'])[0]
    dic = {}
    for calendar in Calendar.objects.filter(user=user):
        date = calendar.get_date_str()
        if date not in dic:
            dic[date] = []
        dic[date].append(calendar.json_dic())
    return dic

"""
    below is the database interface for Invitation
"""
def create_invitation(dic):
    inviter = User.objects.filter(session_key = dic['inviter'])[0]
    if 'invitee_id' in dic.keys():
        invitee = User.objects.filter(session_key = dic['invitee'])[0]
    else:
        invitee = None
    invitation = Invitation()
    invitation.inviter = inviter
    invitation.event_key = dic['eventKey']
    invitation.date = dic['date']
    invitation.time = dic['time']
    invitation.thing = dic['thing']
    invitation.place = dic['place']
    invitation.invitee = invitee
    inviter.save()
    invitation.save()
    return invitation.get_key_str()

def edit_invitation(dic):
    inviter = User.objects.filter(session_key=dic['inviter'])[0]
    if 'invitee' in dic.keys():
        invitee = User.objects.filter(session_key=dic['invitee'])[0]
    else:
        invitee = None
    invitation = Invitation.objects.filter(inviter = inviter, date = dic['date'], time = dic['time'])[0]
    invitation.date = dic['date']
    invitation.time = dic['time']
    invitation.thing = dic['thing']
    invitation.place = dic['place']
    invitation.invitee = invitee
    invitation.save()

def delete_invitation(dic):
    inviter = User.objects.filter(session_key = dic['sessionKey'])[0]
    Invitation.objects.filter(inviter = inviter, event_key = dic['eventKey']).delete()

def get_invitations(dic, type):
    user = User.objects.filter(session_key=dic['sessionKey'])[0]
    dic = {}
    if type == 'inviter':
        for invitation in Invitation.objects.filter(inviter=user).order_by('time'):
          date = invitation.get_date_str()
          if date not in dic.keys():
              dic[date] = []
          dic[date].append(invitation.json_dic())
    else:
        for invitation in Invitation.objects.filter(invitee=user).order_by('time'):
          date = invitation.get_date_str()
          if date not in dic.keys():
              dic[date] = []
          dic[date].append(invitation.json_dic())

    return dic

def get_single_invitation(dic):
    inviter = User.objects.filter(session_key = dic['inviterID'])[0]
    invitation = Invitation.objects.filter(inviter=inviter, date = dic['date'], time = dic['time'])[0]
    return invitation.json_dic()
