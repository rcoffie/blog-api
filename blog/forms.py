from django import forms 
from .models import Comment


class EmailPostForm(forms.Form):
  name = forms.CharField(max_length=25)
  email = forms.EmailField(max_length=25)
  to    = forms.EmailField(max_length=25)
  comments = forms.CharField(required=False,widget=forms.Textarea)


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment 
    fields = ('name','email','body')
    