from django.urls import path, include
from . import views
urlpatterns = [
    path('select/',views.select, name='select'),
]
