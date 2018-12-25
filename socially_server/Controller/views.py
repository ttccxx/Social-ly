import DataController.views as DC
import CalendarController.views as CC
import InvitationController.views as IC
from DataController.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def login(request):
    dic = request.GET
    # user_list = User.objects.all()
    # last_user = user_list[user_list.count() - 1]
    # session_key = last_user.get_session_key() + 1
    # DC.create_user(session_key)
    session_key = 123
    return JsonResponse({"sessionKey": session_key})

def check_user(request):
    dic = request.GET
    # get session_key through code
    session_key=123
    state = DC.check_user(session_key)
    DC.create_user(session_key)
    return JsonResponse({"state": state, "sessionKey": session_key})


'''
    calendar part
'''

def create_calendar(request):
    dic = request.GET
    dic = dic.copy()
    #  test code
    #  dic = {'sessionKey':123, 'date':'2018-12-12', 'time':'17:52', 'thing':'study', 'place':'lib'}
    check = DC.check_conflict(dic['sessionKey'], dic['date'], dic['time'])
    if check == 'ok':
        return JsonResponse({"state": "success", "eventKey": CC.create(dic)})
    return JsonResponse({"state": "fail", "eventKey": check})


def edit_calendar(request):
    dic = request.GET
    check = DC.check_edit_conflict(dic['sessionKey'], dic['date'], dic['time'])
    if check == 'ok':
        return JsonResponse({"state": "success", "eventKey": CC.edit(dic)})
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
    print(dic)
    # test
    # dic = {'inviter': 123, 'date': '2018-12-12', 'time': '18:31', 'thing': 'study', 'place': 'lib'}
    check = DC.check_conflict(dic['inviter'], dic['date'], dic['time'])
    print(check)
    if check == 'ok':
        return JsonResponse({"state": "success", "eventKey": IC.create(dic)})
    return JsonResponse({"state": "fail", "eventKey": check})


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
    check = DC.check_conflict(dic['invitee'], dic['date'], dic['time'])
    # dic = {'inviter': 123, 'date': '2018-12-12', 'time': '18:31', 'thing': 'study', 'place': 'lib', 'eventKey': 5, 'invitee': 456}
    if check == 'ok':
        return JsonResponse({"state": "success", "eventKey": IC.accept(dic)})
    else:
        return JsonResponse({"state": "fail", "eventKey": check})

# developing...
def get_inviter_invitations(request):
    dic = request.GET
    return JsonResponse(IC.get_inviter(dic))

def get_single_invitation(request):
    dic = request.GET
    return JsonResponse(IC.get_single_invitation(dic))

def get_invitee_invitations(request):
    dic = request.GET
    return JsonResponse(IC.get_invitee(dic))