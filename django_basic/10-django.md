# Django[2021.09.16]



- articles/views.py

  ```python
  from django.shortcuts import redirect, render
  from django.contrib.auth.decorators import login_required
  
  def index(request):
      return render(request, 'articles/index.html')
  
  @login_required
  def new(request):
      # request.user => 인증됨 => User의 instance => is_authenticated == True
      # request.user => 인증안됨 => Anonymous의 instance => is_authenticated == False
      # if request.user.is_authenticated:
      #     return render(request, 'atricles/new.html')
      # return redirect('accounts:login')
      return render(request, 'articles/new.html')
  ```

- base.html

  ```html
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
        <li><a href="{% url 'articles:index' %}">Home</a></li>
        {% if request.user.is_authenticated %}
          <li><a href="{% url 'articles:new' %}">New</a></li>
          <li><a href="{% url 'accounts:profile' request.user.username %}">{{ request.user.username }}'s profile</a></li>
          <li><a href="{% url 'accounts:logout' %}">Logout</a></li>
        {% else %}
          <li><a href="{% url 'accounts:signup' %}">Signup</a></li>
          <li><a href="{% url 'accounts:login' %}">Login</a></li>
        {% endif %}
      </ul>
    </nav>
  
    <div class="container">
      {% block content %}{% endblock content %}
    </div>
  </body>
  </html>
  ```

- accounts/forms.py

  ```python
  from django.contrib.auth.forms import UserCreationForm, UserChangeForm
  
  class CustomUserCreationForm(UserCreationForm):
  
      class Meta(UserCreationForm.Meta):
          fields = ('username', 'email')
  
  
  class CustomUserChangeForm(UserChangeForm):
  
      class Meta(UserChangeForm.Meta):
          # username은 변경 불가능 하게!
          fields = ('first_name', 'last_name', 'email')
  ```

- accounts/views.py

  ```python
  from django.shortcuts import render, redirect, get_object_or_404
  from django.views.decorators.http import require_http_methods, require_POST, require_safe
  from django.contrib.auth import login as auth_login, logout as auth_logout
  from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
  from django.contrib.auth import get_user_model, update_session_auth_hash  # get_user_model함수는 UserModel이 바뀌더라도 알아서 지금 사용중인 UserModel을 가져온다
  from django.contrib.auth.decorators import login_required
  from .forms import CustomUserCreationForm, CustomUserChangeForm
  
  User = get_user_model()
  
  @require_http_methods(['POST', 'GET'])
  def signup(request):  # User model CREATE
      # 인증된 사용자는 pass
      if request.user.is_authenticated:
          return redirect('articles:index')
      
      # Create User Instance
      if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
              user = form.save()
              # login => session & cookie setting
              auth_login(request, user)
              return redirect('articles:index')
      else:
          form = CustomUserCreationForm()
      context = {
          'form': form,
      }
      return render(request, 'accounts/signup.html', context)
  
  @require_safe
  def profile(request, username): # User model DETAIL
      user = get_object_or_404(User, username=username)
      context = {
          'user': user,
      }
      return render(request, 'accounts/profile.html', context)
  
  
  @login_required
  @require_http_methods(['POST', 'GET'])
  def update(request):
      # 회원정보 수정은, 타인이 아닌 본인에 의해서만 가능
      user = request.user
      if request.method == 'POST':
          form = CustomUserChangeForm(request.POST, instance=user)
          if form.is_valid():
              user = form.save()
              return redirect('accounts:profile', user.username)
      else:
          form = CustomUserChangeForm(instance=user)
      context = {
          'form': form,
      }
      return render(request, 'accounts/update.html', context)
  
  
  @login_required
  @require_http_methods(['POST', 'GET'])
  def change_password(request):
      # PasswordChangeForm == Form
      user = request.user
      if request.method == 'POST':
          form = PasswordChangeForm(user, request.POST)
          if form.is_valid():
              user = form.save()  # 비밀번호 변경 => session_data_missmatch => login
              update_session_auth_hash(request, user) # 새롭게 user에게 session_data & cookie 할당
              return redirect('accounts:profile', user.username)
      else:
          form = PasswordChangeForm(user)
      context = {
          'form': form,
      }
      return render(request, 'accounts/change_password.html', context)
  
  
  @require_POST
  def delete(request):
      # 회원정보 삭제는, 타인이 아닌 본인에 의해서만 가능
      user = request.user
      if user.is_authenticated:
          user.delete()
      return redirect('articles:index')
  
  
  @require_http_methods(['POST', 'GET'])
  def login(request):
      if request.user.is_authenticated:
          return redirect('articles:index')
      
      if request.method == 'POST':
          # AuthenticationForm => 일반 Form
          form = AuthenticationForm(request, request.POST)
          if form.is_valid(): # authenticate(id, pw) => 맞으면, user 객체를 반환
            user = form.get_user()
            auth_login(request, user) # auth_login => session, cookie 세팅
            return redirect(request.GET.get('next') or 'articles:index')
      else:
          form = AuthenticationForm(request)
      context = {
          'form': form,
      }
      return render(request, 'accounts/login.html', context)
    
  
  def logout(request):
      if request.user.is_authenticated:
          auth_logout(request) # auth_logout => session, cookie 날리기
      return redirect('articles:index')
  ```

- accounts/login.html, accounts/signup.html, accounts/update.html, accounts/change_password.html

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>Login</h1>
    <form method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <button>로그인</button>
    </form>
  
  {% endblock content %}
  ```

- accounts/profile.html

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
  
  <h1>{{ user.username }}</h1>
  {% comment %} 
    user => 프로필의 주인
    request.user => 화면을 보고 있는 '나'
  {% endcomment %}
  
  <ul>
    <li>{{ user.email }}</li>
  
    {% if user == request.user %}
      <li>
        <a href="{% url 'accounts:update' %}"><button>회원 정보 변경</button></a>
      </li>
  
      <li>
        <a href="{% url 'accounts:change_password' %}"><button>비밀 번호 변경</button></a>
      </li>
  
      <li>
        <form action="{% url 'accounts:delete' %}" method="POST">
          {% csrf_token %}
          <button>회원탈퇴</button>
        </form>
      </li>
    {% endif %}
    </ul>
  
  {% endblock content %}
  ```

  
