from copy import deepcopy

from django.shortcuts import render
import DataController.views as DC
import CalendarController.views as CC

# Create your views here.
def create(dic):
    DC.createInvitation(dic, invitation_type=1)

    # create calendar
    DC.createCalendar(dic, type=2)

def accept(dic):
    # modify inviter's invitation
    inviter_dic = deepcopy(dic)
    dic['inviter_id'] = 123
    inviter_dic['id'] = dic['inviter_id']
    inviter_dic['invitee_id'] = dic['id']
    DC.editInvitation(inviter_dic, inviter_dic)

    # create invitation for invitee
    DC.createInvitation(dic, invitation_type=2)
    # create calendar for invitee
    DC.createCalendar(dic, type=2)

def edit(dic):
    # get original_dic and new_dic
    original_dic = dic['original']
    new_dic = dic['new']
    DC.editInvitation(original_dic, new_dic)

    # edit calendar
    DC.editCalendar(original_dic, new_dic)

def delete(dic):
    DC.deleteInvitation(dic)
    DC.deleteCalendar(dic)

# developing...
def get(dic):
    pass