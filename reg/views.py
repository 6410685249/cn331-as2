from django.shortcuts import render
from administrator.models import Subject
from users.models import Student

# Create your views here.

# def quota(request):
#     return render(request, 'index.html')

'''
    ปุ่มที่กดเพิ่มนำรายวิชาโควต้าที่เลือกส่งเข้าไปใน list_subject 
'''
def Add_Quota(request, code):
    subject = Subject.objects.get(code=code)

    return render(request)

# def Delete_Quota(request):
# def Add_Subject(request):
# def Delete_Subject(request):

def Quota(request):
    student = Student.objects.get(user_id=request.user)
    student_subjects = student.subjects.all()
    return render(request, 'Quota.html', {
        'subjects' : student_subjects,
        'count' : len(student_subjects),
    })