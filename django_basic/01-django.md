# Django[2021.08.31]

## 1. 서버프로그래밍이란?

- web framework

  => 틀, 일의 흐름이 짜여져 있음

  => you can focus on writing your app without needing to reinvent the wheel.

- static web page(정적 페이지)

  - 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
  - 서버는 추가적인 처리 과정 필요 X, 단순 전달
  - flat page라고도 함
  - 일반적으로 html, css, js로 작성되어 있음
  - 모든 상황에서 모든 사용자에게 동일한 정보를 보여줌

- dynamic web page(동적 페이지)

  - 웹 페이지에 대한 요청을 받고 추가적인 처리 과정 이후 응답을 보냄
  - 페이지 내용은 그때그때마다 다름
  - 서버 사이드 프로그래밍언어사용(python, java, c++)

- framework를 사용하는 이유

  1. 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적임 
  2. 이용하지 않으면 그냥 처음부터 끝까지 다 만들어야함 ㅂㄷㅂㄷ
  3. 빠른 속도로 개발할 수 있음



## 2. framework architecture

- MVC design pattern(model-view-controller)
  - 디자인 패턴 중 하나(디자인 패턴이란? 지금까지 많은 시행착오 중 최적이라고 생각하는 정형화된 패턴)
  - 장고에서는 MTV pattern이라고 함
  - MVC == MTV
- MTV pattern
  - model-template-view == model-view-controller에 대응
  - model == db
  - template == html
  - view == db와 html에서 중간관리
