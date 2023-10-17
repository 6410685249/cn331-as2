from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Import your models and views
from .models import Subject, Student
from .views import Add_Quota, Home, Subject_page, Delete_Subject, Add_Subject, Quota, index

# Create your tests here.
class YourAppViewsTestCase(TestCase):
    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.user.save()

        # Create test subjects and students
        self.subject = Subject.objects.create(code="TEST1")
        self.student = Student.objects.create(user=self.user)

    def test_add_quota_view(self):
        # Log in the user
        self.client.login(username="testuser", password="testpassword")

        # Make a POST request to the Add_Quota view
        response = self.client.post(reverse('add_quota', args=(self.subject.code,)))

        # Check that the response status code is 200 (or another expected code)
        self.assertEqual(response.status_code, 200)

        # You can also make assertions about the response content and other aspects.

    # def test_home_view(self):
    #     # ...

    # def test_subject_page_view(self):
    #     # ...

    # def test_delete_subject_view(self):
    #     # ...

    # def test_add_subject_view(self):
    #     # ...

    # def test_quota_view(self):
    #     # ...

    # def test_index_view(self):
        # ...