from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models
from authenticate.models import TODO


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
    
        print(fnm, emailId, pwd)
    return render(req,'authenticate/register.html')

def login(req):
    return render(req, 'authenticate/login.html')