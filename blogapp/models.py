from django.db import models
from django.contrib.auth.models import User, UserManager
from django.contrib import auth
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Account(models.Model):
    username   = models.CharField(max_length = 200)
    password   = models.CharField(max_length = 500)
    name       = models.CharField(max_length = 20,null=True,default='')
    major      = models.CharField(max_length = 20,null=True,default='')
    addmission = models.CharField(max_length = 20,null=True,default='')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete=True, null=True, default=1)
    body = RichTextUploadingField()
    def __str__(self):
        return self.title

class Comment(models.Model):
     blog = models.ForeignKey(Blog, on_delete=True, null=True)
     comment_date = models.DateTimeField(auto_now_add = True)
     comment_user = models.TextField(max_length=20)
     comment_thumbnail_url = models.TextField(max_length=300)
     comment_textfield = models.TextField()
     def __str__(self):
         return self.comment_user

class Calculator(models.Model):

    semester = models.TextField(default = '')
    subject = models.TextField(default = '')
    title = models.TextField()
    point = models.TextField()
    code = models.TextField()
    def __str__(self):
        return self.semester
