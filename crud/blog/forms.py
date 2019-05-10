#우리가 만든 Model을 바로 Form으로 바꿔줌!!
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  class Meta: # 직접적으로 데이터를 건드리기 보다는, 어떤걸 사용하고 싶은지 전달해줌. form에서 자동으로 만들어준다.
    model = Post
    fields = ('title', 'contents',)
    # We need to tell Django that this form is a model form...
    # which model should be used to create this form

    # 장고 docs
    # https://docs.djangoproject.com/en/dev/_modules/django/forms/models/#ModelForm
    # https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#modelforms-selecting-fields