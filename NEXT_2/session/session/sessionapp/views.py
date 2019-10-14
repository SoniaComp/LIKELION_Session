from django.shortcuts import render
from django.core.exceptions import PermissionDenied
# Create your views here.
def home(request):
  return render(request, "home.html")

def step1(request): 
  # Step1에 온 사용자의 세션을 만든다.
  request.session['step1_complete'] = True

  return render(request, "step1.html")

def step2(request):
  if not request.session.get('step1_complete', False): # 값이 없음 False, 값이 있으면 그 값을 리턴
    raise PermissionDenied

  return render(request, "step2.html")