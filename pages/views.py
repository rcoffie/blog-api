from django.shortcuts import render
from blog.models import *
from django.core.paginator import Paginator
# Create your views here.


def home(request):
  headlines_post = Post.objects.filter(headline_post=True)
  posts = Post.objects.filter(featured_post=True)
  p = Paginator(posts,6)
  page_number = request.GET.get('page')
  try:
    page_obj = p.get_page(page_number)
  except PageNotAnInteger:
    page_obj = p.page(1)
  except EmptyPage:
    page_obj = {'page_obj': page_obj}

   
  return render(request,'blog/pages/index.html', {'page_obj':page_obj,'headlines_post':headlines_post,})
  