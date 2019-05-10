# 함수의 종류는 4가지가 있습니다.

# 1. 입력값이 몇개가 될 지 모를 경우

# 2.
# 튜플은 파이썬의 독특한 특징
# 입력하는 모든 값들을 더해서 돌려주세요!
# 매개변수명 앞에 *를 붙이면 입력값들을 모두 모아서 튜플로 만들어줍니다.
'''
def add_many(*args):
  result = 0
  for i in args:
    result = result + i
  return result

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)
'''
# 3. 매개변수 앞에 **을 붙이면 출력을 딕셔너리 형태로!
# 인수는 key = value의 형태

# 4. scope in function
# 함수 안에서 사용하는 변수의 효력 범위는 함수를 벗어나지 않는다.

############# 입력 #############
# 1. 입력
'''
a = input()
print(a)
# 사용자에게 입력을 받을 때 "숫자를 입력하세요," "이름을 입력하세요."라는 안내 문구 또는 질문.
#input("질문 내용")
number = input("number? ")
print(number)
'''

# 클래스
# 용어정리: 매개변수, 인수
# 용어정ㄹ: 객체(Object), 인스턴스(Instance)