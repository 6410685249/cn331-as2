from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Student
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

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
    
    def test_index_view_authenticated_user(self):
        response = self.client.post(reverse('login'), {'username': '6410681111', 'password': 'iamharry123'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        user = authenticate(username='6410681111', password='iamharry123')
        self.assertTrue(user.is_authenticated)
        
    # def test_index_view_unauthenticated_user(self):
    #     self.client.logout()
    #     response = self.client.get(reverse('index'))
    #     self.assertIsInstance(response, HttpResponseRedirect)
    #     # self.assertEqual(response, HttpResponseRedirect)  # Redirect to login page
    #     # self.assertRedirects(response.url, reverse('login'))
    #     self.assertEqual(response.url, reverse('login'))