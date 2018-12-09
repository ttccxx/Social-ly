from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

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
    '''
        operations for calendar
    '''
    if type == 'CreateCalendar':
        if not DC.checkConflict(dic['id'], dic['date'], dic['time']):
            return HttpResponse('False')
        CC.create(dic)
    if type == 'EditCalendar':
        if not DC.checkConflict(dic['new']['id'], dic['new']['date'], dic['new']['time']):
            return False
        CC.edit(dic)
    if type == 'DeleteCalendar':
        CC.delete(dic)
    if type == 'GetCalendar':
        dic = CC.get(dic)
        return JsonResponse(dic)
    '''
        operations for invitation
    '''
    if type == 'CreateInvitation':
        if not DC.checkConflict(dic['id'], dic['date'], dic['time']):
            return False
        IC.create(dic)
    if type == 'AcceptInvitation':
        if not DC.checkConflict(dic['id'], dic['date'], dic['time']):
            return False
        IC.accept(dic)
    if type == 'EditInvitation':
        if not DC.checkConflict(dic['new']['id'], dic['new']['date'], dic['new']['time']):
            return False
        IC.edit(dic)
    if type == 'GetInvitation':
        dic = IC.get(dic)
        return dic
    if type == 'DeleteInvitation':
        IC.delete(dic)

    return JsonResponse(dic)