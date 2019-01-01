from django.test import TestCase

from .views import *

class TestLogin(TestCase):
    def setUp(self):
        create_user(123)
    def test_get_event_key(self):
        """
        input: sessionKey(equals to userID)
        output: eventnum +1
        """
        self.assertEqual(get_event_key(123), 1)
        self.assertEqual(get_event_key(123), 2)
        self.assertEqual(get_event_key(123), 3)
    def test_check_user(self):
        """
        input: sessionKey
        output: whether the user exits
        """
        self.assertEqual(check_user(123), True)
        self.assertEqual(check_user(456), False)

class TestConflict(TestCase):
    def setUp(self):
        create_user(123)
        eventKey = get_event_key(123)
        dic = {
            'sessionKey': 123,
            'eventKey': eventKey,
            'date': '2018-12-30',
            'time': '19:56',
            'thing': 'study',
            'place': 'lib',
            'type': 1
        }
        create_calendar(dic)

    def test_check_conflict(self):
        """
        input: dic(date,time,thing,place etc)
        output: "ok" when no conflict
                the corresponding eventKey when conflict
        only when the date and time do not conflict will the test pass
        """
        eventKey = get_event_key(123)
        dic = {
            'sessionKey': 123,
            'eventKey': eventKey,
            'date': '2018-12-30',
            'time': '19:56',
            'thing': 'study',
            'place': 'lib',
            'type': 1
        }
        self.assertEqual(check_conflict(dic['sessionKey'], dic['date'], dic['time'])['eventKey'], '001')
        dic['date'] = '2018-12-31'
        self.assertEqual(check_conflict(dic['sessionKey'], dic['date'], dic['time']), 'ok')
        dic['date'] = '2018-12-30'
        dic['time'] = '19:00'
        self.assertEqual(check_conflict(dic['sessionKey'], dic['date'],dic['time']), 'ok')