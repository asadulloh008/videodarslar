from django.shortcuts import render, redirect
from django.urls import reverse
from .form import SignUpForm, LogInForm

def sign_or_log(request):
    return render(request, "sign_or_log.html")

def signup(request):
    sign=SignUpForm()
    print("1")
    if request.method == 'POST':
        print("2")
        sign=SignUpForm(request.POST,request.FILES)
        # sign.save()
        if sign.is_valid():
            sign.save()
            print("3")
            return redirect(reverse('course_app:home'))
    return render(request, "signup.html", {'sign':sign})

def login(request):
    log=LogInForm()
    return render(request, "login.html", {'log':log})