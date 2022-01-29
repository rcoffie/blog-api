from django.shortcuts import render
from blog.models import *
# Create your views here.


def home(request):
  headlines_post = Post.objects.filter(headline_post=True)
  posts = Post.objects.filter(featured_post=True)

   
  return render(request,'blog/pages/index.html', {'posts':posts,'headlines_post':headlines_post,})
  