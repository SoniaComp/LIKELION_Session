import requests
# 인터넷 http로 접근할 수 있는 패키지
import json

def news_json():
  apiKey = "apiKey=a655f1752ddf4ff485ffa19b2500a630"
  url = "https://newsapi.org/v2/top-headlines?country=kr&" + apiKey
  newsDummy = requests.get(url).json()
  # 파이썬에서 딕셔너리 접근하는 방법
  articles = newsDummy["articles"]

  articlesSorted = [{"source_name": article["source"]["name"], "author": article["author"], "title": article["title"], "url": article["url"], "urlToImage":article["urlToImage"]} for article in articles]

  return articlesSorted
