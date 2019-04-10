from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
# Create your views here.
def home(request):
  reviews = Review.objects.all()
  return render(request, 'home.html', {'reviews':reviews})

def new(request):
  if request.method == "POST":
    form = ReviewForm(request.POST)
    review = form.save(commit = False)
    form.save()
    return redirect('detail', review.pk)
  else:
    form = ReviewForm()
  return render(request, 'new.html', {'form':form})

def detail(request, review_pk):
  review = Review.objects.get(pk = review_pk)
  return render(request, 'detail.html', {'review':review})