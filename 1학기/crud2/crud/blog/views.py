from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, Comment

# Create your views here.
def home(request):
  posts = Post.objects.all()
  return render(request, 'home.html', {'posts':posts})

def new(request):
  # 그냥 올릴때는 get 방식이 되고, 쏴줄때는 post 방식이 된다.
  if request.method == "POST":
    form = PostForm(request.POST)
    post = form.save(commit = False) # 바로 저장되지 않고, post 객체가 나오게 된다.
    post.save()
    return redirect('home')
  else:
    form = PostForm()
    return render(request, 'new.html', {'form':form}) #form이라는 이름의 변수로 form을 넣어준다.

def detail(request, post_pk):
  if request.method =="POST":
    post = Post.objects.get(pk=post_pk)
    form = CommentForm(request.POST)
    comment = form.save(commit = False)
    comment.post = post
    comment.save()
    return redirect('detail', post.pk)
  else:
    post = Post.objects.get(pk=post_pk)
    form = CommentForm() # 빈 CommentForm이 여기 들어감
    return render(request, 'detail.html', {'post':post, 'form':form})

def delete(request, post_pk, comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  comment.delete()
  return redirect('detail', post_pk)
