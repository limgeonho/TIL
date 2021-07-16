# Chatbot Programming

> 요청은 url로 응답은 텍스트 덩어리(str)이다.

## 1. GET / POST 방식

- GET : 데이터베이스에 바뀌는 내용이 없음, 그저 내가 원하는 정보를 가져올 뿐...(서류출력)
- POST : 내가 직접  데이터를 전달함 -> 데이터 베이스에 변경사항이 생김.(전입신고)

## 2. 클라우드 컴퓨팅

- 내 컴퓨터를 24시간동안 켜놓을 수 없음 => 어딘가에 존재하는 임의의 컴퓨터를 빌려서 원격 사용함.
- AWS가 가장 유명함. 실습에서는 pythonanywhere 사용

## 3. 클라이언트 / 서버

- 요청을 하는 모든 존재를 통틀어서 = 클라이언트
- 응답을 하는 모든 존재를 통틀어서 = 서버
- 서버와 클라이언트는 고정된 것이 아니라 매 순간 정보의 이동 방향에 따라 가변적임.
- 1. 내가 텔레그램(챗봇)에 메세지를 보내면 : 나(클라) - 텔레(서버)
  2. 텔레그램(챗봇)이 나한테 답을 한다(메세지를 로컬로 전달해줌) :  텔레(클라) - 나(서버)

## 4. IP주소 / 도메인

- IP주소는 구체적인 주소임, 인천광역시 부평구 ~~ 와 같은 맥락(누구나 찾을 수 있음)
- 도메인은 기억하기 쉬운 대표적인 주소임, 역삼 멀티캠퍼스(서로 아는 사람들끼리만 이해O)
- 127.0.0.1(IP주소) - 우리집(도메인)

## 5. 백도어 프로그램

- ngrok 사용함
- 내 컴퓨터는 방화벽 때문에 외부에서 접근할 수 없다 => ngrok를 통해 전달 받은 임의의 주소로 우회해서 내 컴퓨터(로컬)에 접근 가능.

## 6. Chatbot 

- naver 검색 OpenAPI를 활용

- 텔레그램 챗봇 만들기 활용

- 하나의 일의 단위는 function으로 만들어서 활용

  

  1. 네이버 API 활용

```python
import requests

def search_shopping(keyword):
    url = f'https://openapi.naver.com/v1/search/shop.json?query={keyword}'

    naver_client_id = <네이버 클라이언트 아이디>
    naver_client_secret = <네이버 클라이언트 비밀번호>

    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret,
    }

    # GET요청을 보내고 url과 headers도 함께 보낸다. => API결과 값이 return한다.
    res = requests.get(url, headers=headers).json()

    # 금액, 제품명, 링크까지 return하고 싶다...
    # 답은 리스트, str, 여러가지가 있지만 그나마 현실데이터와 가장 비슷한 dict구조로 하자
    item = res['items'][0]
    result = {
        'price': int(item['lprice']),
        'name': item['title'],
        'link': item['link'],
    }

    return result
    # pprint는 json을 통해서 dict로 반환된 데이터를 좀 보기 편하게 해줌
    # return (res['items'][0]['lprice'])


# 다른 곳에서 import했을 때 자동 실행 안되게 하는 방법(아래)
if __name__ == '__main__':

    print(search_shopping('ps5'))  # => 801210

```

2. 텔레그램(챗봇) 만들기 

```python
import requests

def send_message(chat_id, message):
    token = <챗봇 토큰값>

    # 메세지 보내기
    url = f'https://api.telegram.org/bot{token}/sendMessage?text={message}&chat_id={chat_id}'

    res = requests.get(url).json()

if __name__ == '__main__':
    send_message(12345678, 'hi')  # => hi가 전송됨.

```

3. 

```python
from flask import Flask, request
import naver
import telegram
# 이미 만들어 놓은 naver파일에 있는 함수를 이용할 수 있다.
# naver.search_shopping('ps5')

# 다른곳에서 만든 함수들을 불러와서 역할분담을 시킨다. = 모듈화
# data = naver.search_shopping('ps5')

# msg = f"{data['name']}의 가격은{data['price']:,}원, \n{data['link']}"

# telegram.send_message(msg)

app = Flask(__name__)

# 언제 할건데? 아무때나 할 건 아니잖아..콜센터 처럼 할 수 있는 일을 매핑해줘야함
# 127.0.0.1:5000/a로 요청 => def hello()로 요청이 들어오고 => 다시 응답(브라우저로)

@app.route('/')
def index():
    print(request)
    return 'Hello!'

@app.route('/receive', methods=['POST'])
def receive():
    data = request.get_json()
    chat_id = data['message']['chat']['id']

    msg = data['message']['text']

    telegram.send_message(chat_id, msg)
    return 'ok', 200

@app.route('/send')
def hello():
    data = naver.search_shopping('ps5')

    msg = f"{data['name']}의 가격은{data['price']:,}원, \n{data['link']}"

    telegram.send_message(msg)

    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)

```

