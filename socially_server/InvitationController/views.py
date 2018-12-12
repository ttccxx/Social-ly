from copy import deepcopy

import DataController.views as DC
import CalendarController.views as CC

def create(dic):
    event_key = DC.get_event_key(dic['inviter'])
    dic['eventKey'] = event_key
    DC.create_invitation(dic)

    # create calendar
    dic['sessionKey'] = dic['inviter']
    dic['type'] = 2
    CC.create(dic, type=2)
    return event_key

def accept(dic):
    # modify inviter's invitation
    DC.edit_invitation(dic)

    # create calendar for invitee
    event_key = DC.get_event_key(dic['invitee'])
    dic['eventKey'] = event_key
    dic['sessionKey'] = dic['invitee']
    dic['type'] = 2
    CC.create(dic, type=2)
    return event_key

def edit(dic):
    DC.edit_invitation(dic)

    # edit calendar
    dic['sessionKey'] = dic['inviter']
    CC.edit(dic)
    return dic['eventKey']

def delete(dic):
    DC.delete_invitation(dic)

    # delete calendar
    dic['sessionKey'] = dic['inviter']
    DC.delete_calendar(dic)

# developing...
def get(dic):
    pass
