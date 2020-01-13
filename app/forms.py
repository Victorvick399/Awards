from django import forms
from .models import Profile, Post

class ProfileForm(forms.ModelForm):
    '''
    This is a form to create a profile.
    '''
    class Meta:
        model = Profile
        fields = ['image','bio','contacts']
        exclude = ['user']

class PostForm(forms.ModelForm):
    '''
    This is a form for the post model.
    '''
    class Meta:
        model = Post
        fields = ['title','photo','description','link']
        exclude = ['posted_on', 'posted_by']
         