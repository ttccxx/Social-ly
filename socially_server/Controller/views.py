import DataController.views as DC
import CalendarController.views as CC
import InvitationController.views as IC
import StatController.views as SC
from DataController.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import logging

def login(request):
    dic = request.GET
    appid = 'appid'
    secret = 'secret'
    r = requests.get('https://api.weixin.qq.com/sns/jscode2session?appid='+appid+'&secret='+secret+'&js_code='+dic['code']+'&grant_type=authorization_code')

    session_key = r.json()['openid']
    DC.create_user(session_key)
    return JsonResponse({"sessionKey": r.json()['openid']})

def set_name(request):
    dic = request.GET
    DC.set_name(dic)
    return JsonResponse({"state": "ok"})

def check_user(request):
    dic = request.GET
    appid = 'appid'
    secret = 'secret'
    r = requests.get('https://api.weixin.qq.com/sns/jscode2session?appid='+appid+'&secret='+secret+'&js_code='+dic['code']+'&grant_type=authorization_code')

    session_key = r.json()['openid']
    return JsonResponse({"state": DC.check_user(session_key), "sessionKey": session_key})

'''
    calendar part
'''

def create_calendar(request):
    dic = request.GET
    #  test code
    #  dic = {'sessionKey':123, 'date':'2018-12-12', 'time':'17:52', 'thing':'study', 'place':'lib'}
    check = DC.check_conflict(dic['sessionKey'], dic['date'], dic['time'])
    if check == 'ok':
        return JsonResponse({"state": "success", "eventKey": CC.create(dic)})
    return JsonResponse({"state": "fail", "eventKey": check['eventKey']})


def edit_calendar(request):
    dic = request.GET
    check = DC.check_edit_conflict(dic['sessionKey'], dic['eventKey'], dic['date'], dic['time'])
    print(check)
    if check == 'ok':
        DC.edit_calendar(dic)
        return JsonResponse({"state": "success"})
    return JsonResponse({"state": "fail", "eventKey": check})


def delete_calendar(request):
    dic = request.GET
    CC.delete(dic)
    return JsonResponse({})


def get_calendar(request):
    dic = request.GET
    return JsonResponse(CC.get(dic))

"""
    invitation part
"""
def create_invitation(request):
    dic = request.GET
    dic = dic.copy()
    # test
    # dic = {'inviter': 123, 'date': '2018-12-12', 'time': '18:31', 'thing': 'study', 'place': 'lib'}
    check = DC.check_conflict(dic['inviter'], dic['date'], dic['time'])
    if check == 'ok':
        return JsonResponse({"state": "success", "eventKey": IC.create(dic)})
    return JsonResponse({"state": "fail", "eventKey": check['eventKey'], "type": check['type']})


def edit_invitation(request):
    dic = request.GET
    # test
    # dic = {'inviter': 123, 'date': '2018-12-12', 'time': '18:31', 'thing': 'study', 'place': 'lib', 'eventKey':5}
    check = DC.check_edit_conflict(dic['inviter'], dic['eventKey'], dic['date'], dic['time'])
    if check == 'ok':
        return JsonResponse({"state": "success", "eventKey": IC.edit(dic)})
    return JsonResponse({"state": "fail", "eventKey": check})


def delete_invitation(request):
    dic = request.GET
    IC.delete(dic)
    return JsonResponse({})

def accept_invitation(request):
    dic = request.GET
    dic = dic.copy()
    # dic = {'inviter': 123, 'date': '2018-12-12', 'time': '18:31', 'thing': 'study', 'place': 'lib', 'eventKey': 5, 'invitee': 456}
    return JsonResponse({"state": "success", "eventKey": IC.accept(dic)})

def get_inviter_invitations(request):
    dic = request.GET
    return JsonResponse(IC.get_inviter(dic))

def get_single_invitation(request):
    dic = request.GET
    return JsonResponse(IC.get_single_invitation(dic))

def get_invitee_invitations(request):
    dic = request.GET
    return JsonResponse(IC.get_invitee(dic))

'''
    statistic part
'''
def get_statistics(request):
    dic = request.GET
    statistc = SC.get_statistics(dic)
    response = dict()
    response['statistics'] = statistc
    return JsonResponse(response)

def add_statistic(request):
    dic = request.GET
    return JsonResponse({'state': SC.add_statistic(dic)})

def get_single_statistic(request):
    dic = request.GET
    return JsonResponse(SC.get_single_statistic(dic))

def add_reply(request):
    dic = request.GET
    return JsonResponse({'state': SC.add_reply(dic)})
