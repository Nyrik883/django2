from .models import Blog 
from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(max_length=100, label='название блога')
    descritions = forms.CharField(widget =forms.Textarea,label='описание')
    public = forms.BooleanField()

class FeedBlogForm(forms.ModelForm):
    class Meta:
        model = Blog 
        fields = ['title' , 'descriptions', 'public', 'img']

