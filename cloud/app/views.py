from telnetlib import LOGOUT
from django.shortcuts import render
from flask import render_template
from django.shortcuts import redirect, render
from .forms import UserForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request , "index.html")

def home(request):
    return render(request , "home.html")

def about(request):
    return render(request , "About.html")

def scope(request):
    return render(request , "scope.html")

def services(request):
    return render(request , "services.html")




def register_page(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        # user_info_form = UserInfoForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # user_info = user_info_form.save(commit=False)

            # user_info.user = user

            # if 'profile_pic' in request.FILES:
            #     user_info.profile_pic = request.FILES['profile_pic']
            # user_info.save()
            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()
        # user_info_form = UserInfoForm()

    return render(request, 'register.html', {'user_form':user_form,})

# def login_page(request):
#     login_error=''
#     login_form=LoginForm()

#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')

#         user=authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request,user)
#                 return redirect(reverse('userapp:home'))
#             else:
#                 return HttpResponse('Acount is not active')
#         else:
#             login_error = 'Invalid Login Details'

#     return render(request,'login.html',{'login_error':login_error,'login_form':login_form})

# @login_required
# def index(request):
#     return render(request, 'index.html')

# @login_required
# def logout_page(request):
#     logout(request)
#     return redirect(reverse('app:index'))

def career_page(request):
    return render(request , "career.html")

def interview_page(request):
    return render(request , "interview.html")

def cv_building(request):
    return render(request , "cvbuilding.html")
