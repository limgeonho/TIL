# Django[2021.09.02]

## 1. url

- html에서 주소를 넣을 때

  -> `<a href="{% url 'articles:detail' %}">`

  -> {% url 'articles:detail' %} 처럼 작성하면 /articles/detail로 넘어간다

  -> 이때 변수값을 함께 넘기고 싶다면?

  ->  /articles/detail/2

  -> /articles/detail/`<id>`

  -> {% url 'articles:detail' article.pk %} 으로 해결한다!!!!



## 2. admin

- 장고에는 기본적으로 admin페이지가 존재한다.

- http://127.0.0.1:8000/admin/에서 DB를 직접 조회, 수정, 삭제 가능하다.

- admin.py

- admin계정 만들기

  - python manage.py createsuperuser

- ```python
  from django.contrib import admin
  from .models import Article
  
  # Register your models here.
  # 관리자 페이지에 Article를 등록하겠습니다!
  admin.site.register(Article)
  ```



## 3. method in `<form>`

- GET

  - 데이터 내놔라
  - url에 입력한 데이터가 표시된채 같이 전달된다(보안 X)

- POST

  - 데이터 받아라

  - DB에 변경이 생기는 요청의 경우 반드시 POST사용

  - 양이 많은 경우 GET은 사용할 수 없다(글자 수 제한이 있음) -> POST사용

  - CSRF Token을 반드시 함께 보내줘야 한다.

    -> {% csrf_token %}를 `<form>`에 넣는다.

- ```html
  <form method="POST" action="{% url 'articles:create' %}">
    {% csrf_token %}
    <div>
      <label for="title">제목 : </label>
      <input name="title" type="text" id="title">
    </div>
  
    <div>
      <label for="content">내용 : </label>
      <textarea name="content" id="content" cols="30" rows="5"></textarea>
    </div>
  
    <div>
      {% comment %} form태그 안에서 button은, 자동으로 submit {% endcomment %}
      <button>제출</button>
    </div>
  </form>
  ```



## 4. redirect

- 사용자가 입력한 내용을 처리 후에 다시 사용자에게 요청을 보내지 않고 서버에서 내부적으로 바로 데이터를 원하는 페이지로 전달하는 것

- from django.shortcuts import render, redirect

- views.py에서 redirect 주소 입력방법

  - return redirect(f'/articles/{article.pk}') == hardtyping(비추)

  - return redirect('articles:detail', article.pk) == 추천!!!

    -> html파일에서 url을 쓸때 {% url 'articles:detail', article.pk %}와 같은 의미임(하지만 양식이 다를 뿐...DTL이니까)

- ```python
  # views.py
  
  from django.shortcuts import render, redirect
  # Article에 접근하기 위해서는 models을 불러와야함
  from .models import Article
  
  # Create
  # 사용자에게 <form> 포함한 html을 전송(ping)
  def new(request):
      return render(request, 'articles/new.html')
  
  # 사용자가 제출한 데이터를 저장 => 상세 페이지로 이동
  def create(request):
      title = request.POST.get('title')
      content = request.POST.get('content')
  
      article = Article(title=title, content=content)
      article.save()
  
      # context = {
      #     'article': article,
      # }
      # return render(request, 'articles/~', context)를 사용하지 않는 이유?
      # -> 사용자가 입력한 데이터를 DB에 저장했는데 이를 새로운 url페이지가 아닌 기존의 detail페이지에
      # pk값만 가지고 바로 전달!! == redirect
  
      # return redirect(f'/articles/{article.pk}') -> hardtyping보다는 아래의
      # -> redirect('articles:detail', article.pk) 이용
      # {% url 'articles:detail' article.pk %}와 같은 의미지만 다른 양식임!!!(주의)
      return redirect('articles:detail', article.pk)
  ```



## 5. delete

- 데이터 삭제

  1. 먼저 삭제할 데이터를 DB에서 가져와야한다.(pk값으로)

     -> article = Article.objects.get(*pk*=*pk*)

  2. pk를 통해서 가져온 데이터를 삭제한다.

     -> article.delete()

  3. 삭제 후 기존 페이지로 redirect

