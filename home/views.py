import re
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import about
from django.contrib import messages
from postbook.models import Post, TradeRequest

def home(request):
    allposts = Post.objects.all()
    Context = { 'allposts': allposts }
    return render(request, 'index.html', Context)

def index(request):
    return redirect('home')

def chat(request):
    return render(request, 'chats.html')

@login_required(login_url='home')
def new_post(request):
    if request.method =='POST':
        title = request.POST.get('title', '')
        cover = request.FILES.get('cover') 
        author = request.POST.get('author', '')
        info = request.POST.get('info', '')
        phone = request.POST.get('phone', '')
        
        if len(title)==0 or len(author)<1 or len(info)<1 or len(phone)<10:
            messages.error(request,"Please fill all the fields correctly")
        else:
            new_book = Post(owner=request.user, title=title, cover=cover, author=author, info=info, phone=phone)
            new_book.save()
            messages.success(request, "Your Post is Successfully uploaded.")
            return redirect('profile')
    return render(request, 'newpost.html')

@login_required(login_url='home')
def profile(request):
    my_books = Post.objects.filter(owner=request.user)
    incoming_requests = TradeRequest.objects.filter(book_requested__owner=request.user).order_by('-timestamp')
    outgoing_requests = TradeRequest.objects.filter(requester=request.user).order_by('-timestamp')
    
    context = {
        'my_books': my_books,
        'incoming_requests': incoming_requests,
        'outgoing_requests': outgoing_requests
    }
    return render(request, 'profile.html', context)

def register(request):
    return render(request, 'register.html')


def contactus(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        content = request.POST['content']
        
        if len(name)<2 or len(email)<3 or len(phone_no)<10 or len(content)<1 :
            messages.error(request,"Please fill the form correctly")
        else:    
            contact = about(name=name, email=email, phone=phone_no, content=content)
            contact.save()
            messages.success(request, "Thank you, Your message has been successfully sent.")
    return render(request, 'contactus.html')

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST.get('phone', '') # fixed variable
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 10:
            messages.error(request, "Username must be of 10 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username only contain letters and numbers")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "Password does not match. Type the same password twice.")
            return redirect('home')
        if User.objects.filter(username=username).exists():
           messages.error(request, "Username already taken.")
           return redirect('home')

        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created. Please log in.")
        return redirect('home')
    else:
        return HttpResponse('404 - Page Not Found')

def posted(request):
    allposts = Post.objects.all()
    Context = { 'allposts': allposts }
    return render(request, 'posted.html', Context)

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid UserId or Password, Please try again")
            return redirect('home')
    else:
        return HttpResponse ('404 - Page Not Found')

def handlelogout(request):
    logout(request)
    messages.success(request, "You have been successfully Logged Out")
    return redirect('home')

def notauthenticated(request):
    messages.error(request,"you have to first signup or login")
    return redirect('home')

def search(request):
    query=request.GET.get('query', '')
    allposts = Post.objects.filter(title__icontains=query)
    Context = { 'allposts': allposts }
    return render(request, 'search.html', Context)

def read(request):
    return render(request, 'read.html')


# Trade System Views
@login_required(login_url='home')
def request_trade(request, book_id):
    book = get_object_or_404(Post, id=book_id)
    if book.owner == request.user:
        messages.error(request, "You cannot request a trade for your own book.")
        return redirect('home')
    
    if TradeRequest.objects.filter(requester=request.user, book_requested=book, status='Pending').exists():
        messages.error(request, "You already have a pending request for this book.")
        return redirect('home')

    if request.method == 'POST':
        message = request.POST.get('message', '')
        TradeRequest.objects.create(requester=request.user, book_requested=book, message=message)
        messages.success(request, f"Trade request sent to {book.owner.username}!")
        return redirect('profile')

    return render(request, 'request_trade.html', {'book': book})

@login_required(login_url='home')
def accept_trade(request, req_id):
    trade_req = get_object_or_404(TradeRequest, id=req_id, book_requested__owner=request.user)
    trade_req.status = 'Accepted'
    trade_req.save()
    
    book = trade_req.book_requested
    book.status = 'Trade Pending'
    book.save()
    
    messages.success(request, f"You accepted the trade request from {trade_req.requester.username}!")
    return redirect('profile')

@login_required(login_url='home')
def decline_trade(request, req_id):
    trade_req = get_object_or_404(TradeRequest, id=req_id, book_requested__owner=request.user)
    trade_req.status = 'Declined'
    trade_req.save()
    messages.warning(request, f"You declined the trade request from {trade_req.requester.username}.")
    return redirect('profile')
