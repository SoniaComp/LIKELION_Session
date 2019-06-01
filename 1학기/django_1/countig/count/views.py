from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')

def result(request):
  print(request)
  text = request.GET['fulltext']
  textcount = len(text)
  #
  splitted_text = text.split()
  text2 = "".join(splitted_text)
  #
  text2count = len(text2)
  return render(request, 'result.html',{
    'text' : text,
    'textcount' : textcount,
    'text2count' : text2count
  })