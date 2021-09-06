# Django[2021.09.06]

## 1. Form Class

- 유효성 검사를 도와주는 도구

- 개발자가 직접작성한 form보다 더 안전하게 보호가능

- 랜더링을 위한 데이터 준비 및 재구성

- 데이터에 대한 HTML forms 생성

- 클라이언트로부터 받은 데이터 수신 및 처리

- 유효하지 않은 field에 대해서는 에러 메세지도 결정

- form의 장점

  1. Validation
  2. html자동 생성

- forms.py 파일을 만들어 준다

- forms 라이브러리에 있는 Form 클래스를 상속받음

- ```python
  # forms.py
  from django import forms
  
  class ArticleForm(forms.Form):
  	title = forms.CharField(max=length)
      # forms에는 TextField가 없음
  	content = forms.CharField(widget=forms.Textarea)
  ```

- ```python
  # views.py
  from .forms import ArticleForm
  
  def new(request):
      form = ArticleForm()
      context = {
          'form': form,
      }
      return render(request, 'articles/new.html', context)
  ```

- ```html
  # new.html
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}" method="POST">
      {% csrf_token %}
        # 나머지는 전부 같지만 기존에 있던 input, label 태그들이 사라지고 {{ form.as_p }}하나로 같은 효과
        {{ form.as_p }}
      <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
  {% endblock  %}
  ```

- form rendering options

  - {{ form }}만 하면 한줄로 나옴 -> rendering options를 선택
  - as_p : 필드가 `<p>`로 감싸짐
  - as_ul : 필드가 `<li>`로 감싸짐 -> `<ul>`는 직접 작성
  - as_table : 필드가 `<tr>`로 감싸짐 -> `<table>`는 직접 작성

- django에서 HTML input요소를 표현하는 방법

  1. form fields
     - input에 대한 유효성 검사를 처리
  2. widgets(단독적으로 쓰이지 않고 form fields에 종속되서 사용)
     - html input 요소 렌더링

- Form field 응용

- ```python
  from django import forms
  
  class ArticleForm(forms.Form):
      # 형식은 공식 style guide임
      REGION_A = 'sl'
      REGION_B = 'dj'
      REGION_C = 'gj'
      REGION_D = 'gm'
      REGION_E = 'bs'
      
      # list + tuple 형식으로 작성
      REGION_CHOICES = [
          # 사용자에게 출력될 값 -> 하지만 서버에서는 sl로 인식
          (REGION_A, '서울'),
          (REGION_B, '대전'),
          (REGION_C, '광주'),
          (REGION_D, '구미'),
          (REGION_E, '부산'),
      ]
  
      title = forms.CharField(max_length=10)
      # forms.Charfield()랑 models.Charfield()랑 아예 다른거임(관계없음)
      # forms에는 TextField가 없음
      content = forms.CharField(widget=forms.Textarea)
      # select의 name이 key값, 선택한 것이 value값
      region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select)
  ```

