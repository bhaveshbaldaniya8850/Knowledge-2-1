"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import path
from home import views
# from postbook import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.home, name='home'),
    path("", views.index, name='index'),
   path("chat", views.chat, name='chat'),
   path("new_post", views.new_post, name='new_post'),
   path("posted", views.posted, name='posted'),
   path("profile", views.profile, name='profile'),
   path("contactus", views.contactus, name='contactus'),
   path("signup", views.handlesignup, name='handlesignup'),
   path("login", views.handlelogin, name='login'),
   path("logout", views.handlelogout, name='logout'),
   path("notauthenticated", views.notauthenticated, name='notauthenticated'),
   path("search", views.search, name='search'),
   path("read", views.read, name='read'),
   
   path("request_trade/<int:book_id>/", views.request_trade, name='request_trade'),
   path("accept_trade/<int:req_id>/", views.accept_trade, name='accept_trade'),
   path("decline_trade/<int:req_id>/", views.decline_trade, name='decline_trade'),


]
