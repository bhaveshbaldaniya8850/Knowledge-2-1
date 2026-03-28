from postbook.views import postbookall, posted
from django.contrib import admin
from django.urls import path , include
from postbook import views

urlpatterns = [
    path('',views.home, name='home'),
    path('posted',views.posted,name='posted'),

]
