# Crawling and API(2)

- 데이터 수집(web에서 가져온다)
- http = 웹의 정보공유 기초
- request
- response
- 클라이언트는 서버한테 url로 정보 요청
- 서버는 클라이언트한테 문서(텍스트덩어리)로 - HTML 응답
- 검색창에 검색을 하고 엔터를 치는 행위 = url을 바꾸는 행위
- 크롤링 = 원하는 데이터를 긁어오는 것
- requests의 역할은 html을 받아오는 것까지
  => 원하는 대로 사용하기 위해서는 추가작업 필요
  => BeautifulSoup = html에서 데이터를 뽑아 주는 python라이브러리
  => pip install beautifulsoup4 

```python
import requests
from bs4 import BeautifulSoup

# 요청을 보낼 URL
url = 'https://finance.naver.com/sise/'

# 실제 요청을 보내고, 응답 객체를 response 변수에 저장
response = requests.get(url)

# 응답 객체의 본문(text)을 해석하여 data변수에 저장
# BeautifulSoup클래스를 통해 text문서를 html.parser을 가지고 해석해!
data = BeautifulSoup(response.text, 'html.parser')

# 해석한 data에서 원하는 정보를 선택하고, 내용만 kospi에 저장
kospi = data.select_one('#KOSPI_now').text

print(kospi)
```

- 크롤링의 단점
  1. 브라우저가 아닌 상황에서 필요 없는 데이터가 너무 많음
  2. 원하는 데이터를 얻기 위한 추가작업

  => API로 해결

- API server
  = 응용프로그램(개발자)를 위한 데이터를 응답하는 프로그램

- 코드밖에서 가져오는 데이터는 무조건 str이라고 생각하자

```python
import requests
from pprint import pprint


class <name>:

    def __init__(self, api_key=None):
        self.api_key = api_key
	
    # 사용하려는 API마다 다른 양식을 갖고 있기 때문에 공식문서 참조!! 
    def get_request_url(self, method='/movie/popular', **kwargs):
        base_url = '<API공식문서에 나와있는 기본틀>'
        request_url = base_url + method
        request_url += f'?api_key={self.api_key}'

        for k, v in kwargs.items():
            request_url += f'&{k}={v}'

        return request_url

    # 제목으로 영화 검색 후 검색결과에서 id를 return
    def get_movie_id(self, title):
        request_url = self.get_request_url(
            '/search/movie', query=title, language='ko', region='KR')
        # 검색결과
        data = requests.get(request_url).json()

        # get()을 사용하는 이유는 결과값이 없는 경우 keyerror대신에 none값을 받기 위해서
        results = data.get('results')
        if results:
            movie_id = results[0]['id']
            return movie_id
        else:
            return None
```



