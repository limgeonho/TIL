# Django[2021.09.15]



## 1. Django Authentication System

- 이미 settings.py에 INSTALLED_APPS에 등록되어 있음
- django.contrib.auth
- django.contrib.contenttypes
- Authentication(인증)
  - 사용자의 신원 확인
  - 사용자가 자신이 누구인지 확인하는 것
- Authorization(권한)
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업 결정
  - ex) superuser



## 2. 쿠키와 세션

- http(Hyper Text Transfer Protocol)

  - 비연결지향

    - 서버는 요청을 보내고 연결을 끊음

  - 무상태

    - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음

      -> 로그인은?

      -> 클라이언트와 서버의 지속적인 연결관계를 유지하기 위해 쿠키와 세션이 존재!!

- 쿠키(입장을 확인하는 도장이나 팔찌같은 존재)

  - 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

  - 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일

  - 사용자의 로컬에 key-value 데이터를 저장

  - 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송

  - HTTP쿠키는 상태가 있는 세션을 만들어줌

  - 클라이언트는 요청을 보낼때 마다 쿠키를 보내야함 

    -> 그래야 서버입장에서 매 순간 연결된 상태처럼 보일 수 있도록 해줌

  - 웹페이지에 접속하면 요청한 웹 페이지를 받으묘 쿠키를 저장하고, 클라이언트가 같은 서버에 재요청 시 요청과 쿠키도 전송

    -> 상태가 있는 연결상태 유지(로그인 상태 유지 가능) 

    ![쿠키](https://user-images.githubusercontent.com/73927750/133351248-c03fef34-de20-46e8-bf67-0066a5b56653.JPG)

  - 쿠키의 사용 목적

    1. 세션 관리**
       - 로그인, 아이디 자동 완성, 공지 하루 안보기, 팝업, 장바구니
    2. 개인화
       - 사용자 선호, 테마 설정
    3. 트래킹
       - 사용자 행동을 기록 분석

- 세션

  - 사이트와 특정 브라우저 사이의 상태를 유지시키는 것
  - 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고 클라이언트는 발급 받은 session id를 쿠키에 저장
  - 쿠키에 session id를 넣어서 서버로 전송
  - 로그인 -> 로그인성공(session id를 같이 받음) -> 이후부터 매 요청 시 session id를 담은 쿠키를 전송(로그인 상태 유지)

- 쿠키의 수명

  - session cookies
    - 현재 세션이 종료되면 삭제됨
  - persistent cookies
    - expires 속성에 지정된 날짜 혹은 Max_Age 속성에 지정된 기간이 지나면 삭제

- Session in Django

  - 미들웨어를 통해 구현됨

  - database-backed-sessions 저장방식을 기본 값으로

  - django-session 테이블에 저장됨

  - ```python
    # settings.py
    MIDDLEWARE = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
    ]
    ```

### 

## 3. Login

- 로그인은 session을 create하는 로직과 같음

- django에서는 built-in forms를 제공함

- Authentication Form

  - 사용자 로그인을 위한 form
  - request를 첫 번째 인자로 받음

- login함수

  - 현재 세션에 연결하려는 인증 된 사용자가 있는 경우 login()가 필요

  - view함수 내에서 사용

  - User객체가 필요

  - 기존의 view함수 안에 있는 create와 비슷한 구조(session id를 만드는 것)

  - ```python
    # accounts/views.py
    
    from django.shortcuts import redirect, render
    # 내가 만든 login url함수와 이름이 같기 때문에 auth_login라고 별칭을 붙여준다.
    from django.contrib.auth import login as auth_login
    from django.contrib.auth.forms import AuthenticationForm
    
    def login(request):
        # 사용자가 로그인 되었다면 login페이지로 들어갈 수 없게 미리 처리하는 부분
        # request.user -> user은 이미 settings.py
        # -> 'django.contrib.auth.context_processors.auth', 에 선언되어 있기 때문에 
        # -> 어떤 context에서도 바로 사용할 수 있음
        if request.user.is_authenticated:
            return redirect('articles:index')
    
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                # 로그인
                # get_user()는 AuthenticationForm의 인스턴스 메서드
                auth_login(request, form.get_user())
                return redirect(request.GET.get('next') or 'articles:index')
        else:
            # 비어있는 로그인 form
            form = AuthenticationForm()
        context = {
            'form': form,
        }
    
        return render(request, 'accounts/login.html', context)
    ```

  - 현재 로그인 되어 있는 유저 정보 출력

  - ```html
    # base.html
    <body>
      <div class="container">
        {% if request.user.is_authenticated %}
          # 로그인된 사용자의 id를 출력(context에 없어도 가져올 수 있다)
          <h3>Hello, {{user}} </h3>
          <form action="{% url 'accounts:logout' %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="Logout">
          </form>
        {% else %}
          <a href="{% url 'accounts:login' %}">Login</a>
        {% endif %}
    
        {% block content %}
        {% endblock content %}
      </div>
    </body>
    ```

    

## 4. Logout

- 로그아웃은 session을 delete(삭제)하는 것임

- logout함수

  - HttpRequest 객체를 인자로 받고 반환 값이 없음

  - 현재 요청에 대한 session data를 DB에서 완전히 삭제하고, 클라이언트 쿠키에서도 sessionid가 삭제됨

    -> 그래야 다음 사용자가 내 로그인 정보에 접근할 수 없다.

  - ```python
    # accounts/views.py
    
    from django.shortcuts import redirect, render
    from django.contrib.auth import logout as auth_logout
    from django.contrib.auth.forms import AuthenticationForm
    from django.views.decorators.http import require_POST
    
    @require_POST
    def logout(request):
        if request.user.is_authenticated:
            auth_logout(request)
        return redirect('articles:index')
    ```



## 5. 로그인 사용자에 대한 엑세스 제한 2가지 방법

1. is_authenticated -> attribute

   - User model의 속성 중 하나

   - 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성(Anonymous user은 False)

   - 사용자가 인증 되었는지 여부를 알 수 있는 방법

   - request.user에서 해당 속성을 사용

   - 권한과는 관련 X

   - ```html
     # base.html
     <body>
       <div class="container">
         # 로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정
         {% if request.user.is_authenticated %}
           # 로그인된 사용자의 id를 출력(context에 없어도 가져올 수 있다)
           <h3>Hello, {{user}} </h3>
           <form action="{% url 'accounts:logout' %}" method="POST">
             {% csrf_token %}
             <input type="submit" value="Logout">
           </form>
         {% else %}
           <a href="{% url 'accounts:login' %}">Login</a>
         {% endif %}
     
         {% block content %}
         {% endblock content %}
       </div>
     </body>
     ```

   - ```python
     # accounts/views.py
     
     def login(request):
         # 사용자가 로그인 되었다면 login페이지로 들어갈 수 없게 미리 처리하는 부분
         if request.user.is_authenticated:
             return redirect('articles:index')
     
         if request.method == 'POST':
             form = AuthenticationForm(request, request.POST)
             if form.is_valid():
                 # 로그인
                 auth_login(request, form.get_user())
                 return redirect(request.GET.get('next') or 'articles:index')
         else:
             form = AuthenticationForm()
         context = {
             'form': form,
         }
         return render(request, 'accounts/login.html', context)
     
     # 인증된 사용자(로그인 상태)만 로그아웃 로직을 수행할 수 있도록 처리
     @require_POST
     def logout(request):
         if request.user.is_authenticated:
             auth_logout(request)
         return redirect('articles:index')
     ```

2. login_required -> decorator

   - 사용자가 로그인되어 있지 않으면, settings.LOGIN_URL에 설정된 문자열 기반 절대 경로로 redirect함

   - LOGIN_URL의 기본값은 '/accounts/login/'

     -> app이름을 accounts로 한 이유!

   - 사용자가 로그인되어 있으면 정상적으로 view함수 실행

   - 인증 성공 시 사용자가 redirect되어야 하는 경로는 'next'라는 퀴리 문자열 매개 변수에 저장됨

     -> 로그인 하지 않은 상태에서 articles/create 접근

     -> /accounts/login/?next=/articles/create 와 함께 로그인 페이지로 옴

     -> 로그인 완료

     -> index가 아닌 articles/create 로 바로 redirect

     ```python
     # accounts/views.py/login
     if request.method == 'POST':
             form = AuthenticationForm(request, request.POST)
             if form.is_valid():
                 # 로그인
                 auth_login(request, form.get_user())
                 return redirect(request.GET.get('next') or 'articles:index')
     ```

   - views.py에서 로그인이 필요한 기능은 미리 decorator을 통해 로그인을 요구하자!!

     - ```python
       # articles/views.py
       
       from django.shortcuts import render, redirect, get_object_or_404
       from django.views.decorators.http import require_http_methods, require_POST, require_safe
       from django.contrib.auth.decorators import login_required
       from .models import Article
       from .forms import ArticleForm
       
       
       @login_required
       @require_http_methods(['GET', 'POST'])
       def create(request):
           if request.method == 'POST':
               form = ArticleForm(request.POST)
               if form.is_valid():
                   article = form.save()
                   return redirect('articles:detail', article.pk)
           else:
               form = ArticleForm()
           context = {
               'form': form,
           }
           return render(request, 'articles/create.html', context)
           
           
       @login_required
       @require_POST
       def delete(request, pk):
           article = get_object_or_404(Article, pk=pk)
           article.delete()
           return redirect('articles:index')
       
       
       @login_required
       @require_http_methods(['GET', 'POST'])
       def update(request, pk):
           article = get_object_or_404(Article, pk=pk)
           if request.method == 'POST':
               form = ArticleForm(request.POST, instance=article)
               if form.is_valid():
                   form.save()
                   return redirect('articles:detail', article.pk)
           else:
               form = ArticleForm(instance=article)
           context = {
               'article': article,
               'form': form,
           }
           return render(request, 'articles/update.html', context)
       ```

- @required_post와 @login_required를 함께 사용하는 경우 에러발생

  - 로그인 이후 'next'매개변수를 따라 해당 함수로 다시 redirect되는데 이때 @required_post때문에 405 에러가 발생함

  - 따라서, @required_post와 @login_required 중 @login_required를 지우고 delete함수 안에 raw한 방법으로 로그인 여부파악

    -> if request.user.is_authenticated:

  - ```python
    # articles/views.py
    
    # @login_required
    @require_POST
    def delete(request, pk):
        if request.user.is_authenticated:
            article = get_object_or_404(Article, pk=pk)
            article.delete()
        return redirect('articles:index')
    ```



## 6. 회원가입

- UserCreationForm

  - 주어진 username과 passord로 권한이 없는 새 user를 생성하는 ModelForm

  - username, password1, password2 총 3가지 필드를 가진다.

  - articles/views.py에서 create와 form의 형태말고는 전부 같음

  - ```python
    # accounts/views.py
    
    from django.contrib.auth import login as auth_login
    from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
    
    
    @require_http_methods(['POST', 'GET'])
    def signup(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                # UserCreationForm에서는 return값이 방금 회원가입시 입력한 user이다
                user = form.save()
                # 방금 회원가입한 user로 로그인!!
                auth_login(request, user)
                return redirect('articles:index')
        else:
            form = UserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)
    ```



## 7. 회원탈퇴

- 회원탈퇴는 DB에서 사용자를 삭제하는 것과 같음

- ```python
  # accounts/views.py
  
  @require_POST
  def delete(request):
      if request.user.is_authenticated:
          request.user.delete()
          # 삭제한 후 user의 sessionid가 남아있는 것을 삭제하기 위해(순서 : 탈퇴 -> 로그아웃)
          auth_logout(request)
      return redirect('articles:index')
  ```



## 8. 회원정보수정

- UserChangeForm

  - 사용자의 정보 및 권한을 변경하기 위해 admin인터페이스에서 사용되는 ModelForm

  - UserChangeForm에서는 일반 사용자가 접근해서는 안될 정보들까지 모두 수정이 가능해짐

    -> UserChangeForm을 상속받아서 CustomUserChangeForm을 만들어서 접근 가능한 필드를 조정해야함

  - 사실상 article의 update와 같은 구조임

  - ```python
    # articles/forms.py
    
    from django.contrib.auth.forms import UserChangeForm
    from django.contrib.auth import get_user_model
    
    # UserChangeForm을 상속 받아서 CustomUserChangeForm을 생성
    class CustomUserChangeForm(UserChangeForm):
    
        class Meta:
            model = get_user_model()
            # fields = ??? -> 수정시 필요한 필드만 선택해서 작성
            fields = ('email', 'first_name', 'last_name',)
    ```

  - get_user_model()

    - 현재 프로젝트에서 활성화 된 사용자 모델을 반환

  - ```python
    # accounts/views.py
    
    from .forms import CustomUserChangeForm
    
    @login_required
    @require_http_methods(['POST', 'GET'])
    def update(request):
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('articles:index')
        else:
            # 상속 받아 만든 CustomUserChangeForm
            form = CustomUserChangeForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/update.html', context)
    ```



## 9. 비밀번호 변경

- PasswordChangeForm

  - 사용자가 비밀번호를 변경할 수 있도록 하는 Form

  - 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함

  - 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스

    -> 상속받기 때문에 PasswordChangeForm(*request*.user)이 기본값임!!!!(다른 Form들과 다름 주의!!)

  - 비밀번호가 변경되면 session이 바뀜(기존 세션과 회원인증 정보가 일치하지 않게 되기 때문에)

    -> 변경 후 로그아웃되버림

    -> 새로운 password hash로 session을 업데이트 해줘야함

    -> update_session_auth_hash(*request*, form.user)

  - ```python
    # accounts/views.py
    
    from django.contrib.auth import update_session_auth_hash
    from django.contrib.auth.forms import PasswordChangeForm
    
    @login_required
    @require_http_methods(['POST', 'GET'])
    def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('articles:index')
        else:
            # 지금 까지와는 다르게 request.user가 인자로 먼저 전달된다.
            form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, 'accounts/change_password.html', context)
    ```



## 10. 총 정리

- accounts/views.py

  ```python
  from django.shortcuts import redirect, render
  from django.contrib.auth import login as auth_login
  from django.contrib.auth import logout as auth_logout
  from django.contrib.auth import update_session_auth_hash
  from django.contrib.auth.decorators import login_required
  from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
  from django.views.decorators.http import require_POST, require_http_methods
  from .forms import CustomUserChangeForm
  
  
  @require_http_methods(['POST', 'GET'])
  def login(request):
      # 사용자가 로그인 되었다면 login페이지로 들어갈 수 없게 미리 처리하는 부분
      if request.user.is_authenticated:
          return redirect('articles:index')
  
      if request.method == 'POST':
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              # 로그인
              auth_login(request, form.get_user())
              return redirect(request.GET.get('next') or 'articles:index')
      else:
          form = AuthenticationForm()
      context = {
          'form': form,
      }
  
      return render(request, 'accounts/login.html', context)
  
  
  @require_POST
  def logout(request):
      if request.user.is_authenticated:
          auth_logout(request)
      return redirect('articles:index')
  
  
  @require_http_methods(['POST', 'GET'])
  def signup(request):
      if request.user.is_authenticated:
          return redirect('articles:index')
  
      if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
              # UserCreationForm에서는 return값이 방금 회원가입시 입력한 user이다
              user = form.save()
              # 방금 회원가입한 user로 로그인!!
              auth_login(request, user)
              return redirect('articles:index')
      else:
          form = UserCreationForm()
      context = {
          'form': form,
      }
      return render(request, 'accounts/signup.html', context)
  
  
  @require_POST
  def delete(request):
      if request.user.is_authenticated:
          request.user.delete()
          # 삭제한 후 user의 sessionid가 남아있는 것을 삭제하기 위해(순서 : 탈퇴 -> 로그아웃)
          auth_logout(request)
      return redirect('articles:index')
  
  
  @login_required
  @require_http_methods(['POST', 'GET'])
  def update(request):
      if request.method == 'POST':
          form = CustomUserChangeForm(request.POST, instance=request.user)
          if form.is_valid():
              form.save()
              return redirect('articles:index')
      else:
          # 상속 받아 만든 CustomUserChangeForm
          form = CustomUserChangeForm(instance=request.user)
      context = {
          'form': form,
      }
      return render(request, 'accounts/update.html', context)
  
  
  @login_required
  @require_http_methods(['POST', 'GET'])
  def change_password(request):
      if request.method == 'POST':
          form = PasswordChangeForm(request.user, request.POST)
          if form.is_valid():
              form.save()
              update_session_auth_hash(request, form.user)
              return redirect('articles:index')
      else:
          # 지금 까지와는 다르게 request.user가 인자로 먼저 전달된다.
          form = PasswordChangeForm(request.user)
      context = {
          'form': form,
      }
      return render(request, 'accounts/change_password.html', context)
  
  ```

- articles/views.py

  ```python
  from django.shortcuts import render, redirect, get_object_or_404
  from django.views.decorators.http import require_http_methods, require_POST, require_safe
  from django.contrib.auth.decorators import login_required
  from .models import Article
  from .forms import ArticleForm
  
  
  @require_safe
  def index(request):
      articles = Article.objects.order_by('-pk')
  
      context = {
          'articles': articles,
      }
      return render(request, 'articles/index.html', context)
  
  
  @login_required
  @require_http_methods(['GET', 'POST'])
  def create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              article = form.save()
              return redirect('articles:detail', article.pk)
      else:
          form = ArticleForm()
      context = {
          'form': form,
      }
      return render(request, 'articles/create.html', context)
  
  
  @require_safe
  def detail(request, pk):
      article = get_object_or_404(Article, pk=pk)
      context = {
          'article': article,
      }
      return render(request, 'articles/detail.html', context)
  
  
  # @login_required
  @require_POST
  def delete(request, pk):
      if request.user.is_authenticated:
          article = get_object_or_404(Article, pk=pk)
          article.delete()
      return redirect('articles:index')
  
  
  @login_required
  @require_http_methods(['GET', 'POST'])
  def update(request, pk):
      article = get_object_or_404(Article, pk=pk)
      if request.method == 'POST':
          form = ArticleForm(request.POST, instance=article)
          if form.is_valid():
              form.save()
              return redirect('articles:detail', article.pk)
      else:
          form = ArticleForm(instance=article)
      context = {
          'article': article,
          'form': form,
      }
      return render(request, 'articles/update.html', context)
  
  ```

- base.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  <body>
    <div class="container">
      {% if request.user.is_authenticated %}
        <h3>Hello, {{user}} </h3>
        <a href="{% url 'accounts:update' %}">회원정보수정</a>
        <form action="{% url 'accounts:logout' %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="Logout">
        </form>
      
        <form action="{% url 'accounts:delete' %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="회원탈퇴">
        </form>
  
      {% else %}
        <a href="{% url 'accounts:login' %}">Login</a>
        <a href="{% url 'accounts:signup' %}">Signup</a>
      {% endif %}
  
      {% block content %}
      {% endblock content %}
    </div>
  </body>
  </html>
  ```

  
