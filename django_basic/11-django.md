# Django[2021.10.18]



## 1. Model Relationship(1)

- Foreign Key

  - 외부키

  - 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행(PK)을 식별할 수 있는 키

  - 여러개의 참조하는 테이블의 행이 참조되는 테이블의 동일한 행을 참조할 수 있다.

    ex) 하나의 게시글에는 여러개의 댓글이 달릴 수 있음.

  - 참조하는 모델에서의 외래키(FK)는 참조되는 모델의 기본키(PK)를 가리킴

    중복되지 않게 하기 위해 PK를 가리키고 있음(유일한 값 - 참조 무결성)

    자식 테이블의 FK -> 부모 테이블의 PK

- ForeignKeyField

  - Many to one relationship(1:N)

  - 2개의 위치인자가 반드시 필요

    1. 참조하는 model class
    2. on delete 옵션 = 외래키가 참조하는 객체가 사라졌을 때 외래키를 가진 객체를 어떻게 처리할 지를 정의

  - 작성방법

    - ```python
      # articles/models.py
      
      class Comment(models.Model):
          # FK를 작성하는 곳은 1:N중 N쪽에서 작성!!
          article = models.ForeignKey(Article, on_delete=models.CASCADE)
          content = models.CharField(max_length=200)
          created_at = models.DateTimeField(auto_now_add=True)
          updated_at = models.DateTimeField(auto_now=True)
      
          def __str__(self):
              return self.content
      ```

    - ![캡처2](https://user-images.githubusercontent.com/73927750/137666278-b839bf83-fb29-473d-be0e-63fd556307d0.JPG)

    - 댓글 작성 순서

      - Comment의 article에 원하는 Article의 객체자체를 넣어준다.
      - ![캡처4](https://user-images.githubusercontent.com/73927750/137666540-ebee15aa-5d99-4f17-96a3-5a532638a8b5.JPG)
      - 두 번째 댓글 추가
      - ![캡처5](https://user-images.githubusercontent.com/73927750/137666592-a95c8b4c-26a7-474f-942c-907b577060df.JPG)

  - 참조

    - N -> 1
    - Comment(N) -> Article(1)
    - 댓글의 경우 반드시 자신이 참조하고 있는 게시글이 있으므로 comment.article과 같이 접근할 수 있음
    - 늘 하던대로 객체 참조하면 됨

  - 역참조

    - Article(1) - > Comment(N)

    - 실제로 Article 클래스에는 Comment와 어떠한 관계도 작성되어 있지 않음

      -> article.comment 처럼 접근 할 수 없음

      -> article.comment_set manager가 생성됨

    - ![캡처3](https://user-images.githubusercontent.com/73927750/137666610-07facb55-09e8-49d7-876f-a0606d271447.JPG)

    - ForeignKey에서(Article, on delete='', related='comments')

      -> related='comments'를 설정하면 comment_set 대신 comments로 사용가능

## 

## 2. Comment CREATE, READ, DELETE

- comment 또한 form이 필요한 model이기 때문에 ModelForm을 이용해서 만들어준다.

  ```python
  # articles/forms.py
  
  from django import forms
  from django.db.models import fields
  from .models import Article, Comment
  
  class CommentForm(forms.ModelForm):
       
      class Meta:
          model = Comment
          # fields = '__all__' -> 외래키 필드인 article_pk는 가져올 필요 없음 -> content만
          exclude = ('article', )
  ```

- views.py

  ```python
  # articles/views.py
  
  
  # ======================= READ =======================
  @require_safe
  def detail(request, pk):
      article = get_object_or_404(Article, pk=pk)
      comment_form = CommentForm()
      # 해당 article에 해당하는 모든 comment들을 가져온다(.comment_set.all() = QuerySet)
      comments = article.comment_set.all()
      context = {
          'article': article,
          'comment_form': comment_form,
          'comments': comments,
      }
      return render(request, 'articles/detail.html', context)
  
  
  # ======================= CREATE =======================
  @require_POST
  def comments_create(request, pk):
      if request.user.is_authenticated:
          article = get_object_or_404(Article, pk=pk)
          comment_form = CommentForm(request.POST)
  
          if comment_form.is_valid():
              # save를 바로 할 수 없음 => commit=False을 하면 바로 save하지 않고 일단 comment객체를 return해줌
              comment = comment_form.save(commit=False)
              comment.article = article
              # comment save!!
              comment.save()
          return redirect('articles:detail', article.pk)
      return redirect('accounts:login')
  
  
  # ======================= DELETE =======================
  @require_POST
  def comments_delete(request, article_pk, comment_pk):
      if request.user.is_authenticated:
          comment = get_object_or_404(Comment, pk=comment_pk)
          comment.delete()
      return redirect('articles:detail', article_pk)
  
  # ======================= UPDATE =======================
  # JS활용!
  
  ```

- articles/templates/articles/detail.html

  ```html
  # articles/templates/articles/detail.html
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h2>DETAIL</h2>
    <h3>{{ article.pk }} 번째 글</h3>
    <hr>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성시각 : {{ article.created_at }}</p>
    <p>수정시각 : {{ article.updated_at }}</p>
    <hr>
    <a href="{% url 'articles:update' article.pk %}">[UPDATE]</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
    <a href="{% url 'articles:index' %}">[back]</a>
    
    <hr>
    <h4>댓글 목록</h4>
    {% if comments %}
  	# DTL 사용 (|)
      <p><b>{{ comments|length }}개의 댓글이 있습니다.</b></p>
    {% endif %}
    <ul>
      {% for comment in comments %}
        <li>
          {{ comment.content }}
          <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
            {% csrf_token %}
            <input type="submit" value="DELETE">
          </form>
        </li>
      {% empty %}
        <p>댓글이 없어요...</p> 
      {% endfor %}
    </ul>
  
  
    <hr>
    <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit">
    </form>
  {% endblock content %}
  ```

  

## 3. Customizing authentication in Django

- Substituting a custom User model

  - User모델 대체하기 -> 사이트마다 인증 요구사항이 다를 수 있음

  - 커스텀 유저 모델을 설정하는 것을 강력하게 권장함!!!(그냥 무조건 하기) -> 재정의

  - AUTH_USER_MODEL

    - settings.py에 있음
    - 무조건 첫 번째 migrations에서 적용해야함(프로젝트를 시작하면 무조건 맨 처음에!!!)
    - 기본값 : auth.User -> my_app.User

  - Custom User 정의하기

    1. db.sqlite3 파일 삭제

    2. migrations 파일 삭제

    3. settings.py

       ```python
       # settings.py
       
       # AUTH_USER_MODEL = 'auth.User'
       # -> default는 auth.User임 하지만 커스터마이징!
       AUTH_USER_MODEL = 'accounts.User'
       ```

    4. accounts/models.py

       ```python
       # accounts/models.py
       
       from django.db import models
       from django.contrib.auth.models import AbstractUser
       
       # 일단 설정해놓고 나중에 필요하면 활용
       class User(AbstractUser):
           pass
       ```

    5. admin

- Custom user & Built-in auth forms

  - AUTH_USER_MODEL이 auth.User -> my_app.User 때문에 기존의 Built-in forms에서 에러발생

    -> UserCreationForm과 UserChangeForm이 기존 내장 User 모델을 사용한 ModelForm이기 때문에 Custom User모델로 대체

  - ```python
    # accounts/forms.py
    
    from django.contrib.auth.forms import UserChangeForm, UserCreationForm
    from django.contrib.auth import get_user_model
    
    class CustomUserChangeForm(UserChangeForm):
    
        class Meta:
            # get_user_model()을 사용해서 직접 User을 참조하지 말고 현재 활성화 되어 있는 UserModel을 참조해라
            model = get_user_model()
            fields = ('email', 'first_name', 'last_name',)
    
    
    class CustomUserCreationForm(UserCreationForm):
    
        class Meta(UserCreationForm.Meta):
            model = get_user_model()
            fields = UserCreationForm.Meta.fields + ('email',)
    ```

  - get_user_model()

    - from django.contrib.auth import get_user_model
    - 현재 프로젝트에서 활성화된 사용자 모델을 반환
    - django에서는 직접 User클래스를 참조하지 말 것을 강조 -> get_user_model() 활용!! 



## 4. Model Relationship(2)

- User - Article(1:N)
- Article - Comment(1:N)
