
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Features',views.features, name="features"),
    path('contact',views.contact, name="contact"),
    path('blogMain/',views.blogMain,name='blogMain'),
    path('blogMain/create_post',views.create_post,name='create_post'),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('blogMain/detail/<int:blog_id>/', views.detail, name='detail'),

]
