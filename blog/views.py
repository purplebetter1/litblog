from django.shortcuts import render

# Create your views here.

from .models import Blog, BlogAuthor, BlogComment
from django.views import generic

def index(request):

	return render(request,'index.html')

from django.views.generic.list import ListView

class BlogListView(generic.ListView):
	model = Blog

class BloggerListView(generic.ListView):
	model = BlogAuthor
	 