# BeautifulSoup 모듈 import 하기
from bs4 import BeautifulSoup
# requests 모듈 import 하기
import requests

URL = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
# 변동되는 값들을 input으로 받는다.
query = input('찾고 싶은 뉴스 키워드: ')

# URL 확정
fullURL = URL + query
# HTTP 접근 -> request
data = requests.get(fullURL).text
# html 파일 형식으로 파싱을 한다.
soup = BeautifulSoup(data, 'html.parser')

# 뉴스 태그와 링크 주소를 가져옴.
# 개발자도구로 체크한다. ul > li > dl > dt > a
# a 태그로 접근해보장 --> CSS selector 클래스랑 아이디는 가지고 오고 싶은 data들의 위치를 표현해줌.
news_titles = soup.find_all(class_='_sp_each_title')# find_all이라는 메소드는 괄호 안에 있는 조건을 만족하는 아이들을 받아와서 리스트에 담아준다.
# class는 예약어(?)이므로 class_라고 적는다.

# 원하는 애들만 가져오기 --> get이라는 메서드
title_list = []
for title in news_titles:
  title_list.append({'url':title.get('href'), 'title':title.get('title')})

  