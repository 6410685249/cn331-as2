# from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.admin.sites import AdminSite
from users.models import Student
from administrator.models import Subject
from administrator.admin import SubjectManage
    
class RegisterViewsTest(TestCase):
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
        self.cs101 = Subject.objects.create(name='Introduction Programing', code='CS101',
                                             professor='John', semester='1',
                                            year='2023', seat=1)
        self.cn201 = Subject.objects.create(name='OOP', code='CN201',
                                             professor='Taweesak', semester='1',
                                            year='2023', quota=True, seat=1)

        self.cn331.save()
        self.cn321.save()
        self.cn361.save()
        self.cs101.save()
        self.cn201.save()
    
    def test_Add_Subject_view(self):
        self.client.login(username='6410681111', password='iamharry123')
        subjects_code = ['CN331', 'CN321', 'CS101']
        for code in subjects_code:     
            response = self.client.get(reverse('reg:Add_Subject', args=[code]))
            self.assertEqual(response.status_code, 200)
        
        # Verify that the student is enrolled in the subject
        student_subjects = self.student1.subjects.all()
        self.assertTrue(self.cn331 in student_subjects)
        self.assertTrue(self.cn321 in student_subjects)
        self.assertTrue(self.cs101 in student_subjects)    

    def test_Add_Quota_view(self):
        self.client.login(username='6410681111', password='iamharry123')
        subjects_code = ['CN361', 'CN201']
        for code in subjects_code:
            response = self.client.post(reverse('reg:Add_Quota', args=[code]))
            self.assertEqual(response.status_code, 200)

         # Verify that the student is enrolled in the subject
        student_subjects = self.student1.subjects.all()
        self.assertTrue(self.cn361 in student_subjects)
        self.assertTrue(self.cn201 in student_subjects)


    def test_Delete_Subject_view(self):
        self.client.login(username='6410681111', password='iamharry123')
        self.student1.subjects.add(self.cn331)
        self.student1.subjects.add(self.cn321)

        response = self.client.get(reverse('reg:Delete_Subject', args=['CN331',]))
        self.assertEqual(response.status_code, 200)
        
        # Verify that the student is deleted subject
        student_subjects = self.student1.subjects.all()
        self.assertFalse(self.cn331 in student_subjects)
        self.assertTrue(self.cn321 in student_subjects)
        
    def test_logout_view(self):
        self.client.login(username='6410681111', password='iamharry123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('message' in response.context)
        self.assertEqual(response.context['message'], 'Logged out')
        self.assertFalse(response.context['user'].is_authenticated)

class StudentEnrollmentAdminTest(TestCase):
    def setUp(self):
        # Create admin for test
        self.admin = User.objects.create_superuser(username='admin', password='adminpassword123')
        self.admin.is_staff = True
        self.admin.save()
        
        # Create student for test
        self.user1 = User.objects.create_user(username='6410681111', password='iamharry123',
                                               first_name='Harry', last_name='Potter')
        self.student1 = Student.objects.create(user=self.user1, student_id='6410681111',
                                               status=True, faculty='Engineering')

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
        self.cs101 = Subject.objects.create(name='Introduction Programing', code='CS101',
                                             professor='John', semester='1',
                                            year='2023', seat=1)
        self.cn201 = Subject.objects.create(name='OOP', code='CN201',
                                             professor='Taweesak', semester='1',
                                            year='2023', quota=True, seat=1)

        self.cn331.save()
        self.cn321.save()
        self.cn361.save()
        self.cs101.save()
        self.cn201.save()
        
        self.student1.subjects.add(self.cn201)
        self.student1.subjects.add(self.cn321)

    def test_student_enrolled_in_subject(self):
        self.client.login(username='admin', password='adminpassword123')

        # CN321
        subject_url1 = reverse('admin:administrator_subject_change', args=[self.cn321.code])
        
        # Get student id from students attribute
        response1 = self.client.post(subject_url1, {
            'fileter_horizental': [str(self.student1.user)],
        })

        # Check if the action message is displayed
        self.assertContains(response1, '6410681111')
        
        
        #CN201
        subject_url2 = reverse('admin:administrator_subject_change', args=[self.cn201.code])
        response2 = self.client.post(subject_url2, {
            'fileter_horizental': [str(self.student1.user)],
        })

        # Check if the action message is displayed
        self.assertContains(response2, '6410681111')
        
