from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
class Subject(models.Model):
    subject_year     = models.IntegerField(null=True,default='2020')
    subject_category = models.CharField(max_length = 20,null=True,default='전공')
    subject_title    = models.CharField(max_length = 20,null=True,default='')
    subject_point    = models.IntegerField(null=True)
    subject_code     = models.CharField(max_length = 20,null=True,default='')

    def __str__(self):
        return str(self.subject_year) + "년 " + self.subject_category + " " + self.subject_title
