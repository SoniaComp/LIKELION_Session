import mod2 #import 모듈 이름
# from mod import add # from 모듈 import 함수
# 모듈에서 함수 뿐 아니라 변수, 클래스도 다 불러올 수 있다.
# from mod import add, sub: 여러개의 함수 동시 호출 가능
# from mod import *: 해당 모듈의 모든 '함수' 호출

# 모듈, 해당 모듈의 함수로 해당 모듈의 함수를 불러올 수 있음.
# 파이썬 라이브러리가 저장된 디렉토리에 있는 모듈만 불러올 수 있다. ex) sort 모듈

print(mod2.PI)

a = mod2.Math()
print(a.solv(2))

# 패키지: 파이썬의 모듈을 계층적(디렉터리 구조)로 관리하는 방식
# 파이썬 프로그램을 만드는 것이 공동작업이나 유지 보수 등 여러 면에서 유리하다.