from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, UserManager
from django.contrib import auth
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

from django.conf import settings
User = settings.AUTH_USER_MODEL

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey('auth.User', on_delete=True, null=True, default=1)
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
