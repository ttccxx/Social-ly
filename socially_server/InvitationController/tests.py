from django.test import TestCase
import datetime

from .views import *
from DataController.views import *
from DataController.models import *

class TestCreate(TestCase):
    def setUp(self):
        create_user(123)
        create_user(456)

    def test_create_invitation(self):
        """
        test the create function
        fail when the inviter hasn't logged in
        """
        dic = {
            'inviter': 123,
            'date': '2018-12-31',
            'time': '0:25',
            'thing': 'study',
            'place': 'lib',
        }
        self.assertEqual(create(dic), '001')
        invitation = Invitation.objects.filter(date = '2018-12-31')
        self.assertEqual(invitation[0].time, datetime.time(00, 25))
        calendar = Calendar.objects.filter(date = '2018-12-31')
        self.assertEqual(calendar[0].time, datetime.time(00, 25))

    def test_accept(self):
        """
        test accept
        expectation: corresponding invitee is added
                     calendar for that invitee is added
        """
        dic = {
            'inviter': 123,
            'date': '2018-12-31',
            'time': '0:25',
            'thing': 'study',
            'place': 'lib',
        }
        create(dic)
        dic = {
            'inviter': 123,
            'invitee': 456,
            'date': '2018-12-31',
            'time': '0:25',
            'thing': 'study',
            'place': 'lib',
        }
        self.assertEqual(accept(dic), 1)
        inviter = User.objects.filter(session_key=123)[0]
        invitation = Invitation.objects.filter(inviter = inviter, date = '2018-12-31', time = '00:25')
        self.assertEqual(invitation.count(), 1)
        invitee = User.objects.filter(session_key=456)[0]
        self.assertEqual(invitation[0].invitee, invitee)
        calendar = Calendar.objects.filter(user=invitee)
        self.assertEqual(calendar.count(), 1)
        self.assertEqual(calendar[0].date, datetime.date(2018, 12, 31))
        self.assertEqual(calendar[0].time, datetime.time(00, 25))

    def test_delete(self):
        """
        test delete
        expectation: both the calendar and invitation are null
        """
        dic = {
            'inviter': 123,
            'date': '2018-12-31',
            'time': '0:25',
            'thing': 'study',
            'place': 'lib',
        }
        create(dic)
        delete(dic)
        inviter = User.objects.filter(session_key=123)[0]
        invitation = Invitation.objects.filter(inviter=inviter, date = '2018-12-31', time='00:25')
        self.assertEqual(invitation.count(), 0)
        calendar = Calendar.objects.filter(user=inviter, date='2018-12-31', time='00:25')
        self.assertEqual(calendar.count(), 0)