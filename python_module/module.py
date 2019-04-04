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
    while(b!=0):
      b = int(input())
      if b == 0 :
        print("다시 입력하세요")
  return a / b