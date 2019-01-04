from django.test import TestCase

from .views import *
from DataController.views import *

class TestCalendar(TestCase):
    def setUp(self):
        create_user(123)
    def test_create(self):
        """
        input: event dic
        output: eventKey
        """
        dic = {
            'sessionKey': 123,
            'date': '2018-12-30',
            'time': '19:56',
            'thing': 'study',
            'place': 'lib',
        }
        self.assertEqual(create(dic), '001')
        dic = {
            'sessionKey': 123,
            'date': '2018-12-30',
            'time': '19:00',
            'thing': 'study',
            'place': 'lib',
            'eventKey': 2,
            'type': 2
        }
        self.assertEqual(create(dic, 2), '002')
    def test_get(self):
        """
        input: sessionKey
        output: schedule for that user
        """
        dic = {'sessionKey': 123}
        self.assertEqual(get(dic).__len__(), 0)
        dic = {
            'sessionKey': 123,
            'date': '2018-12-30',
            'time': '19:56',
            'thing': 'study',
            'place': 'lib',
        }
        self.assertEqual(create(dic), '001')
        dic = {'sessionKey': 123}
        self.assertEqual(get(dic).keys(), {'2018-12-30': 1}.keys())