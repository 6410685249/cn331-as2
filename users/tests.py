from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Student
from administrator.models import Subject

# Create your tests here.

class LoginViewsTest(TestCase):
    def setUp(self):
        # Create user for test
        self.user = User.objects.create_user(username='6410681111', password='iamharry123'
                                             , first_name='Harry', last_name='Potter')
        self.student = Student.objects.create(user=self.user, student_id='6410681111'
                                              , status=True, faculty='Engineering')

    def test_status_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    
    def test_login_view_valid_credentials(self):
        response = self.client.post(reverse('login'), {'username': '6410681111', 'password': 'iamharry123'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_login_view_invalid_credentials(self):
        response = self.client.post(reverse('login'), {'username': '6410681111', 'password': 'iamron12345'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('message' in response.context)
        self.assertEqual(response.context['message'], 'Invalid credentials!')
