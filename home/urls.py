from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path , include
from home import views

admin.site.site_header = "Knoledge^2+1 Admin"
admin.site.site_title = "Knoledge^2+1 Admin Portal"
admin.site.index_title = "Welcome to Knoledge^2+1 Researcher Portal"

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path("signup", views.handlesignup, name='signup'),
    path("posted", views.posted,name='posted'),
    path("login", views.handlelogin, name='login'),
    path("logout", views.handlelogout, name='logout'),
    path("search", views.search, name='search'),
    path("new_post", views.new_post, name='new_post'),
    path("read", views.read, name='read'),

]
