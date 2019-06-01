from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def home(request):
  return render(request, 'home.html')

def new(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    # POST인 애들을 다 담아낸다!
    post = form.save(commit = False)
    # 우선 commit을 false라고 하고!
    form.save()
    # 저장
    return redirect('detail', post_pk = post.pk)
  else:
    form = PostForm()
    # 빈 form을 보여준다.
  return render(request, 'new.html', {'form':form})

def home(request):
  posts = Post.objects.all()
  return render(request, 'home.html', {'posts':posts})

def detail(request, post_pk):
  post = Post.objects.get(pk=post_pk)
  return render(request, 'detail.html', {'post':post})

def edit(request, post_pk):
  post = Post.objects.get(pk = post_pk)
  if request.method == 'POST':
    form = PostForm(request.POST, instance = post)
    # instance 값을 주면, 기존의 DB에 덮어쓰기를 한당!
    form.save()
    return redirect('detail', post.pk)
  else:
    form = PostForm(instance = post)
    # 데이터 베이스 만들어진 하나하나를 instance라고 할 수 있다.
  return render(request, 'edit.html', {'form':form})

def delete(request, post_pk):
  post = Post.objects.get(pk = post_pk)
  post.delete()
  return redirect('home')
  