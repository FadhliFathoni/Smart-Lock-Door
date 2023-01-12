from django.shortcuts import render,redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from .forms import LoginForm

def loginView(request):
    context = {
        "form":LoginForm
    }
    return render(request,'login.html',context)