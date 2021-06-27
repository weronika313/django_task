import datetime

from django.test import TestCase
from django.urls import reverse

from .models import CustomUser as User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username="TestUser", birthday='2010-03-12')

    def test_username_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_birthday_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('birthday').verbose_name
        self.assertEqual(field_label, 'birthday')

    def test_object_name_is_username(self):
        user = User.objects.get(id=1)
        expected_object_name = user.username
        self.assertEqual(str(user), expected_object_name)

    def test_random_number_field(self):
        user = User.objects.get(id=1)
        self.assertGreaterEqual(user.random_number, 1)
        self.assertLessEqual(user.random_number, 100)


class UserListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_users = 12

        for user_id in range(number_of_users):
            User.objects.create(
                username=f'User {user_id}',
                birthday='2000-03-12',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_list.html')