- Flow
  - http request -> URLS(urls.py) -> View(views.py)(Model과 Template와 상호작용) -> http response
  - ![MTV](https://user-images.githubusercontent.com/73927750/131532945-0240fcbd-a764-474a-a117-d23fd95b56b9.JPG)



## 3. Django

- $ pip install django == 장고 설치

- $ django-admin startproject `<pjt name>` == 장고 프로젝트 만들기

- $ python manage.py runserver == 장고 서버 실행

- 장고 내부 파일

  - manage.py == 집사같은 존재

  - `<pjt name>`과 같은 이름의 폴더 == master app

  - 또 다른 app1, app2, app3 ... 

    -> $ python manage.py startapp `<app name>`으로 생성 -> setting.py -> INSTALLED_APPS = ['`<app name>`'을 등록한다] == 출생신고

- /`<pjt name>`/urls.py

  - 외부 url request가 들어왔을 때 가장 먼저 url을 처리하는 곳(장고의 눈같은 존재)

  - url이 들어오면 해당 url에 맞는 일을 처리한다 -> 함수

  - ```python
    # urls.py
    from django.contrib import admin
    from django.urls import path
    
    from django.http.response import HttpResponse
    
    def hello(request):
        html = '<h1>Hello!</h1>'
        return HttpResponse(html)
    
    urlpatterns = [
        # 요청받은 url의 뒷부분
        path('admin/', admin.site.urls),
        # url/hello/가 왔을 경우 hello함수를 실행
        path('hello/', hello)
    ]
    ```

  -  urls.py에서는 url만 처리하고 나머지 기능은 view.py로 역할분담

  - ```python
    # urls.py
    from . import views
    
    urlpatterns = [
        path('hello/', views.hello)
    ]
    
    # views.py == controller
    from django.http.response import HttpResponse
    
    def hello(request):
        html = '<h1>Hello!</h1>'
        return HttpResponse(html)
    ```

  - 지금 까지 views.py로 나눈 것들을 다시 `<app name>`으로 포워딩

    -> ~/first_app, ~/second_app, ~/third_app 처럼 큰 분류로 또 나눌 수 있음 == 효율적으로 url 관리

    ->  $ python manage.py startapp `<app name>`으로 app 생성 후 INSTALLED APP에 등록

  - from django.urls.conf import include를 통해서 포워딩

  - ```python
    # urls.py
    from django.contrib import admin
    from django.urls import path
    from django.urls.conf import include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        # first_app으로 시작하면 first_app.urls.py로 포워딩(include를 import해줘야함)
        path('first_app/', include('first_app.urls')),
    
    ]
    
    # first_app/urls
    from django.urls import path
    from . import views
    
    urlpatterns = [
        # first_app/ + hello
        # url안에 <>처리를 하면 <>안은 변수 처리된다.
        path('hello/<name>/', views.hello),
        path('lunch/', views.lunch),
        path('lotto/', views.lotto),
    ]
    ```

  - first_app/urls.py안에 있는 path('lunch/', views.lunch)는 first_app안에 존재하는 views.py에 있는 lunch 함수를 실행하겠다는 의미

  - first_app/views안에 있는 render함수를 통해서 render함

  - render(request, `<html파일>`, context(dict))으로 `<html파일>`로 전달

  - 이때 html파일은 반드시 first_app안에 있는 templates에 위치해야한다.  

    ```python
    # first_app/views
    from django.shortcuts import render
    import random
    
    def lunch(request):
        menus = ['백반', '샌드위치', '짜장면', '굶기']
        menu = random.choice(menus)
        # render(request, html파일, context(dict))
        context = {
            'menu': menu,
            'name': 'geonho',
        }
        return render(request, 'first_app/lunch.html', context)
    ```

  - ```html
    # first_app/templates/first_app/lunch.html
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      <h1>오늘의 {{ name }}의 점심 메뉴는?</h1>
    
      <h2>{{ menu }}</h2>
    </body>
    </html>
    ```

  - render()로 전달한 context를 html에서 전달받는 방법

    -> DTL(django templates language)이용

  - ```html
    DTL 형식
    -> for, if과 같은 반복, 조건문 사용가능
    -> python과 비슷해보이지만 완전 다른 것임
    1. {{ name }} -> 전달받은 name을 print
    2. {% for in %}
       {% endfor %}
    3. {% if  %}
       {% else %}
       {% endif %}
    
    {% if name == 'admin' %}
        <h2>관리자님 어서오십시오.</h2>  
    {% elif name == 'manager' %}
        <h2>매니저님 어서오세요.</h2>
    {% elif name == 'staff' %}
        <h2>스태프님 하이요.</h2>
    {% else %}
        <h2>일반인 어서오고.</h2>
    {% endif %}
    ```

- variable routing

  - hello/`<name>`/ == 처럼 url에 입력된 값을 변수에 저장해서 views의 함수에 전달할 때..

  - ```python
    # first_app/urls
    from django.urls import path
    from . import views
    
    urlpatterns = [
        # first_app/ + hello
        # url안에 <>처리를 하면 <>안은 변수 처리된다.
        path('hello/<name>/', views.hello),
        path('lunch/', views.lunch),
        path('lotto/', views.lotto),
    ]
    
    
    #  first_app/views
    
    # urls.py의 urlpattern안에 있는 'hello/<name>/'의 name변수명과 def hello(request, name):의 name을 맞춰줘야한다. == variable routing
    # -> url에서 받아온 name을 context에 전달가능 -> html로 render
    def hello(request, name):
        # 이름을 URL을 통해 받는다.
        # hello/geonho/
        context = {
            'name': name,
        }
        return render(request, 'first_app/hello.html', context)
    
    ```

- 따라서, url -> view -> template 순으로 작성

- render함수의 특징

  - render함수는 html을 render할 때 각각의 app에 있는 templates에 존재하는 모든 html파일들을 하나도 모아서 가져온다.

    -> 하지만 서로다른 app에 존재하는 html파일의 이름이 같다면? -> 어떤 것을 render할지 모른다

    -> 따라서 각각의 app하위에 있는 templates에 app의 name과 같은 폴더를 하나 더 만들어 주면 분리가 된다.

    -> first_app/templates/first_app/hello.html

  - render함수는 settings.py의 INSTALLED APPS에 작성된 app의 templates의 html을 자동으로 불러온다

    -> 'APP_DIRS': True

  - 하지만 반복되는 html을 하나로 묶기위해서는 base.html을 root에 생성한다

    -> 이때 base.html은 app에 들어있지 않기 때문에 불러올 수 없다.

    -> 'DIRS':[BASE_DIR / 'templates'] or 'DIRS': ['templates']를 써줌으로 수동으로 root에 있는 base.html도 render가능하게 할 수 있다.

    ```html
    # base.html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      <nav>
        <ul>
          <li><a href="{% url 'first_app:lotto' %}">Lotto</a></li>
          <li><a href="{% url 'first_app:lunch' %}">Lunch</a></li>
          <li><a href="{% url 'first_app:ping' %}">Ping</a></li>
        </ul>
      </nav>    
      <div class="container">
     # block로 정한 구역에 {% extends 'base.html' %}로 extends한 html파일의 content가 불러와진다.
        {% block content %}
        {% endblock  %}
      </div>
    </body>
    </html>
    
    # lotto.html
    # 반드시 선언해야한다 -> 해당 html파일을 'base.html'에 연결  
    {% extends 'base.html' %}
    # 'base.html'의 {% block content %}에 넣는다. 
    {% block content %}
    
      <h1>로또 번호는?</h1>
        {{ lotto_numbers }} => print
      
      <ul>
        # DTL을 이용해서 for문 사용
        {% for number in lotto_numbers %}
          # DTL을 이용해서 print사용
          <li>{{ number }}</li>
        {% endfor %}
      </ul>
    
    {% endblock content %}
    
    ```
    
  
- app_name설정과 path의 3번째 인자

  - path의 3번째 인자 == name='`<name>`'지정

  - path('hello/`<name>`', views.hello, name='hello')

    -> url이 hello/`<name>`로 전달되고 `<name>`은 views.py안에 있는 hello함수의 인자 hello(request, name)로 활용가능하고

    -> 마지막 name='hello'는 html에서 해당 url로 연결할 때 hello라는 명칭으로 바로 불러와서 사용할 수 있게 해준다

  - app_name설정

  - 위에서 언급한 name='hello'는 다른 app에서 존재할 수 도 있다

    -> url을 {% url 'hello' %}로 연결하면 어떤 url을 가져올지 알 수 없다

    -> 해당 app의 urls.py에 app_name='first_app'으로 설정한다

    -> 그리고 html에서 url을 연결할때 {% url 'first_app:hello' %}로 연결하면 오류없이 불러올 수 있다.

  - 따라서, app_name과 path의 name은 앞으로 무조건적으로 작성하자!!!!!!!!!

- 서버에 `<form>`를 이용해서 데이터 전달

  - 서버에 데이터를 전달하는 방법은 url을 통해서임

  - 사용자가 `<form>`에 값을 입력하면 `<input *name*="message" *type*="text" *id*="message">`의 name=message에 저장된다.

  - 이때 Querydict에 message라는 key로 값은 value로 저장된다.

  - 이후에 submit를 누르면 action에 있는 url로 Querydict상태로 전달된다.

  - 전달받은 url의 함수의 request에서 해당 값을 message라는 key를 통해서 가져올 수 있다.(딕셔너리처럼 활용가능)

  - ```python
    # first_app/view.py
    
    def ping(request):
        # 사용자에게 <form>이 담긴 HTML제공
        return render(request, 'first_app/ping.html')
    
    # ping에서 <form>을 통해 보낸 데이터를 읽어서 pong.html로 보여주는 함수
    def pong(request):
        # request에서 값을 꺼내기
        # print(request.GET)
        # <QueryDict: {'mesaage': ['dasd'], 'sign': ['dasd']}> => 딕셔너리처럼 사용가능
    
        message = request.GET.get('message')
        sign = request.GET.get('sign')
    
        context = {
            # request꾸러미에서 GET 딕셔너리처럼 행동하는 것의 key값인 message와 sign으로 값을 가져온다
            # 하지만 key가 없다면...? name="signaaaa" -> 키에러 -> 키에러를 방질 할 수 있는 .get활용
            # 'a': request.GET['message'],
            # 'b': request.GET['sign'],
            'message': message,
            'sign': sign,
        }
    
        return render(request, 'first_app/pong.html', context)
    
    ```

  - /ping + enter키를 누르면 발생하는 flow

    1. 서버로 request
    2. master urls.py
    3. 해당 app의 app urls.py
    4. url에 맞는 view함수 호출
    5. ping.html에 render하여 return
    6. 사용자의 데이터 입력
    7. 제출
    8. form action으로 request
    9. master urls.py
    10. 해당 app의 app urls.py
    11. url에 맞는 view함수 호출
    12. request객체 안에서 데이터 꺼내기(딕셔너리 형태로!)

