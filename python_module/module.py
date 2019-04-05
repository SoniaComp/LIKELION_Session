def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mul(a, b):
  return a * b

def div(a, b):
  if b == 0:
    print("0으로는 나눌 수 없어욧!")
    # return "바보"
    while(1):
      print("다시 입력하세요")
      b = int(input())
      if b != 0:
        break
  return a / b