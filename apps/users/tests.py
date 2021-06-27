import datetime

from django.test import TestCase
from django.urls import reverse

from .models import CustomUser as User
from .templatetags.custom_tags import bizz_fuzz, check_age


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


class UserUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create(
            username='User1',
            birthday='2000-03-12',
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/user/{self.user.pk}/')
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('user-update', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('user-update', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_update.html')

    def test_update_user(self):

        response = self.client.post(
            reverse('user-update', args=[self.user.pk]),
            {'username': 'updated_username', 'birthday': '2000-10-10'})

        self.assertEqual(response.status_code, 302)

        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updated_username')
        self.assertEqual(self.user.birthday, datetime.date(2000, 10, 10))


class UserCreateViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/user/create')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('user-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('user-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_create.html')

    def test_create_user(self):

        response = self.client.post(
            reverse('user-create'),
            {'username': 'username', 'birthday': '2000-10-10'})

        self.assertEqual(response.status_code, 302)

        user = User.objects.last()

        self.assertEqual(user.username, 'username')
        self.assertEqual(user.birthday, datetime.date(2000, 10, 10))


class UserDeleteViewTest(TestCase):

    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create(
            username='User1',
            birthday='2000-03-12',
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/user/{self.user.pk}/delete/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('user-delete', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('user-delete', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_confirm_delete.html')

    def test_get_request(self):
        response = self.client.get(reverse('user-delete', args=[self.user.pk]), follow=True)
        self.assertContains(response, f'Are you sure you want to delete "{self.user}"?')

    def test_post_request(self):
        post_response = self.client.post(reverse('user-delete', args=[self.user.pk]), follow=True)
        self.assertRedirects(post_response, reverse('users'), status_code=302)


class UserDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create(
            username='User1',
            birthday='2000-03-12',
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/users/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('user-detail', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('user-detail', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_detail.html')

    def test_get_request(self):
        response = self.client.get(reverse('user-detail', args=[self.user.pk]), follow=True)
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.random_number)



class BizzFuzzTemplateTagTest(TestCase):

    def test_number_divisible_by_5(self):
        result = bizz_fuzz(10)
        self.assertEqual(result, 'Fuzz')

    def test_number_divisible_by_3(self):
        result = bizz_fuzz(18)
        self.assertEqual(result, 'Bizz')

    def test_number_divisible_by_3_and_5(self):
        result = bizz_fuzz(60)
        self.assertEqual(result, 'BizzFuzz')

    def test_number_indivisible_by_3_and_5(self):
        result = bizz_fuzz(67)
        self.assertEqual(result, '67')


class CheckAgeTemplateTagTest(TestCase):

    def test_number_less_than_13(self):
        result = check_age(12)
        self.assertEqual(result, 'blocked')

    def test_number_greater_than_13(self):
        result = check_age(24)
        self.assertEqual(result, 'allowed')

    def test_number_13(self):
        result = check_age(13)
        self.assertEqual(result, 'blocked')