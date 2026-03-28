from typing import ContextManager
from django.shortcuts import render, HttpResponse
from postbook.models import post

# Create your views here.
# def posted(request):
#     allpost = post.objects.all()
#     print(allpost)
#     Context = { 'allpost': allpost }
#     return render(request, 'postbook/posted.html', Context)

def postbookall(request):
    return render(request, 'postbook/postbookposts.html')