- ![choiceform](https://user-images.githubusercontent.com/73927750/132156147-8259c824-79b4-43e1-81de-6dbeb032c631.JPG)



## 2. ModelForm

- 이미 정의된 model을 통해서 form 정의(반복을 피하기 위해)

- Article 모델이 있고 사용자가 게시글을 제출할 수 있는 양식을 만들고 싶은 경우

  -> 이미 model필드에서 정의했기 때문에 form필드에서 재정의 하는 중복발생

  -> ModelForm을 통해 기존의 model을 이용해서 form을 정의

- 선언

  - forms.ModelForm을 상속

  - ```python
    from .models import Article
    
    class ArticleForm(forms.ModelForm):
        # 반드시 작성
        class Meta:
            model = Article
            # model에서 가져오는 field가 많지 않을 때(하나씩 직접 작성)
            # fields = ('title', 'content',)
            # model에서 가져오는 field가 많을 때('__all__') -> 전부 가져오기
            fields = '__all__'
            # 제외하고 싶은 field
            # exclude = ('title',)
    ```

  -  Meta class

    - 어떤 model을 참조했는지에 대해 Meta class에 작성

      -> 따라서, ModelForm은 반드시 Meta class를 가지고 있어야한다.

    - modelform은 어떤  model을 기반으로하는지에 대한 정의가 필요함 

      -> meta class를 통해 해당 model을 참고한다고 알려줘야함

    - ```python
      class ArticleForm(forms.ModelForm):
          # HTML 요소
          title = forms.CharField(
              label='제목',
              widget=forms.TextInput(
                  attrs={
                      'class': 'my_title',
                      'placeholder': 'Enter the title',
                      'maxlength': 10,
                  }
              )
          )
          content = forms.CharField(
              label='내용',
              widget=forms.Textarea(
                  attrs={
                      'class': 'my_content',
                      'placeholder': 'Enter the content',
                      'rows': 5,
                      'cols': 50,
                  }
              )
          )
      
          # 반드시 작성
          class Meta:
              model = Article
              # model에서 가져오는 field가 많지 않을 때(하나씩 직접 작성)
              # fields = ('title', 'content',)
              # model에서 가져오는 field가 많을 때('__all__') -> 전부 가져오기
              fields = '__all__'
              # 제외하고 싶은 field
              # exclude = ('title',)
      
      ```

- Validation

  - ModelForm을 통한 views.py 수정(유효성 검사)

  - ModelForm을 통해 유효성 검사를 간단하게 할 수 있음

  - is_valid()

  - ```python
    def create(request):
        # 기존의 방법================================================
        # title = request.POST.get('title')
        # content = request.POST.get('content')
    
        # article = Article(title=title, content=content)
        # article.save()
        # return redirect('articles:detail', article.pk)
        # ==========================================================
    
        # 데이터가 채워진 form 가져옴(request.POST로 가져온 모든 내용)
        form = ArticleForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            # 저장한 객체
            article = form.save()
            return redirect('articles:detail', article.pk)
        return redirect('articles:new')
    ```

  - save()

    - form에 바인딩 된 데이터에서 데이터베이스 객체를 만들고 저장

    - 인자로 (instance= )를 받을 수 있음

      - form = ArticleForm(*request*.POST, *instance*=article) 

        -> instance가 O 

        -> UPDATE!!!!

      - form = ArticleForm(*request*.POST)

        -> instance가 X

        -> CREATE!!!!

      - 따라서, UPDATE하려면 무조건 instance을 써줘야한다!!!!!!!!!!

      - ```python
        def update(request, pk):
            article = Article.objects.get(pk=pk)
        
            # update
            if request.method == 'POST':
        
                form = ArticleForm(request.POST, instance=article)
                if form.is_valid():
                    form.save()
                    return redirect('articles:detail', article.pk)
        
            # edit
            else:
                form = ArticleForm(instance=article)
            context = {
                'article': article,
            }
            return render(request, 'articles/edit.html', context)
        ```

- views의 최종상태!!!

- ```python
  # 필요 없어짐
  # def new(request):
  #     pass
  
  
  def create(request):
      # title = request.POST.get('title')
      # content = request.POST.get('content')
  
      # article = Article(title=title, content=content)
      # article.save()
      # return redirect('articles:detail', article.pk)
  
      # =============================================================
      # new -> 단순하게 페이지를 조회 -> GET
      # 데이터가 채워진 form 가져옴
      # create -> POST/articles/create
      if request.method == 'POST':
          # create -> form에서 데이터를 받아서 데이터베이스에 저장 -> POST
          form = ArticleForm(request.POST)
          # 유효성 검사
          if form.is_valid():
              # 저장한 객체
              article = form.save()
              return redirect('articles:detail', article.pk)
      else:
          # new -> GET/articles/create
          form = ArticleForm()
      # context = {}의 indent가 나와 있는 이유는 39번째 줄에서 form이 유효성검사를 통과하지 못할 경우 대비
      context = {
          # form은 상황에 따라서 1. 에러메세지를 포함한 form, 2. 빈 form
          'form': form,
      }
      return render(request, 'articles/create.html', context)
  ```

- 결론

  - Form vs ModelForm
  - 둘 중에 한 쪽만 사용하는 것이 아님
  - Form
    - model에 연관되지 않는 데이터를 가져올 때 사용
  -  ModelForm
    - django가 model의 기본적인 양식을 갖고 있기 때문에 model에 연관된 데이터를 가져올때 편하게 사용
  - 상황에 맞는 form을 사용한다



## 3. Handling HTTP requests

- django에서 HTTP요청을 처리하는 방법

  1. django shortcut functions
  2. django view decorators

- django shortcut functions

  1. render()

  2. redirect()

  3. get_object_or_404()

     - manager object에서 get()을 호출

       -> 해당 객체가 존재하지 않을 경우 404 raise

       -> 해당 객체가 없는 경우를 명확하게 표현할 수 있도록함

       -> 앞으로는 .get(pk=pk)대신에

       ->  article = get_object_or_404(Article, *pk*=*pk*)사용!!!

     - ```python
       from django.shortcuts import render, redirect, get_object_or_404
       
       @require_safe
       def detail(request, pk):
           # article = Article.objects.get(pk=pk)
           article = get_object_or_404(Article, pk=pk)
           context = {
               'article': article,
           }
           return render(request, 'articles/detail.html', context)
       ```

- django view decorators

  - Allowed HTTP methods

  - 요청 메서드(GET / POST)에 따라 view함수에 대한 엑세스를 제한 -> 405

    - @require_http_methods(['GET', 'POST'])

      -> view함수 바로 위에 써주는데 해당함수는 GET', 'POST'로만 접근 가능 

    - @require_POST

      -> 'POST'로만 접근 가능

    - @require_GET 대신에 @require_safe 사용 권장

  - ```python
    from django.views.decorators.http import require_http_methods, require_POST, require_safe
    
    # import해서 view함수 바로 위에 선언
    
    @require_safe
    def index(request):
        pass
    
    @require_POST
    def delete(request, pk):
    	pass
    
    @require_http_methods(['GET', 'POST'])
    def create(request):
        pass
    ```



## 4. 기타(장고 시작 순서)

- ![장고시작순서](https://user-images.githubusercontent.com/73927750/132238211-6e0d8fb7-bf17-4bb8-8c88-8f7e6d2030cc.JPG)
