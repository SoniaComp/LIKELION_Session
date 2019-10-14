from django.shortcuts import render

# Create your views here.
def home(request):
  if request.method == "POST":
    res = render(request, 'home.html')
    res.set_cookie('ck', request.POST.get('ck'))

    return res
  else:
    print(request.COOKIES.get('ck'))
    
    return render(request, request.POST.get('ck'))