- ```python
  # views.py
  # Delete
  # 특정 게시글을 삭제
  def delete(request, pk):
      article = Article.objects.get(pk=pk)
      article.delete()
      return redirect('articles:index')
  ```

- detail.html페이지에 delete버튼을 만들어준다.

- 삭제는 DB에 직접적으로 변경하는 것이기 때문에 

  -> 무조건 POST로 보내야한다.

  -> POST로 보내니깐 당연히 CSRF Token도 같이 보낸다.

- 추가적으로 button만 누르면 삭제되기 때문에 경고창를 하나 띄워준다

  -> JS로 밖에 방법이 없음...

  -> `<button *onclick*="return confirm('진짜 삭제하실??')">`삭제`</button>`

- ```html
  # detail.html
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      {% comment %} onclick="return confirm('진짜 삭제하실??')" -> JS로 브라우저를 직접 control {% endcomment %}
      <button onclick="return confirm('진짜 삭제하실??')">삭제</button>
    </form>
  ```

- `<form>`의 url을 전달받은 view.py의 delete함수 수정!!!

- ```python
  # Delete
  # 특정 게시글을 삭제
  def delete(request, pk):
      article = Article.objects.get(pk=pk)
  
      # 사용자가 페이지에서 버튼을 누르는 것 == POST요청 -> POST요청이 들어왔을 경우에만 삭제 기능 활성화
      # 이런 처리를 하지 않으면 url로 접근해서(GET) 무작위로 삭제 가능(방어)
      if request.method == 'POST':
          article.delete()
          return redirect('articles:index')
      # POST로 요청이 들어온 것이 아니라면 그냥 detail페이지로 redirect(=GET요청이면 방어)
      else:
          return redirect('articles:detail', article.pk)
  ```



## 6. update

- 데이터 수정

- detail함수에서 수정하려는 특정 게시글을 사용자에게 <form>을 포함한 html전송(+내용 채워서)

- 이때 html파일에서는 기존의 내용을 미리 불러와야 한다. `<input>`의 value활용!!

- ```html
  <h1>Edit</h1>
  
  {% comment %} <input>의 value에 넣는다 {% endcomment %}
  {% comment %} {{ article.title }} {% endcomment %}
  {% comment %} {{ article.content }} {% endcomment %}
  
  <form method="POST" action="{% url 'articles:update' article.pk %}">
    {% csrf_token %}
    <div>
      <label for="title">제목 : </label>
      <input name="title" type="text" id="title" value="{{ article.title }}">
    </div>
  
    <div>
      <label for="content">내용 : </label>
      <textarea name="content" id="content" cols="30" rows="5">{{ article.content }}</textarea>
    </div>
  
    <div>
      {% comment %} form태그 안에서 button은, 자동으로 submit {% endcomment %}
      <button>수정</button>
    </div>
  </form>
  ```

- action="{% url 'articles:update' article.pk %}" 을 통해 article.pk을 가지고 update함수를 호출한다

- update에서는 create처럼 새로운 객체를 만들면 안된다 

  -> 나중에 수정된 사항을 할당하고 save()하면 객체가 수정되는 것이 아니라 새로운 객체가 만들어지기 때문!!!

  -> 새로운 객체 생성 X -> pk를 통해 가져온 객체의 인스턴스 변수에 덮어 쓴다 -> save() -> 상세페이지로~

- ```python
  # views.py
  # 사용자에게 <form>을 포함한 html전송(+내용 채워서)
  def edit(request, pk):
      article = Article.objects.get(pk=pk)
      context = {
          'article': article,
      }
      return render(request, 'articles/edit.html', context)
  
  
  # 사용자가 수정한 데이터를 저장(새로운 객체 만들기가 아니라 덮어써야함 -> pk로 해당 article를 불러와서 덮어쓰고 save()!!!) => 상세페이지로 이동
  def update(request, pk):
      article = Article.objects.get(pk=pk)
      article.title = request.POST.get('title')
      article.content = request.POST.get('content')
      article.save()
      return redirect('articles:detail', article.pk)
  ```




## 7. 기타

- 페이지는 먼저 html페이지를 보여주고(render) -> 내부적으로 데이터CRUD를 한 뒤에 다른 페이지로 보낸다(redirect)
- from .models import Article? => models.py에서 Article를 의미함
