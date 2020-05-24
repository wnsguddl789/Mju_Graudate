from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('logout/',views.logout, name='logout'),
    path('signin/',views.signin, name='signin'),
    #url(r'^join/$', views.signup, name='join'),
]
