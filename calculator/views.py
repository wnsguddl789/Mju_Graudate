from django.shortcuts import render
from .models import Subject

# Create your views here.
def select(request):
    subject = Subject.objects.all()


    return render(request,'select.html')
