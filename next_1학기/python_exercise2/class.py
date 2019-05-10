# 계산기 class
class Fourcal:
  def __init__(self, first, second): # 메소드의 첫번째 자기 자신
    self.first = first
    self.second = second
  def add(self):
    result = self.first + self.second
    return result
  def mul(self):
    result = self.first * self.second
    return result
  def sub(self):
    result = self.first - self.second
    return result
  def div(self):
    result = self.first / self.second
    return result
'''
a = Fourcal(4, 2)
b = Fourcal(6,3)
print(a.first)
print(a.second)
print(a.mul())
print(a.sub())
print(a.div())
print(a.add())
print(b.mul())
print(b.sub())
print(b.div())
print(b.add())
'''
'''
class MoreFourCal(Fourcal):
  pass

a = MoreFourCal(4,2)
print(a.add())
# 클래스 상속이 가능하다. class 클래스명(상속하고 싶은 클래스):
# 상속한다: 상속해주는 클래스의 메소드들을 사용할 수 있다.
class ChangeFourCal(Fourcal):
  def add(self):
    result = self.first * self.second
    return result
# 메소드 오버라이딩
# 부모함수를 자식의 함수로 덮어 씌운다. (같은 명의 함수일 경우)
b = ChangeFourCal(4,2)
print(b.add())
'''

#### 질문 ####
# __init__ 디폴트 값: 객체를 만드는 순간 자동으로 실행
# 클래스 내 메소드 매개변수에는 꼭 self가 들어가야? 그냥 print 함수
# 나눗셈 형변환
'''
# 파이썬 변수 선언을 메소드 내에서 함! No!!
클래스 안에는 모든 형태가 들어갈 수 있어요. 함수, 문자형, 리스트형, 클래스
모든 걸 다 객체로 본당!
'''

# 2. 클래스 변수
class Family:
  lastname = "박"
print(Family.lastname) # 클래스 명은 클래스명.클래스변수로 접근 가능

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

class newFamily(Family):
  lastname = "김"

c = newFamily()
print(c.lastname)