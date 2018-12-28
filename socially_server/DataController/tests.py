from django.test import TestCase

from DataController.views import *

class DataController(TestCase):
    def setUp(self):
        create_user(123)
    def test_check_user(self):
        """
        check whether the user has logged in
        """
        self.assertEqual(check_user(123), True)
        self.assertEqual(check_user(456), False)
    def test_get_event_key(self):
        """
        get event key for a specific user
        the key will increase by one when triggered
        """
        self.assertEqual(get_event_key(123), 1)
        self.assertEqual(get_event_key(123), 2)
        self.assertEqual(get_event_key(123), 3)
