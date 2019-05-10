from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'content')

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('comment', ) #그냥 괄호가 되지 않게, 뒤에 콤마를 찍어주기!!
    
    