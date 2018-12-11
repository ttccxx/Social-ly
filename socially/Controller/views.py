import DataController.views as DC
import CalendarController.views as CC
from DataController.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def login(request):
    # dic = request.GET
    user_list = User.objects.all()
    last_user = user_list[user_list.count() - 1]
    session_key = last_user.get_session_key() + 1
    DC.create_user(session_key)
    return JsonResponse({"sessionKey": session_key})


def create_calendar(request):
    dic = request.GET
    check = DC.check_conflict(dic['sessionKey'], dic['date'], dic['time'])
    if check == 'ok':
        return JsonResponse({"state": "success", "eventKey": CC.create(dic)})
    return JsonResponse({"state": "fail", "eventKey": check})


def edit_calendar(request):
    dic = request.GET
    check = DC.check_conflict(dic['sessionKey'], dic['date'], dic['time'])
    if check == 'ok':
        return JsonResponse({"state": "success", "eventKey": CC.create(dic)})
    return JsonResponse({"state": "fail", "eventKey": check})


def delete_calendar(request):
    dic = request.GET
    CC.delete(dic)
    return JsonResponse({})


def get_calendar(request):
    dic = request.GET
    return JsonResponse(CC.get(dic))
