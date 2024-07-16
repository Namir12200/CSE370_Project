from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'login.html')


def register(request):
    if (request.method == "POST"):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def home(response):
    return render(response, 'users/home.html', {})


def about(response):
    return render(response, 'users/about.html', {})


def contact(response):
    return render(response, 'users/contact.html', {})


def profile(response):
    return render(response, 'users/profile.html', {})
