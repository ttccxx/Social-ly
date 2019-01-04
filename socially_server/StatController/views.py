from django.shortcuts import render
from DataController.models import User, Statistic
from DataController.views import *

import json

def get_statistics(dic):
    user = User.objects.filter(session_key = dic['sessionKey'])[0]
    eventKeys = Statistic.objects.values('eventKey').distinct()
    statistics = []
    for eventKey in eventKeys:
        choices = []
        people_num = 0
        same_statistic = Statistic.objects.filter(user=user, eventKey=eventKey['eventKey'])
        for one_statistic in same_statistic:
            choices.append(one_statistic.get_choice())
            people_num += one_statistic.number
        statistic_dic = dict()
        statistic_dic['title'] = same_statistic[0].title
        statistic_dic['thing'] = same_statistic[0].thing
        statistic_dic['deadDate'] = same_statistic[0].deadDate
        statistic_dic['deadTime'] = same_statistic[0].deadTime
        statistic_dic['people'] = people_num
        statistic_dic['place'] = same_statistic[0].place
        statistic_dic['eventKey'] = same_statistic[0].eventKey
        statistic_dic['choices'] = choices
        statistics.append(statistic_dic)
    return statistics

def add_statistic(dic):
    user = User.objects.filter(session_key=dic['sessionKey'])[0]
    eventKey = get_event_key(dic['sessionKey'])
    choices = json.loads(dic['choices'])
    for choice in choices:
        statistic = Statistic()
        statistic.user = user
        statistic.eventKey = eventKey
        statistic.title = dic['title']
        statistic.thing = dic['thing']
        statistic.place = dic['place']
        statistic.deadDate = dic['deadDate']
        statistic.deadTime = dic['deadTime']
        statistic.date = choices[choice]['date']
        statistic.time = choices[choice]['time']
        statistic.number = choices[choice]['number']
        statistic.save()
    return 'success'

def get_single_statistic(dic):
    user = User.objects.filter(session_key=dic['statID'])[0]
    statistic = dict()
    choices = []
    people_num = 0
    same_statistic = Statistic.objects.filter(user=user, eventKey=dic['eventKey'])
    for one_statistic in same_statistic:
        choices.append(one_statistic.get_choice())
        people_num += one_statistic.number
    statistic['title'] = same_statistic[0].title
    statistic['thing'] = same_statistic[0].thing
    statistic['deadDate'] = same_statistic[0].deadDate
    statistic['deadTime'] = same_statistic[0].deadTime
    statistic['people'] = people_num
    statistic['place'] = same_statistic[0].place
    statistic['eventKey'] = same_statistic[0].eventKey
    statistic['choices'] = choices
    return statistic

def add_reply(dic):
    user = User.objects.filter(session_key=dic['sessionKey'])[0]
    reply = json.loads(dic['reply'])
    for answer in reply:
        if reply[answer] == True:
            statistic = Statistic.objects.filter(user=user, eventKey=dic['eventKey'], rank=answer)[0]
            statistic.number += 1
            statistic.save()
    return 'success'