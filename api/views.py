from django.shortcuts import render
from .serializers import PostSerializer 
from rest_framework import generics
from rest_framework.permissions import IsAdminUser 
from blog.models import *

# Create your views here.
class PostList(generics.ListAPIView):
  serializer_class = PostSerializer 
  
  def get_queryset(self):
    return Post.objects.filter(status='published').order_by('-created')
