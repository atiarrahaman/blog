from django import forms 
from . models import Post,Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# create your forms


class Post_Form(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','des','catagory','img']
        
       

class CommetnsForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['comment']



class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']