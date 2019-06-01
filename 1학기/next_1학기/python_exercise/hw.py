'''
# 연습문제
# 리스트
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

# 별찍기
i=0
s=''
while i < 5:
  s+='*'
  print(s)
  i+=1
#아니면, print('*' * i) 이런식으로 찍어내도 된다.

# 모음찾기
s = [i for i in "mutzangesazachurum" if i in "aeiou"]
print(len(s))
'''

#1-1
# i = 1
# sum = 0
# while i<1001:
#   if i%3 == 0:
#     sum += i
#   i+=1
# print(sum)
# 값: 166833

#1-2
# i=0
# while i<10 :
#   print('*'*(10-i))
#   i += 1

#1-3
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# sum = 0
# for i in A:
#   if i>=50:
#     sum += i
# print(sum)
# # 답: 481

#2-1
# for i in range(1, 101):
#   print(i)

#2-2
# A = [70,60,55,75,95,90,80,80,85,100]
# sum = 0
# for i in A:
#   sum += i
# print(sum/len(A))
# #답: 79.0

#2-3
# result = [i*2 for i in [1,2,3,4,5] if i%2 == 1]
# print(result)
# #출력 결과: [2, 6, 10]