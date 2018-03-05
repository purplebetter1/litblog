from django.shortcuts import render

# Create your views here.

from .models import Blog, BlogAuthor, BlogComment
from django.views import generic

def index(request):

	return render(request,'index.html')