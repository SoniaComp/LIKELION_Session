from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
def home(request):
  reviews = Review.objects.all()
  return render(request, 'home.html', {'reviews':reviews})

def new(request):
  if request.method == "Review":
    form = ReviewForm(request.Review)
    review = form.save(commit = False)
    form.save()
    return redirect('detail', review.pk)
  else:
    form = ReviewForm()
  return render(request, 'new.html', {'form':form})

def detail(request, review_pk):
  review = Review.objects.get(pk = review_pk)
  return render(request, 'detail.html', {'review':review})

def edit(request, review_pk):
  review = Review.objects.get(pk = review_pk)
  if request.method == 'POST':
    form = ReviewForm(request.POST, instance = review)
    # instance 값을 주면, 기존의 DB에 덮어쓰기를 한당!
    form.save()
    return redirect('detail', review.pk)
  else:
    form = ReviewForm(instance = review)
    # 데이터 베이스 만들어진 하나하나를 instance라고 할 수 있다.
  return render(request, 'edit.html', {'form':form})

def delete(request, review_pk):
  review = Review.objects.get(pk = review_pk)
  review.delete()
  return redirect('home')