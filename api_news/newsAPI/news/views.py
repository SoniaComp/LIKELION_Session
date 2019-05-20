from django.shortcuts import render
from .modules import news_json

# Create your views here.
def home(request):
  articles = news_json()
  return render(request, 'home.html', {'articles':articles})