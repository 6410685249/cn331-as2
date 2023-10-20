from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Student
from administrator.models import Subject

class HomeViewTest(TestCase):
    def setUp(self):
        # Create user for test
        self.user1 = User.objects.create_user(username='6410681111', password='iamharry123',
                                               first_name='Harry', last_name='Potter')
        self.student1 = Student.objects.create(user=self.user1, student_id='6410681111',
                                               status=True, faculty='Engineering')
        # self.user2 = User.objects.create_user(username='6410681112', password='iamhermione123',
        #                                        first_name='Hermione', last_name='granger')
        # self.student2 = Student.objects.create(user=self.user2, student_id='6410681112',
        #                                        status=True, faculty='Science')
        

        # Create subjects for test
        self.cn331 = Subject.objects.create(name='Software Engineering', code='CN331',
                                             professor='Weerachai', semester='1',
                                            year='2023', seat=100)
        self.cn321 = Subject.objects.create(name='Network 1', code='CN321',
                                             professor='Taweesak', semester='1',
                                            year='2023', seat=100)
        self.cn361 = Subject.objects.create(name='Microprocessor', code='CN361',
                                             professor='Nawin', semester='1',
                                            year='2023', quota=True, seat=10)
        self.cs101 = Subject.objects.create(name="Introduction Programing", code='CS101',
                                             professor='John', semester='1',
                                            year='2023', seat=1)
        self.cn201 = Subject.objects.create(name="OOP", code='CN201',
                                             professor='Taweesak', semester='1',
                                            year='2023', quota=True, seat=1)

        self.cn331.save()
        self.cn321.save()
        self.cn361.save()
        self.cs101.save()
        self.cn201.save()
        
        self.student1.subjects.add(self.cn201)
        self.student1.subjects.add(self.cn321)
    
    def test_Home_view(self):
        self.client.login(username='6410681111', password='iamharry123')
        response = self.client.get(reverse('reg:Home'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        
        # Show Student Information
        self.assertContains(response, 'Harry Potter') # Name Surname
        self.assertContains(response, '6410681111') # Student ID
        self.assertContains(response, 'Engineering') # Faculty
        
        # List of Subject is enrolled --> They must show in Home Page.
        self.assertContains(response, 'Network 1')
        self.assertContains(response, 'OOP')
        self.assertNotContains(response, 'Software Engineering')
        self.assertNotContains(response, 'Introduction Programming')
        self.assertNotContains(response, 'Microprocessor')

    def test_Subject_page_view(self):
        self.client.login(username='6410681111', password='iamharry123')
        response = self.client.get(reverse('reg:Subject_page'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Adding_page.html')
    
    def test_Quota_view(self):
        self.client.login(username='6410681111', password='iamharry123')
        response = self.client.get(reverse('reg:Quota'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Quota.html')
