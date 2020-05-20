import json
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .forms import Create_post
from .models import Blog , Comment , Calculator , Account
from .forms import BlogCommentForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def index(request):
    return render(request,'index.html')
def blogMain(request):
    blogs = Blog.objects.all()
    return render(request,'blogMain.html',{'blogs':blogs})
def features(request):
    return render(request,'features.html')
def contact(request):
    return render(request,'contact.html')
def create_post(request):

    if request.method == 'POST':
        form = Create_post(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blogMain')
        else:
            return redirect('index')
    else:
        form = Create_post()
        return render(request,'create_post.html',{'form':form})
def calculator(request):
    calculator = Calculator.objects.all()
    context = {'calculator':calculator}
    return render(request,'calculator.html', context)
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog_id=blog_id)

    if request.method == 'POST':
        comment_form = BlogCommentForm(request.POST)

        if comment_form.is_valid():
            content = comment_form.cleaned_data['comment_textfield']

            print(content)

            return redirect('blogMain')
        else:
            return redirect('blogMain')

    else:
        comment_form = BlogCommentForm()

        context = {
            'blog_detail': blog_detail,
            'comments': comments,
            'comment_form': comment_form
        }

        return render(request, 'detail.html', context)

def signup(request):
    if request.method =="POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = Account.objects.create_user(
                username   = request.POST["username"],
                password   = request.POST["password1"],
                name       = request.POST["name"],
                major      = request.POST["major"],
                addmission = request.POST["addmission"]
            )
            auth.login(request,user)
            return redirect('blogMain.html')
        return render(request,'signup.html')
    return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('blogMain.html')
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('blogMain.html')
        else:
            return render(request,'signin.html',{'error':'username or password is incorrect'})
    else:
        return render(request,'signin.html')
