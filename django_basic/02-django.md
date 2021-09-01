# Django[2021.09.01]

## 1. model

- model.py에 작성된다
- 데이터에 대한 정보를 가짐(사용자가 저장)
- model을 통해 데이터베이스에 접속하고 관리함(model != 데이터베이스), DB를 조작만 함
- 데이터베이스
  - 체계화된 데이터의 모임
  - query(쿼리)
    - 데이터를 조회하기 위한 명령어
  - 스키마 : 데이터베이스의 구조(전반적인 명세를 기술한 것)
  - 테이블 : 엑셀표와 같음(컬럼-열-필드, 행-레코드) - 관계
  - 필드에는 데이터 형식이 작성된다
  - 레코드에는 데이터가 저장된다
  - PK(기본키) : 각 행의 고유값, 반드시 설정해야함!!(UNIQUE), 다흔 데이터와 구별하기 위해



## 2. ORM

- object relational mapping

- 객체지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템간에 (django-sql)데이터를 변환하는 기술

- OOP프로그래밍에서 RDBMS을 연동할때 데이터베이스와 객체 지향 프로그래밍 언어 간에 호환되지 않는 데이터를 변환하는 프로그래밍 기법

- django는 내장 django 내장 ORM을 사용   ==>   class Article(models.Model)

- ```python
  from django.db import models
  """
  1. 모델명(클래스명) => 명사형 단수로 작성
  2. 1 모델 == DB의 1 테이블과 대응(Article == excel에서 1 sheet)
  3. 모델 클래스 내부의 클래스 변수 == 컬럼 이름에 해당
  """
  class Article(models.Model):
      pass
  ```

- 결과적으로 

  -> python을 이용해서 작성 -> 내장 ORM -> SQL문으로 변환해서 -> DB에 접근

- 장점 : SQL언어를 몰라도 DB에 접근가능, 객체지향적으로 생산성이 높음(제일 중요!)

- 단점 : ORM만으로는 완전한 서비스를 구현하기 어려운 경우가 있음

- 목적 : DB를 객체로 조작하기 위해 ORM을 사용(python)

