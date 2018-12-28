from django.test import TestCase

from .views import *
from DataController.views import *

class CalendarTest(TestCase):
    def setUp(self):
        create_user(123)

    def test_create(self):
        dic = {
            'sessionKey': 123,
            'date': '2018-12-28',
            'time': '21:36',
            'thing': 'study',
            'place': 'lib'
        }
        self.assertEqual(create(dic), '001')