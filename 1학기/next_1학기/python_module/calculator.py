from module import *

print("Menu\n------------------\n1: add\n2: sub\n3: multiply\n4: divide\n5: finish")


while(1):
  print("메뉴를 선택하세용!")
  op = int(input(":"))
  if op == 5:
    break
  elif op not in [1,2,3,4]:
    print("Wrong number. Please write number agin.")
    continue
  num1 = int(input("num1:"))
  num2 = int(input("num2:"))
  if op == 1:
    result = add(num1, num2)
  elif op == 2:
    result = sub(num1, num2)
  elif op == 3:
    result = mul(num1, num2)
  elif op == 4:
    result = div(num1, num2)
  print(result)
