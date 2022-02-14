from rest_framework import serializers
from blog.models import *


# class UserSerializer(serializers.HyperlinkedModeSerializer):

#   class Meta:
#     model = User
#     fields = ['url','username','email','groups']



class PostSerializer(serializers.ModelSerializer):
  created = serializers.ReadOnlyField()

  class Meta:
    model = Post 
    fields = ['id','title','hot','headline_post','featured_post','author','body','publish','created','status']