# 한줄 주석 처리입니다.

"""
여러줄 
주석
처리입니다.
"""

'''
작은 따옴표도
할 수 있습니다. :)
'''

# ㅇㄹㅇㄹ
# ㅇㄹㅇㄹ
# command + ? : 드래그 후 한꺼번에 주석처리

'''
1. 숫자형
정수
실수
8진수&16진수

a = 15
print(a)
# 터미널에서 확인 가능!!

b = 15.5
print(b)
'''

'''
2. 사칙연산

c = 11
d = 5
print(c+d)
print(c-d)
print(c*d)
print(c/d)
print(c//d) # 몫만 출력
print(c%d) # 나머지만 출력
'''

'''
3. 문자형

str1 = "hello"
str2 = "world"

print(str1, str2) # , 로 하면 자동 띄어쓰기
print(str1 + str2)
print(str1 * 3)
'''

'''
4. 이스케이프 문자
\n == 엔터키
\t == tab키
\\
\"
\'

print("오늘 강의는 "+"\'파이썬\'"+ "\n입니다.")
'''

'''
5. 문자열
## 문자열도 리스트의 일종이다.
## 따라서 문자열도 똑같이 인덱싱, 슬라이싱이 된다.

text = "hello, world"
#인덱싱
print(text[0])
print(text[1])
#슬라이싱
print(text[0:5])
'''

'''
6. 불 자료형

a = True
b = False
c = 1<3
print(c)
d = 1>3
print(d)
'''

'''
7. 리스트

리스트 뽀인트.. 인덱스!!!
우리가 배운 모든 자료형을 리스트 안에 넣을 수 있디.

list1 = ['hello', 'python', 'java', 'c++', [1,2,3]]
print(list1[0])
print(list1[0:2])
print(list1[4][0])

#리스트의 연산
list2 = [1, 2]
list3 = [3, 4]
print(list2+list3)
print(list3*3) # 결과: [3, 4, 3, 4, 3, 4]

#수정

#삭제
listB = ['a', 'b', 'c']
del listB[0]
print(listB[0])

#삽입
listC = ['a', 'b', 'c']
listC.append('d')
print(listC)

list에는 내장함수가 짱 많다!! 구글링을 해랏!
리스트는 인덱스가 있고, 수정, 삭제, 삽입이 가능한 자료형이다.

# 연습문제 1
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)
'''

'''
8. 튜플
(): 수정, 삭제, 삽입이 불가능(리스트와의 차이점))
'''

'''
9. 딕셔너리
key: 변하지 않는 값, 리스트는 들어갈 수 없다(튜플은 가능)
value: 변하지 않는, 변하는 값 모두 사용 가능, 모든 자료형이 가능

print(dic1)

# Key를 사용하여 value 얻기
print(dic1['이름'])
print(dic1['나이'])

dic1 = {'이름':'홍길동', '나이':22, '학교':'고려대학교'}
# 키 모음(객체로 존재: dict_keys, dict_values, dict_items)을 list 형태로 전환
# key, value 리스트 얻기
keylist = list(dic1.keys())
keylist2 = dic1.keys()
print(keylist)
print(keylist2) #dict_keys가 출력이 된다.
valuelist = list(dic1.values())
print(valuelist)

# key, value 쌍을 튜플로 만들기
keyvalue = list(dic1.items())
print(keyvalue)
'''

'''
10. set 자료형
<<< 중복을 제거할 때 많이 사용한다. >>>
순서 관계 없음 --> 인덱싱 사용할 수 없음.
(리스트, 튜플로 형변환하면 인덱스 기능을 사용할 수 있다.)

list1 = ['1','2','3','4','5','1','2','3']
print(list1)
setNum = set(['1','2','3','4','5'])
print(setNum)

# 집합의 생성
# set([요소1, 요소2, 요소3])
# set을 직접 선언하는 일보다, list를 set으로 변환하는 경우가 더 많다.
setNumber = set([1,2,3,4,5])
print(setNumber)

setstr = set(['1','2','3','4','5'])
print(setstr)

setstr2 = set('Good Morning')
print(setstr2)

#인덱스를 사용하려면, 튜플 또는 리스트 형식으로 변경 후 사용
setNum = set([1,2,3,4])
print(setNum)
list2 = list(setNum)
print(list2)
tuple1 = tuple(setNum)
print(tuple1)

# set자료형은 집합
# 차집합(-), 교집합(&), 합칩합(|), 대칭차집합(^)(교집합을 제외한 나머지 부분 다)
'''

