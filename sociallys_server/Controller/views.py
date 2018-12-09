from django.shortcuts import render
import DataController.views as DC
import CalendarController.views as CC
import InvitationController.views as IC

# Create your views here.
def controller(request, dic, type):
    dic = eval(dic)
    if type == 'CreateUser':
        if not DC.checkUserConflict(dic['id']):
            return False
        CC.createUser(dic)
    if type == 'CreateCalendar':
        if not DC.checkConflict(dic['id'], dic['date'], dic['time']):
            return False
        CC.create(dic)
    if type == 'EditCalendar':
        CC.edit(dic)
    if type == 'DeleteCalendar':
        CC.delete(dic)
    if type == 'GetCalendar':
        dic = CC.get(dic)
        return dic
    if type == 'CreateInvitation':
        if not DC.checkConflict(dic['id'], dic['date'], dic['time']):
            return False
        IC.create(dic)