from django.shortcuts import render

import DataController.views as DC

# Create your views here.

def createUser(dic):
    DC.createUser(dic['id'])

def create(dic):
    DC.createCalendar(dic, type = 1)

def edit(dic):
    original_dic = dic['original']
    new_dic = dic['new']
    DC.editCalendar(original_dic, new_dic)

def delete(dic):
    DC.deleteCalendar(dic)

# developing...
def get(dic):
    calendar = DC.getCalendar(dic)
    return calendar