# Django[2021.10.25] - RESTful API



## 1. HTTP

- Hyper Text Transfer Protocol

- 웹상에서 컨텐츠를 전송하기 위한 약속(규칙)

  - request = 클라이언트에 의해 전송되는 메시지
  - response = 서버에서 응답으로 전송되는 메시지

- 상태와 연결이 존재하지 않음(Stateless, Connectless)

  -> 쿠키와 세션을 통해서 연결상태처럼 만들어줌

- HTTP request methods

  - 주어진 리소스에 수행하길 원하는 행동
  - GET(R), POST(C), PUT(U), DELETE(D)
  - 앞으로는 url에 직접 verb로 표현하지 않고 HTTP request methods사용!!

- HTTP response status codes

  - Informational responses(1xx)
  - Successful responses(2xx)
  - Redirection responses(3xx)
  - Client error responses(4xx)
  - Server error responses(5xx)

- 리소스란?

  - HTTP요청의 대상을 리소스라고 함
  - 문서, 사진 등이 될 수 있음
  - URI에 의해 식별

- URI(Uniform Resource Identifier)

  - URL(Uniform Resource
    - 통합 자원 위치
    - = 링크
    - 네트워크 상 어디에 있는지 위치를 나타내줌
  - URN(Uniform Resource Name)
    - 통합 자원 이름
    - 고유한 이름(ISBN과 비슷)
    - 잘안씀
  - 구조
    - scheme
      - 프로토콜
      - hrrps, http, data, file, ftp, malito
    - host
      - 요청받는 웹 서버의 이름
      - 도메인주소
    - port
      - 웹 서버 상의리소스에 접근하는데 사용되는 문
      - http : 80
      - https : 443
    - path
      - 웹 서버 상의 리소스 경로
      - 오늘날은 실제 위치가 아닌 추상화적인 형태의 구조로 표현
    - query
      - 웹 서버에 제공되는 추가적인 매개 변수
      - &로 구분되는 key-value
    - fragment
      - anchor
      - 자원 안에서 북마크
      - `#`형태



## 2. RESTful API

- API(Application Programming Interface)
  - 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스
  - 애플리케이션과 소통하는 방법임
  - 응답 데이터 타입
    - JSON, HTML, XML
- REST(REpresentational State Transfer)
  - API server를 개발하기 위한 일종의 소프트웨어 설계 방법론
  - REST의 자원과 주소 지정 방법
    1. 자원
       - URI
    2. 행위
       - HTTP methods
    3. 표현
       - 자원과 행위를 통해 궁극적으로 표현되는 결과물
       - JSON으로 표현된 데이터를 가공
- JSON(JavaScript Object Notation)
  - 파이썬의 딕셔너리
  - 자바스크립트의 object
  - key-value형태



## 3. Response

- HTML을 응답하는 서버 => 기존의 project(templates/articles~.html)

- JsonResponse

  - ```python
    # views.py
    
    from rest_framework.decorators import api_view
    from rest_framework.response import Response
    from django.shortcuts import render
    from django.http.response import JsonResponse, HttpResponse
    from django.core import serializers
    from .serializers import ArticleSerializer
    from .models import Article
    
    # 기존의 HTML로 response
    def article_html(request):
        articles = Article.objects.all()
        context = {
            'articles': articles,
        }
        return render(request, 'articles/article.html', context)
    
    # Json으로 response - 직접 JSON객체 구성
    def article_json_1(request):
        articles = Article.objects.all()
        articles_json = []
    
        for article in articles:
            articles_json.append(
                {
                    'id': article.pk,
                    'title': article.title,
                    'content': article.content,
                    'created_at': article.created_at,
                    'updated_at': article.updated_at,
                }
            )
        # dict이외의 객체를 직렬화(Serialization)하려면 safe=False설정!!!(articles_json = list)
        return JsonResponse(articles_json, safe=False)
    
    
    def article_json_2(request):
        articles = Article.objects.all()
        data = serializers.serialize('json', articles)
        return HttpResponse(data, content_type='application/json')
    
    #########################################################################################
    # $ pip install djangorestframework 를 이용한 방법
    # @api_view(['GET'])
    @api_view()
    def article_json_3(request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    ```

- Serialization(직렬화)

  - 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고 나중에 재구성할 수 있는 포맷으로 변환하는 과정

    -> QuerySet -> serialize -> JSON으로 쉽게 변환할 수 있는 python 데이터타입 형태로 바꾸는 행위 

  - ```python
    # serializers.py
    
    from rest_framework import serializers
    from .models import Article
    
    # form.py와 거의 같음
    class ArticleSerializer(serializers.ModelSerializer):
    	
        # Article에 해당하는 요소들을 자동으로 JSON형태로
        class Meta:
            model = Article
            fields = '__all__'
    ```

  - JSON으로 보낸 데이터를 가져오기

    ```python
    # ssafy.py
    
    import requests
    from pprint import pprint
    response = requests.get('http://127.0.0.1:8000/api/v1/json-3/')
    # pprint(type(response.json()))
    
    data = response.json()
    
    pprint(data[0])
    ```

- django ModelForm vs DRF Serializers

  ![3](https://user-images.githubusercontent.com/73927750/138643164-e14b6501-539e-4a8e-9c88-4f95be539d65.JPG)



## 4. Single Model

- 단일 모델의 data를 직렬화하여 JSON으로 변환하는 방법

- ```python
  # serializers.py
  
  from rest_framework import serializers
  from .models import Article
  
  
  class ArticleListSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Article
          fields = ('id', 'title',)
  
  
  class ArticleSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Article
          fields = '__all__'
  ```

- ModelSerializer을 이용하면

  1. 모델 정보에 맞춰 자동으로 필드 생성
  2. serializer에 대한  유효성 검사기를 자동으로 생성(is_valid())

- 'many' argument

  ```python
  serializers = ArticleListSerializer(articles, many=True)
  # many=True를 해야 여러개를 직렬화할 수 있음
  ```

- build RESTful API

  ![4](https://user-images.githubusercontent.com/73927750/138644451-aafe41ce-283c-4989-b10b-37c3b50a5e00.JPG)

- api_view decorator

  - 허용할 수 있는 method를 제한할 수 있는 decorator
  - DRF에서는 반드시 작성해야함!!!

- RESTful API를 활용한 views.py

  ```python
  # views.py
  
  import re
  from django.shortcuts import render, get_list_or_404, get_object_or_404
  
  from rest_framework.response import Response
  from rest_framework.decorators import api_view
  from rest_framework import status
  
  from .models import Article
  from .serializers import ArticleListSerializer, ArticleSerializer
  
  
  @api_view(['GET', 'POST'])
  def article_list(request):
      # 전체 게시글 조회
      if request.method == 'GET':
          articles = get_list_or_404(Article)
          serializers = ArticleListSerializer(articles, many=True)
          return Response(serializers.data)
  
      # 게시글 생성
      elif request.method == 'POST':
          serializers = ArticleSerializer(data=request.data)
          if serializers.is_valid(raise_exception=True):
              serializers.save()
              return Response(serializers.data, status=status.HTTP_201_CREATED)
          # return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
  @api_view(['GET', 'DELETE'])
  def article_detail(request, article_pk):
      article = get_object_or_404(Article, pk=article_pk)
  
      if request.method == 'GET':
          serializer = ArticleSerializer(article)
          return Response(serializer.data)
  
      elif request.method == 'DELETE':
          article.delete()
          data = {
              'delete': f'데이터{article_pk}번이 삭제 되었습니다.'
          }
          return Response(data, status=status.HTTP_204_NO_CONTENT)
  ```

- Status Codes in DRF

  - status 모듈에 HTTP status code 집합이 모두 있음

- 결론

  - RESTful API 형태로 개발 => 기존의 templates 처럼 하나하나 html을 꾸미지 않고 Back-End에서는 JSON객체만 넘겨 주고 끝내겠다! => 꾸미는 것은 Front-End에서 해결!

  - serializers.py를 통해서 간단하게 원하는 요소들을 JSON형태로 변환

  - 기존에는 views와 urls에 함수들이 기능별로 존재함 => urls이 복잡해짐

    -> 하지만 HTTP request methods를 통해 적은 개수의 url로 다양한 기능을 구현할 수 있음(깔끔!)
    
  - RESTful - URL을 잘 짜서 (URL, HTTP verb를 분리)
  
  - API서버 - 꾸밈없이 데이터만(JSON) 제공하는 서버를 만들자 
