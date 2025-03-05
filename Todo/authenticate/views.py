from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models
from authenticate.models import TODO
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(req):
    return render(req, 'index.html')

def signup(req):
    if req.method=='POST':
        fnm=req.POST.get('fnm')
        emailId=req.POST.get('email')
        pwd=req.POST.get('pwd')
        __user= User.objects.create_user(fnm,emailId,pwd)
        __user.save()
        
        return redirect('login')
    
    return render(req,'authenticate/register.html')

def signin(req):
    if req.method=='POST':
        fnm=req.POST.get('fnm')
        pwd=req.POST.get('pwd')
        __user=authenticate(req,username=fnm,password=pwd)
        if __user is not None:
            login(req,__user)
            return redirect('todo')
        else:
            return redirect('login')

    return render(req,'authenticate/login.html')


@login_required(login_url="login")
def todo(req):
    return render(req, 'todo/todo.html')