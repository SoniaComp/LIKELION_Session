'''
1. 조건문
비교연산자, 논리연산자

number1 = 100
number2 = 200
number3 = 300
number4 = 400

a = number1>number2 #F
b = number3<number4 #T

if a:
  print('True')
else:
  print('False')

if a and b:
  print('True')
else:
  print('False')
'''

'''
유용한 if문: x in s!!!
있는지, 없는지... 파이썬에서만 제공하는 아주 유용한 친구

list1= ['a','b']

if 'a' in list1:
  print('a가 있습니다.')
else:
  if 'b' in list1:
    print('b가 있습니다.')
  else:
    print('둘 다 없습니다.')

if 'a' in list1:
  print('a가 있습니다.')
if 'b' in list1:
  print('b가 있습니다.')
else:
  print('a와 b가 모두 없습니다.')
'''

'''
pass는 조건문에서... 실행문을 실행하지 않고 그냥 넘어갈 때
continue는 반복문에서... 반복문을 벗어날 때

list1 = ['a', 'b']

if 'a' in list1:
  pass
else:
  print('a가 없습니다.')

# 한 줄로 만들기
if 'a' in list1:
  print("있습니다.")
  print("진짜!!!")
else:
  print("없습니다.")

######## 세미콜론을 쓰면 한 줄로 만들 수 있음
if 'a' in list1: print("있습니다."); print("진짜!!!")
else: print('없습니다.')
'''

'''
while <조건문>:
  실행문1
  실행문2

treeHit = 0
while treeHit < 10:
  treeHit = treeHit + 1
  print("나무를 %d번 찍었습니다." %treeHit) #파이썬에서 print를 하는 신박한 방법
  if treeHit == 10:
    print("나무 넘어갑니다.")
'''

'''
문자 포매팅
a. 일반 문자 --> input: %s value: %문자
b. 변수형 문자
  %s: 문자열
  %d: 정수형
'''

'''
while True:
  실행문 #실행문이 계속 돈다.
  if 조건문:
    break #여기서 강제 종료 --> 무한루프 방지.. return도 같은 개념으로 쓰이기도 함.
    continue #다시 while로 돌아가게 됨. 뒤에 부분 실행하지 않고 바로 while로 돌아감

num1 = 0
while num1<10:
  num1 +=1
  print(num1)
  if num1 == 5:
    break

num2 = 0
while num2<10:
  num2 +=1
  if num2%2 ==0:
    continue
  print(num2)

i=0
s=''
while i < 5:
  s+='*'
  print(s)
  i+=1
#아니면, print('*' * i) 이런식으로 찍어내도 된다.
'''

'''
for 변수 in list(튜플, 문자열)

list1 = [1,2,3,4,5,6,7,8,9,10]
for i in list1 :
  print(i)
  if i == 5:
    break

list2 = [1,2,3,4,5,6,7,8,9,10]
for i in list2: # i는 for문안에서만 쓰일 수 있는 아이
  if i%2 == 0: continue
  print(i)

#리스트는 매번 설정하기 번거로우므로 for문은 range함수(숫자 리스트를 자동으로 만들어줌)를 사용
#range(start, stop, step)
#위와 같은 형태로 표현되고, default는 +1, 마지막 값은 포함이 되지 않습니다.
'''

'''
List Comprehension

a = [1,2,3,4]
result = []
for num in a:
  result.append(num*3)
print(result)

# 리스트 안의 for문 이용
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)

# [1,2,3,4] 중에서 짝수인 2와 4에만 3을 곱하여 담고 싶다면..
a = [1,2,3,4]
result = [num*3 for num in a if num%2 == 0]
print(result)

조금 복잡하지만 for문을 2개 이상 사용하는 것도 확인
[표현식 for 항목 in 반복가능객체 if 조건문]
[표현식 for 항목 in 반복가능객체 if 조건문1
      for 항목2 in 반복가능객체 if 조건문2]
'''

s = [i for i in "mutzangesazachurum" if i in "aeiou"]
print(len(s))

# for i in [1,2,3]:
#  for j in [2,3,4]:  