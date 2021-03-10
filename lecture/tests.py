from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

from .models import CustomUser, Department

class LoginTest(TestCase):

    # def setUp(self) -> None:
    #     self.dept = Department.objects.create(
    #         dept_code = 'test code',
    #         dept_name = 'test dept name'
    #     )
    #     self.user = get_user_model().objects.create_user(
    #         username='testuser',
    #         email='test@email.com',
    #         password='secret'
    #     )

    def test_create_dept(self):
        dept = Department.objects.create(
            dept_code = 'test code',
            dept_name = 'test dept name'
        )
        self.assertEqual(dept.dept_code, 'test code')
        self.assertEqual(dept.dept_name, 'test dept name')

    def test_create_user(self):
        dept = Department.objects.create(
            dept_code = 'test code',
            dept_name = 'test dept name'
        )
        User = get_user_model()
        user = User.objects.create_user(
            username='user',
            email='user@email.com',
            password='testpassword',
            # year_of_study=3,
            phone_no='1234567890',
            # dept_fk=dept
        )

        self.assertEqual(user.username, 'user')
        self.assertEqual(user.email, 'user@email.com')
        # self.assertEqual(user.year_of_study, 3)
        self.assertEqual(user.phone_no, '1234567890')

        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_login_view(self):

        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

    def test_logged_out_view(self):

        resp = self.client.get(reverse('logout'))
        self.assertEqual(resp.status_code, 200)