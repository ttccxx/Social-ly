from django.shortcuts import render

import DataController.views as DC

# Create your views here.

def createUser(dic):
    DC.createUser(dic['id'])

def create(dic):
    DC.createCalendar(dic['id'], dic['date'], dic['time'], dic['info'])

def edit(dic):
    DC.editCalendar(dic['id'], dic['date'], dic['time'], dic['info'])

def delete(dic):
    DC.deleteCalendar(dic['id'], dic['date'], dic['time'])

def get(dic):
    calendar = DC.getCalendar(dic['id'])
    return calendar