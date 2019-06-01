# beautiful soup은 정적인 페이지만 가져온다.
# selenium: 동작을 해서 가져오고 싶을 때 사용! Ex) 더보기란, 몇초전 등록된 글
# selenium automates browsers.

# pipenv install selenium
# chrome webdriver 설치: chrome://chrome --> 크롬 버전 올려주기
# 버전이 다를 경우 실행되지 않음.

from selenium import webdriver
# 드라이버 안에서 동작할 수 있게끔, 버튼을 파이썬이 인식할 수 있도록 도와주는 패키지
# 웹드라이버는 페이지를 직접 실행해준다.
from selenium.webdriver.common.keys import Keys
# time은 내장되어 있는 것
# sleep: 컴퓨터 반응이 너무 빠르기 때문에 동작
from time import sleep

#url = 'https://search.naver.com/search.naver?where=realtime&sm=tab_jum&query='
word = input('실시간 검색 키워드: ')

# web driver 패키지에 실행하라는 명령어를 변수에 저장해보다.
# chrome driver를 다운로드 받았으므로 chrome('안에는 위치를 적어줌')
# exe는 확장자 이므로 붙여주지 않아도 된다.
driver = webdriver.Chrome('./chromedriver')
# driver.get(url+word)
# f를 붙여주는 이유는 한글도 인식하게 하기 위해서이다.
driver.get(f'https://search.naver.com/search.naver?where=realtime&sm=tab_jum&query={word}')

# 더보기 버튼을 세번 누를 후 결과를 가져와라!
# 더보기를 누르는 버튼의 위치를 알려주는 방법 --> 위치를 알려주는 css selector을 이용하면 된다.

more_button = driver.find_element_by_class_name('_moreBtn')
# class name으로 불린 것을 찾아라. 그리고 more 버튼에 저장해라.
# p_more

'''
more_button이 있을 때까지만 눌러라! 라는 코드를 넣으면 좋을 듯
while(more_button!=NULL)이렇게
'''
for _ in range(3):
  more_button.click() # more_button을 클릭해라.
  # Keys라는 애 안에 click이 있음.
  # sleep 안에는 초를 써주면 된다.
  sleep(2)

# 가져와서 담을 보따리 이름
tweets = driver.find_elements_by_css_selector('#realTimeSearchBody > div.rt_wrap.rt_typ2 > div:nth-child(1) > ul:nth-child(1) > li > dl > dd:nth-child(2) > a')
# 다른 애들이랑 분리할 수 있을 정도까지 올라간다.
# nth-child --> 몇번째 자식 안에 있는지!! (1)부터 시작 << class 명이 없을 때 사용하는 선택자
# 리스트로 반환해주는 css_selector --> 동일한 어미요소를 찾고, 몇번째 인지 찾으면 된다.
# 리스트로 반환해주니까 관련된 li를 쭉 가져와서 뿌려준다.

# 담은 보따리에 있는 text만을 가져오자.
'''
texts = []
for tweet in tweets:
  texts.append(tweet.text)
'''
# 위에 거를 더 짧게 써보자.
texts = [tweet.text for tweet in tweets]


with open('result.txt', 'w', encoding = 'utf-8') as f:
  for text in texts:
    f.write(text+'/n')
# result.txt를 만들고 열어서 거기다 써라!

# 드라이버를 끄는 명령어
driver.quit()