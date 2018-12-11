from django.urls import path
from . import views


app_name = 'Controller'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('event/addEvent', views.create_calendar, name='create_user'),
    path('user/events', views.get_calendar, name='get_calendar'),
    path('event/deleteEvent', views.delete_calendar, name='delete_calendar'),
    path('event/modifyEvent', views.edit_calendar, name='edit_calendar')
]