from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')

def result(request):
  text = request.GET['fulltext']
  splitted_word = text.split()
  all_word = "".join(splitted_word)
  # 딕셔너리로 저장
  # len은 template에서 |length 사용 보다는 view에서 계산을 권장
  word = {}
  for i in splitted_word:
    word[i] = len(i)

  return render(request, 'result.html', {
    "length" : len(all_word),
    "text" : text,
    "word" : word
  })