"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import pathm inlcude
import blogapp.views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.index, name='index'),
    path('Features',blogapp.views.features, name="features"),
    path('contact',blogapp.views.contact, name="contact"),
    path('blogMain/',blogapp.views.blogMain,name='blogMain'),
    path('blogMain/create_post',blogapp.views.create_post,name='create_post'),
    path('blogMain/calculator',blogapp.views.calculator,name='calculator'),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('blogMain/detail/<int:blog_id>/', blogapp.views.detail, name='detail'),
    path('signup/',blogapp.views.signup, name='signup'),
    path('logout/',blogapp.views.logout, name='logout'),
    path('signin/',blogapp.views.signin, name='signin'),
    path('accounts/', include('django.contrib.auth.urls')), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
