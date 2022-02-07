from django import forms 
from .models import Comment
from crispy_forms.helper import FormHelper  
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Button
from crispy_forms.bootstrap import InlineRadios 



class EmailPostForm(forms.Form):

  name = forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
  email = forms.EmailField(max_length=25,label = '',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
  to    = forms.EmailField(max_length=25,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'To'}))
  comments = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'comments'}))




  

  
   


class CommentForm(forms.ModelForm):

  name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
  body  = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control mb-2','placeholder':'Body'}))
  
  class Meta:
    model = Comment 
    fields = ('name','email','body')

  
  




class SearchForm(forms.Form):
  query = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholoder':'Search'}))
  



  """   widgets = {
    'name' : forms.TextInput(attrs={'class':'form-control'}),
    
    'frequency' : forms.NumberInput(attrs={'class':'form-control'}),
 
    }
    
 def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.fields['name'].label = "Name"
    self.fields['frequency'].label = 'Frequency'
   
    self.helper.form_method = 'post'
    self.helper.add_input(Submit('add_new_training_type','Add'))
    self.helper.layout = Layout(
      Row(
        Column('name'),
      ),
      Row(
        Column('frequency')
      )
    ) """

    