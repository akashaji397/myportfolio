from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login as auth_login


def Register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful! Please log in.')
                return redirect('login')
        else:
            messages.info(request, "The passwords do not match.")
            return redirect('register')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)  # Use the aliased login function

            return redirect('home_view')
        else:
            messages.info(request, "Please provide valid credentials")
            return redirect('login')
        
    return render(request, 'login.html')

def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect('login')