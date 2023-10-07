from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.models import Student

# Create your views here.
def index(request):
    student = Student.objects.get(user_id=request.user)
    student_subjects = student.subjects.all()
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'index.html', {
        'student' : student,
        'subjects' : student_subjects,
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'login.html', {
                'message': 'Invalid credentials!'
            })
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return render(request, 'login.html', {
        'message': 'Logged out'
    })
