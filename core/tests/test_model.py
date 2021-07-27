from django.test import TestCase
from core.models import User
# Create your tests here.

class UserModelTest(TestCase):

    def setUp(self):
        User.objects.create(first_name = 'Sara', last_name = 'Ahmadova')

    def test_str_method(self):
        user = User.objects.get(first_name = "Sara")
        self.assertEqual(str(user), 'Sara')

    def test_full_name_method(self):
        user = User.objects.get(first_name = "Sara")
        self.assertEqual(user.get_full_name(), 'Sara Ahmadova')

    def test_isntance(self):
        user = User.objects.get(first_name = "Sara")
        self.assertIsInstance(user, User)