- ![orm](https://user-images.githubusercontent.com/73927750/131594389-2f14e891-3e18-458d-bd77-ce2380d6cca1.JPG)



## 3. model.py

- DB컬럼과 어떠한 타입으로 정의할 것인지에 대해 django.db라는 모듈의 models를 상속

  - 각 모델은 django.db.models.Model클래스의 서브 클래스로 작성

- title과 content는 모델의 필드를 나타냄

  - 각 필드는 클래스 속성으로 지정, 해당 속성은 DB의 열(필드)에 매핑

-   ```python
    from django.db import models
    
    class Article(models.Model):
        # CharField는 길이 제한 가능, TextField는 길이 제한 불가능
        title = models.CharField(max_length=10)
        content = models.TextField()
    ```



## 4. migrations

- django가 model에 생긴 변화를 DB에 반영하는 방법

- 명령어

  - makemigrations
  - migrate

- flow

  - model을 수정한 결과를 -> 설계도로 바꿈(migrations) -> DB에 전달 

    -> python manage.py makemigrations -> migrations에 바뀐파일이 올라감 

    -> python manage.py migrate(migrate를 통해 만든 설계도를 DB에 적용, ORM을 이용)

    -> db.sqlite3에 적용됨

  - model.py를 수정한 이후에는 동일한 과정을 반복한다

    -> makemigrations -> migrate

- 참고

  - Datefield's options

  - ```python
    class Article(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()
        # auto_now_add : 최소 생성 일자(ORM이 insert할 때만 현재 날짜와 시간 갱신)
        # -> 어떤 값을 최초로 넣을 때
        created_at = models.DateTimeField(auto_now_add=True)
        # auto_now : 최종 수정 일자(ORM이 save를 할 떄마다 현재 날짜와 시간 갱신)
        updated_at = models.DateTimeField(auto_now=True)
    ```

- migrations 3 stages

  1. models.py
  2. python manage.py makemigrations
  3. python manage.py migrate



## 5. Database API

- DB를 조작하기 위한 도구

- model을 만들면 django가 객체들을 만들고 읽고 수정하고 지울 수 있는 database-abstract API를 자동으로 만들어줌

- Article.objects.all() == DB API  == 의미 : Article class에 있는 모든 객체를 줘!

  - Article : Class name
  - objects : Manager
  - all() : QuerySet API

- Manager

  - 기본적으로 model클래스를 만들면 무조건 objects라는 manager가 생성됨 -> 끝

- QuerySet 

  - 데이터베이스로부터 전달받은 객체 목록(0개, 1개, ...여러개)
  - QuerySet[    ] : 리스트 형태로 전달되게 때문에 리스트처럼 이용하여 조회, 필터, 정렬 가능

- ![orm](https://user-images.githubusercontent.com/73927750/131630831-0231cb8b-83f6-406b-833c-011814ed111e.JPG)

- 참고사항

  - more powerful interactive shell

    -> pip install django-extensions -> settings.py -> INSTALLED APPS에 등록

    -> pip install ipython

    -> 설치 완료되었다면 python manage.py shell_plus

- 전체 article 조회

  - ```shell
    In [1]: Article.objects.all()
    Out[1]: <QuerySet []>
    ```



## 6. CRUD

- Create, Read, Update, Delete

- Create : 데이터 생성

  - 3가지 방법이 존재함

  - ![data_save](https://user-images.githubusercontent.com/73927750/131629771-5e4f4757-61bd-40c5-af97-1997b32be696.JPG)

  - ```shell
    ====================== 1 번째 방법 ======================
    객체를 생성하고 인스턴스변수에 값을 할당한 뒤에는 반드시 .save() 해야 DB에 등록
    In [1]: article = Article()
    
    In [2]: article
    Out[2]: <Article: Article object (None)>
    
    In [3]: article.title = 'first'
    
    In [4]: article.content = 'django!'
    
    In [5]: Article.objects.all()
    Out[5]: <QuerySet []>
    
    반드시 저장해야 DB등록
    In [6]: article.save()
    
    In [7]: Article.objects.all()
    Out[7]: <QuerySet [<Article: Article object (1)>]>
    
    In [8]: article.title
    Out[8]: 'first'
    
    In [9]: article.id
    Out[9]: 1
    
    pk == id
    In [10]: article.pk
    Out[10]: 1
    
    In [11]: article.created_at
    Out[11]: datetime.datetime(2021, 9, 1, 5, 10, 52, 576726, tzinfo=<UTC>)
    
    ====================== 2 번째 방법(추천) ====================== 
    객체를 생성하고 인스턴스변수에 값을 할당한 뒤에는 반드시 .save() 해야 DB에 등록
    In [12]: article = Article(title='second', content='django!!!')
    
    In [13]: article
    Out[13]: <Article: Article object (None)>
    
    반드시 저장해야 DB등록
    In [14]: article.save()
    
    In [15]: article
    Out[15]: <Article: Article object (2)>
    
    In [16]: article.pk
    Out[16]: 2
    
    ====================== 3 번째 방법 ======================
    따로 .save()를 하지 않아도 알아서 저장되고 return해줌
    In [17]: Article.objects.create(title='third', content='django!!!!!')
    Out[17]: <Article: Article object (3)>
    ```

  - ```python
    # form의 action주소로 받은 입력값들을 통해 새로운 객체를 만들고 Article DB에 저장.save()
    
    def create(request):
        # new로부터 title과 content를 받아서 저장
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 1
        article = Article()
        article.title = title
        article.content = content
        article.save()
    
        # 2 => 앞으로 사용하게 될 방법
        article = Article(title=title, content=content)
        article.save()
    
        # 3 => 바로 저장되어버리기 때문에 유효성검사를 할 수 없다
        Article.objects.create(title=title, content=content)
    
        return render(request, 'articles/create.html')
    ```

- Read : 데이터 조회

  - 크게 2가지로 나눠짐

    1. queryset을 반환 O

       - .get()

         - 객체가 없다면 Dose Not Exist 예외

         - 둘 이상의 객체 MultipleObjectReturned 예외

           -> 따라서 유일한 값을 보장할 수 있는 pk값을 매개변수로 사용!!!

         - 

           ```shell
           In [2]: Article.objects.get(pk=1)
           Out[2]: <Article: first>
           ```

       - .filter()

         - 주어진 매개변수와 일치하는 객체를 포함하는 새 queryset을 반환

         - 만약에 찾고자하는 것과 일치하는 것이 없다면 -> 빈 queryset

         - ```shell
           In [3]: Article.objects.filter(title='aaaa')
           Out[3]: <QuerySet []>
           ```

         - ```python
           # Article.objects.all()으로 DB에 있는 articles를 모두 읽어오기
           
           def index(request):
               # 작성된 모든 게시글을 출력
               # 1. 모든 게시글 조회
               articles = Article.objects.all()
               context = {
                   'articles': articles,
               }
               return render(request, 'articles/index.html', context)
           ```

    2. queryset을 반환 X

- Update : 데이터 수정

  - 수정하기 위해서는 먼저 해당 데이터를 가져와야 한다.

  - 가져온 데이터를 수정하고 반드시 save()해야 DB에 등록된다.

  - ```shell
    수정할 데이터를 가져온다(pk로)
    In [4]: article = Article.objects.get(pk=1)
    
    In [5]: article
    Out[5]: <Article: first>
    
    값 변경
    In [6]: article.title = 'byebye'
    
    변경한 값을 다시 DB에 저장
    In [7]: article.save()
    
    In [8]: article.title
    Out[8]: 'byebye'
    ```

- Delete : 데이터 삭제

  - .delete()하면 끝

  - ```shell
    In [9]: article
    Out[9]: <Article: byebye>
    
    그냥 바로 삭제
    In [10]: article.delete()
    Out[10]: (1, {'articles.Article': 1})
    
    In [11]: Article.objects.all()
    Out[11]: <QuerySet [<Article: second>, <Article: third>]>
    ```



## 7. HTTP method

- GET

  - 특정 리소스를 가져오도록 요청할 때 사용
  - 반드시 데이터를 가져올 때만 사용!!!
  - DB에 영향을 주지 않음
  - CRUD에서 R역할을 담당

- POST

  - 서버로 데이터를 전송할 때 사용
  - 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아서 전송
  - 서버에 변경사항을 만드는 경우
  - CRUD에서 C/U/D역할을 담당

- CSRF(cross-site-request-forgery)

  - 사이트 간 요청 위조 

  - framework가 본인이 만든 페이지가 맞는지 검증하는데 사용

    -> 검증을 받기 위해 추가적인 값을 데이터와 같이 보낸다

    -> 예시에서는 title + content + hashcode를 보낸다(hashcode!!!)

  - Security Token 사용방식

    - 사용자의 데이터에 임의의 난수 값을 부여해 매 요청마다 함께 전달한다

      -> 장고가 스스로 난수 값을 확인하여 검증한다

  - POST, PATCH, DELETE method에서 사용(GET제외)

  - ```html
    <form action="{% url 'articles:create' %}" method="POST">
        {% csrf_token %}
        <label for="title">Title : </label>
        <input type="text" id="title" name="title">
        <label for="content">Content : </label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea>
        <input type="submit">
      </form>
      <hr>
      <a href="{% url 'articles:index' %}">back</a>
    {% endblock %}
    ```

  - ```python
    # views.py
    def create(request):
        # request.GET -> request.POST로 변경!!!
        title = request.POST.get('title')
        content = request.POST.get('content')
    
    ```

    

