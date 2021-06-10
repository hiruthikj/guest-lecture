from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

from .models import Department

TEST_DEPT_CODE = 'test code'
TEST_DEPT_NAME = 'test dept name'


class LoginTest(TestCase):
  
    def setUp(self) -> None:
        self.dept = Department.objects.create(
            dept_code = 'test code',
            dept_name = 'test dept name'
        )
        User = get_user_model()
        self.user = User.objects.create_user(
            username='user',
            email='user@email.com',
            password='testpassword',
            # year_of_study=3,
            phone_no='1234567890',
            # dept_fk=dept
        )
    
    def test_create_dept(self):
        # dept = Department.objects.create(
        #     dept_code = TEST_DEPT_CODE,
        #     dept_name = TEST_DEPT_NAME
        # )
        self.assertEqual(self.dept.dept_code, TEST_DEPT_CODE)
        self.assertEqual(self.dept.dept_name, TEST_DEPT_NAME)

    def test_create_user(self):
        self.assertEqual(self.user.username, 'user')
        self.assertEqual(self.user.email, 'user@email.com')
        # self.assertEqual(user.year_of_study, 3)
        self.assertEqual(self.user.phone_no, '1234567890')

        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_login_view(self):

        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

    def test_logged_out_view(self):

        resp = self.client.get(reverse('logout'))
        self.assertEqual(resp.status_code, 200)