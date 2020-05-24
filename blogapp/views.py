import json
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .forms import Create_post ,BlogCommentForm
from .models import Blog , Comment , Calculator
from django.shortcuts import render, redirect
from django.conf import settings
from account.models import User
# Create your views here.
def index(request):
    return render(request,'index.html')
def blogMain(request):
    user  = User.objects.filter(name="email")
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
