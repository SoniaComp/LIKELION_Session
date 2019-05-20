import requests, xmltodict
# xml to dict: xml을 dictionary 형태로 바꾸어줌! 

raw_data = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?serviceKey=bNxdoE622ngG%2BcPy1fae0tQySPMniJY3GmLFmOygb5btvjmqbGRDHsez1eazNuomQPeDUh3nWIfpLr9HwJWGVw%3D%3D&numOfRows=10&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&searchCondition=DAILY'
data = requests.get(raw_data).content
xmlObject = xmltodict.parse(data)
dataShown = xmlObject['response']['body']['items']['item']

for data in dataShown:
  print(data['dataTime'][0:10]+" 기준 "+data["cityName"]+"의 대기")
  print("이황산가스 농도: "+data['so2Value'])
  print('------------------------------')