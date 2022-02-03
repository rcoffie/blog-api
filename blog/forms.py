from django import forms 
from .models import Comment
from crispy_forms.helper import FormHelper  
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Button
from crispy_forms.bootstrap import InlineRadios 



class EmailPostForm(forms.Form):
  name = forms.CharField(max_length=25)
  email = forms.EmailField(max_length=25)
  to    = forms.EmailField(max_length=25)
  comments = forms.CharField(required=False,widget=forms.Textarea)


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment 
    fields = ('name','email','body')
  

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()

    self.helper.form_class = 'form_control'
    self.helper.form_method = 'post'

    self.helper.add_input(Submit('submit', 'Submit'))
   


class SearchForm(forms.Form):
  query = forms.CharField()
    