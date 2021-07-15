# Crawling and API

- 크롤링과 API를 이용하는 방법 모두 외부 url을 통해 원하는 정보를 가져오는 것임.
- 크롤링은 개발자페이지에서 가져와야하기 때문에(복잡복잡) 데이터 전처리가 필요함.
- API를 통한 방법은 API만 가져오면 나머지는 찾기 쉬움...(추천)
- API를 통한 방법은 정보들을 거의 JSON을 통해 가져옴.(chrome JSON viewer설치하면 편함)

## 1. Crawling

1. 터미널에서 **pip install requests**를 한다.

2. **import requests**를 통해 requests를 가져온다.

3. 크롤링은 페이지가 복잡하기 때문에(str) BeautifulSoup을 이용해서 데이터 전처리를 해준다.

4. 터미널에서 **pip install beautifulsoup4**를 한다.

5. **from bs4 import BeautifulSoup**를 한다.

6. 나머지는 코드로...

   ```python
   import requests
   from bs4 import BeautifulSoup
   
   url1 = 'https://finance.naver.com/sise/'
   
   res1 = requests.get(url1)
   
   print(res1)
   # 결과는 [200] = OK! 내용을 보고 싶다면
   
   print(type(res1.text))
   # 개발자도구 페이지가 와르르
   
   # bs4로 데이터 전처리 왜? 전부 str이라서 너무 복잡하고 많아...
   selector = '#KOSPI_now'
   
   # BeautifulSoup을 통해 res.text를 html.parser한다.
   data = BeautifulSoup(res.text, 'html.parser')
   
   kospi = data.select_one('#KOSPI_now')
   
   print(kospi.text)
   
   # 네이버 시장지표 지수(실습), id는 #, class는 .
   url2 = 'https://finance.naver.com/marketindex/'
   res2 = requests.get(url2)
   
   data2 = BeautifulSoup(res2.text, 'html.parser')
   answer = data2.select_one('.value')
   print(answer.text)
   ```



## 2. API

1. 크롤링과 같은 과정이기 때문에 import requests만 해준다.

2. 크롤링과는 다르게 데이터전처리말고 json()을 한다.

3. 나머지는 코드로...

   ```python
   import requests
   
   url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=971'
   
   res = requests.get(url)
   
   #data = res.text
   
   # 눈에는 {} 때문에 dict 같지만 사실은 str이다.
   # print(type(data))
   
   # API를 통해 가져온 정보이기 때문에 데이터 전처리가 불필요함 -> res.json()을 통해 dict로 만든다.
   data = res.json()
   
   print(data['bnusNo'])
   
   ```

   

