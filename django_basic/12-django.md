# Django[2021.10.20]



## 1. Model Relationship(3)

- M : N 관계

  - ManyToManyField

  - ```python
    # hospital/models.py
    # 1 : N => 모델관계!!
    from django.db import models
    
    class Doctor(models.Model):
        name = models.TextField()
    
        def __str__(self):
            return f'{self.pk}번 의사 {self.name}'
    
    
    class Patient(models.Model):
        name = models.TextField()
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'
    ```

  - ![캡처1](https://user-images.githubusercontent.com/73927750/138058081-cb5d47db-0c57-470e-b364-2220b0276222.JPG)

  - 1 : N의 한계

    - 새로운 예약을 생성하는 것이 불가능(아예 새로운 객체를 생성해야함)
    - 여러 의사에게 진료받은 기록을 환자 한 명에 저장할 수 없음(DB에는 1,2 형식 사용 불가)

  - 환자는 여러 의사에게 예약을 할 수 있음 + 의사도 여러 환자를 진료할 수 있음

    -> 1 : N의 관계가 아닌 M : N관계임!

    

  - 중개 테이블로 해결

  - ```python
    # hospital/models.py
    
    from django.db import models
    
    class Doctor(models.Model):
        name = models.TextField()
    
        def __str__(self):
            return f'{self.pk}번 의사 {self.name}'
    
    
    class Patient(models.Model):
        name = models.TextField()
        # 외래키 삭제
    
        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'
    
    # 중개모델 작성
    class Reservation(models.Model):
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
        patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
        def __str__(self):
            return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
    ```

  - ![캡처4](https://user-images.githubusercontent.com/73927750/138059184-34a92d59-aca7-4df5-80e6-2bc5a05c9c25.JPG)

  

  - => ManyToManyField 필요!!!(중개 모델 삭제!)

  - ManyToManyField

    - Doctor이나 Patient에서 모두 작성 가능

    - ```python
      # hospital/models.py
      
      from django.db import models
      
      
      class Doctor(models.Model):
          name = models.TextField()
      
          def __str__(self):
              return f'{self.pk}번 의사 {self.name}'
      
      
      class Patient(models.Model):
          doctors = models.ManyToManyField(Doctor, through='Reservation')
          name = models.TextField()
      
          def __str__(self):
              return f'{self.pk}번 환자 {self.name}'
      
      
      class Reservation(models.Model):
          doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
          patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
          symptom = models.TextField()
          reserved_at = models.DateTimeField(auto_now_add=True)
      
          def __str__(self):
              return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
      ```

    - ![캡처3](https://user-images.githubusercontent.com/73927750/138102326-4c1d006d-ec4d-4455-9d7e-753180c4dc48.JPG)

  

- 1 : N 인지 아니면 M : N 인지를 구분해야함

- Related Manager

  - add() - 지정된 객체 집합에서 지정된 모델 객체를 추가
  - remove() - 지정된 객체 집합에서 지정된 모델 객체를 삭제

- ManyToManyField Arguments

  - related name = 역참조하는 모델이 해당 모델을 사용할 때 이용할 이름설정

    ```python
    class Patient(models.Model):
        doctors = models.ManyToManyField(Doctor, related_name='patients')
        # doctor1.patient_set.all() 이 아닌 doctor1.patients.all() 를 사용!!    
    ```

  - through = 중개 테이블을 직접 작성하는 경우, through를 통해 중개 테이블을 나타내는 django 모델을 지정할 수 있음

  - symmetrical 

    ManyToManyField 가 동일한 모델을 가리키는 정의에서 사용(재귀, ex: 팔로우) 

    symmetrical = True 인 경우 person_set을 추가하지 않음(why? : 내가 너를 팔로우 하면 자동으로 너도 나를 팔로우 = 서로 자동 참조)

    => 이러한 대칭을 원하지 않는다면 symmetrical = False 로 설정

- 중개 테이블

  - 중개 테이블을 사용하는 이유?

    => 두 테이블의 단순한 연결이 아니고 추가적으로 ex) 생성일자, 수정일자 등 다른 요소들을 추가하고 싶으면 중개테이블의 컬럼에 추가



## 2. Like(좋아요) 구현

- 좋아요!

  - 유저는 여러 개시글에 좋아요 가능
  - 게시글은 여러 유저로부터 좋아요를 받을 수 있음

- ```python
  # articles/models.py
  
  from django.db import models
  from django.conf import settings
  
  
  class Article(models.Model):
      # models.py에서만 settings.AUTH_USER_MODEL사용 => 나머지는 get_user_model()사용!
      user = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
      # ManyToMany, 게시글 입장에서 보았을 때 나한테 좋아요를 누른 users
      # related_name='like_articles'을 설정하지 않을 경우 User에서 Article역참조 시에 위의 user과 중복으로 인해 에러 발생
      like_users = models.ManyToManyField(
          settings.AUTH_USER_MODEL, related_name='like_articles')
      title = models.CharField(max_length=10)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return self.title
  
  
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      user = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
      content = models.CharField(max_length=200)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return self.content
  ```

- ![캡처5](https://user-images.githubusercontent.com/73927750/138105360-0e3e5982-a283-4a03-a5a8-c2185b4a2222.JPG)

- ```python
  # articles/views.py
  
  @require_POST
  def likes(request, article_pk):
      if request.user.is_authenticated:
          article = get_object_or_404(Article, pk=article_pk)
  
          # 현재 좋아요를 요청하는 회원(request.user)이 해당 게시글의 좋아요를 누른 회원 목록에 있다면,
          # in 연산자 보다 QuerySet이 커지면 exists()가 더 빠름
          if article.like_users.filter(pk=request.user.pk).exists():
              # if request.user in article.like_users.all():
              # 좋아요 취소
              article.like_users.remove(request.user)
          else:
              # 좋아요 누름
              article.like_users.add(request.user)
          return redirect('articles:index')
      return redirect('accounts:login')
  ```

- ```html
  # templates/articles/index.html
  
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>Articles</h1>
    {% if request.user.is_authenticated %}
      <a href="{% url 'articles:create' %}">[CREATE]</a>
    {% else %}
      <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요.]</a>
    {% endif %}
    <hr>
    {% for article in articles %}
      <p>
        <a href="{% url 'accounts:profile' article.user.username %}">작성자 : {{ article.user }}</a>
      </p>
      <p>글 번호 : {{ article.pk }}</p>
      <p>글 제목 : {{ article.title }}</p>
      <p>글 내용 : {{ article.content }}</p>
      <div>
        <form action="{% url 'articles:likes' article.pk %}" method="POST">
          {% csrf_token %}
          {% if user in article.like_users.all %}
            <input type="submit" value="좋아요 취소">
          {% else %}
            <input type="submit" value="좋아요">
          {% endif %}
        </form>
      </div>
      <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
      <hr>
    {% endfor %}
  {% endblock content %}
  ```



## 3. Profile

- ```python
  # accounts/viewx.py
  
  def profile(request, username):
      # models.py가 아니기 때문에 User을 참조하기 위해서는 get_user_model()사용!
      person = get_object_or_404(get_user_model(), username=username)
      context = {
          'person': person,
      }
      return render(request, 'accounts/profile.html', context)
  ```

- ```html
  # templates/accounts/profile.html
  
  {% extends 'base.html' %}
  
  {% block content %}
    {% with followings=person.followings.all followers=person.followers.all %}
      <h1>{{ person.username }}의 프로필 페이지</h1>
  
      <div>
        <div>팔로잉 수 : {{ followings | length }} / 팔로워 수 : {{ followers | length }}</div>
      </div>
  
      {% if user != person %}
        <div>
          <form action="{% url 'accounts:follow' person.pk %}" method="POST">
            {% csrf_token %}
            {% if user in followers %}
              <input type="submit" value="언팔로우">
            {% else %}
              <input type="submit" value="팔로우">
            {% endif %}
          </form>
        </div>
      {% endif %}
    {% endwith %}
  
    <hr>
  
    <h2>{{ person.username }}가 작성한 게시글</h2>
    {% for article in person.article_set.all %}
      <div>{{ article.title }}</div>
    {% endfor %}
  
    <hr>
  
    <h2>{{ person.username }}가 작성한 댓글</h2>
    {% for comment in person.comment_set.all %}
      <div>{{ comment.content }}</div>
    {% endfor %}
    
    <hr>
  
    <h2>{{ person.username }}가 좋아요를 누른 게시글</h2>
    {% for article in person.like_articles.all %}
      <div>{{ article.title }}</div>
    {% endfor %}
    
    <a href="{% url 'articles:index' %}">[BACK]</a>
  
  {% endblock content %}
  ```



## 4. Follow

- follower와 following이 재귀적인 관계이기 때문에 User model을 수정!

  ```python
  # accounts/models.py
  
  from django.db import models
  from django.contrib.auth.models import AbstractUser
  
  
  class User(AbstractUser):
      followings = models.ManyToManyField(
          'self', symmetrical=False, related_name='followers')
  ```

- ```python
  # accounts/views.py
  
  # 좋아요와 같음!!!
  @require_POST
  def follow(request, user_pk):
      if request.user.is_authenticated:
          me = request.user
          you = get_object_or_404(get_user_model(), pk=user_pk)
          # person = get_object_or_404(get_user_model(), pk=user_pk)
  
          # 너와 내가 다른 사람이어야 팔로우를 진행할 수 있음(나 자신은 팔로우 불가)
          if me != you:
              # 내가 상대방의 팔로워 리스트에 있다면
              if you.followers.filter(pk=me.pk).exists():
                  # if request.user in person.followers.all():
                  # 언팔로우
                  you.followers.remove(me)
              else:
                  # 팔로우
                  you.followers.add(me)
          return redirect('accounts:profile', you.username)
      return redirect('accounts:login')
  ```

- templates/accounts/profile,html 와 같음...
