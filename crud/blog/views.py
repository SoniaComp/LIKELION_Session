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