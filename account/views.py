import json
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import User,UserManager
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.models import User, UserManager
from django.conf import settings
User = settings.AUTH_USER_MODEL

from .forms import SigninForm,UserCreationForm
from django.template import RequestContext
# Create your views here.

def signup(request):
    if request.method =="POST":
        if request.POST["password1"] == request.POST["password2"]:
            form = UserCreationForm(request.POST)
            user = User.objects.create_user(
                email      = request.POST["email"],
                password   = request.POST["password1"],
                name       = request.POST["name"],
                addmission = request.POST["addmission"],
                major      = request.POST["major"],
            )
            login(request,user)
            return redirect('blogMain')
        else:
            form = UserCreationForm()
        return render(request,'signup.html',{'form':form})
    return render(request,'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('blogMain.html')
def signin(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email = email, password = password)
        if user is not None:
            login(request,user)
            return redirect('blogMain')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해주세요.')

            #return render(request,'signin.html',{'error':'username or password is incorrect'})
    else:
        form = SigninForm()
        return render(request,'signin.html',{'form':form})
