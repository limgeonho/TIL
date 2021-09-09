# Django[2021.09.08]

## 1. Static file

- 정적파일(우리회사 로고 등... 회사입장에서 미리 준비하는 것)

- 응답할때 별도의 처리없이 파일 내용을 그대로 보여주면 되는 파일

- static file의 구성

  1. django.contrib.staticfiles이 INSTALLED_APPS에 있는지 확인 - 기본적으로 되어있음

  2. settings.py에서 STATIC_URL을 정의 - 기본적으로 되어있음

  3. 템플릿에서static 템플릿 태그를 사용하여 지정된 상대경로에 대한 URL을 빌드

     -> {% load static %}

  4. 앱의 static폴더에 정적 파일을 저장

- load

  - 사용자 정의 템플릿 태그 세트를 로드
  - 로드하는 라이브러리, 패키지에 등록된 모든 태그와 필터를 로드

- static

  - STATIC_ROOT에 저장된 정적 파일에 연결

- STATIC_ROOT

  - django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로

  - settings.py의 DEBUG값이 TRUE로 설정되어 있으면 해당 값은 적용되지 않음

  - 배포할 때 사용함

    - 나중에 app별로 흩어져있는 static파일들을 모아둘 폴더를 지정하는 것임

  - 수집하는 방법

    ```python
    # settings.py
    
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    # 배포시에 app들의 static file들을 staticfiles에 모으는 명령
    # -> python manage.py collectstatic
    ```

- STATIC_URL

  - 개발단계에서는 실제 정적 파일들이 저장되어 있는 app/static/경로 및 STATICFILES_DIRS에 정의된 추가 경로들을 탐색함
  - 실제 파일이나 디렉토리가 아니며, URL로만 존재

- STATICFILES_DIRS

  - 프로젝트 폴더 하위에 만든 static 파일 폴더(앱 전체에서 공유할 이미지... 로고)를 자동으로 검색하게 하려면

    -> base.html이 있는 templates처럼 settings.py에 등록해야함

    - ```python
      # settings.py
      
      STATIC_URL = '/static/'
      # BASE_DIR / '<추가 경로 이름>'
      STATICFILES_DIRS = [
          BASE_DIR / 'static',
      ]
      # BASE_DIR / 'templates'와 같은 맥락임
      ```

- STATIC_URL과 STATIC_URL설정방법

- ```html
  # STATIC_URL
  # articles아래에 static/articles폴더 생성 -> img파일 넣기
  # templates에 html넣는 방법과 동일함
  {% extends 'base.html' %}
  # 반드시 설정해줘야함
  {% load static %}
  
  {% block content %}
    # url형식과 비슷
    <img src="{% static 'articles/sample.jpg' %}" alt="sample image">
  {% endblock content %}
  ```

- ```python
  # settings.py
  
  STATIC_URL = '/static/'
  STATICFILES_DIRS = [
      BASE_DIR / 'static',
  ]
  ```



## 2. Media file

- 미디어 파일(사용자가 추가하는 파일들...)

- 사용자가 웹에서 업로드하는 정적 파일

- ImageField

  - 이미지 업로드에 사용되는 모델 필드
  - FileField를 상속받음
  - 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사함
  - ImageField의 인스턴스는 최대 길이가 100자인 문자열로 DB에 저장된다
  - Pillow 라이브러리 필요
    - pip install pillow

- FileField

  - 파일 업로드에 사용되는 모델 필드

  - upload to=''

    1. 문자열 값이나 경로 지정
    2. 함수 호출

    - ```python
      # views.py
      
      from django.db import models
      
      # upload_to : 함수호출방식 -> 원하는 방식으로 custom해서 media/user_<pk>로 폴더 생성 후 저장
      def articles_image_path(instance, filename):
          return f'user_{instance.pk}/{filename}'
      
      class Article(models.Model):
          title = models.CharField(max_length=10)
          content = models.TextField()
          #########################################################################
          # upload_to : 문자열 값이나 경로 지정
          # image = models.ImageField(blank=True, upload_to='images/') -> media/images
          # image = models.ImageField(blank=True, upload_to='%Y/%m/%d/') -> media/2021/01/01
          #########################################################################
          # upload_to : 함수호출방식
          # image = models.ImageField(blank=True, upload_to=articles_image_path) 
          # -> media/user_<pk>
          #########################################################################
          created_at = models.DateTimeField(auto_now_add=True)
          updated_at = models.DateTimeField(auto_now=True)
      
          def __str__(self):
              return self.title
      ```

    - MEDIA_ROOT/`<upload_to='name'>` 형식으로 만들어진 폴더에 이미지가 저장된다.

  - blank=True

    -> form의 유효성검사에서 빈 문자열로 통과 가능(사용자가 이미지를 추가하지 않을 수도 있으니까)

  - null=True

    -> (' ')빈 문자열이 아닌 그냥 데이터가 없다고 알려줌

    -> CharField나 TextField와 같은 문자열 기반 필드에는 사용하는 것을 피해야함(blank=True 사용하자...)

  - blank vs null

    - blank = Validation-related -> form에서 빈 값 허용(유효성 검사)

    - null = Database-related(DB 유효성 검사)

      -> 결론 : 문자열 기반 필드 : blank=True

    - ```python
      # models.py
      
      class Person(models.Model):
      	# null=True 금지(텍스트 기반이기 때문에)
      	bio = models.TextField(max_length=50, blank=True)
      	
      	# null, blank 모두 설정 가능 -> 문자열 기반 필드가 아니기 때문
      	birth_date = models.DateField(null=True, blank=True)
      ```

- MEDIA_ROOT

  - 사용자가 업로드 한 파일들을 보관할 디렉토리 절대 경로
  - 성능을 위해 직접 파일을 저장하는 것이 아니라 파일의 경로를 저장함
  - MEDIA_ROOT = BASE_DIR / '<사진첩 이름>'

- MEDIA_URL

  - MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL
  - 업로드 된 파일의 주소를 만들어주는 역할

- MEDIA_ROOT 과 MEDIA_URL

  - ```python
    # settings.py
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media' -> 추가
    
    # url.py에 추가
    from django.contrib import admin
    from django.urls import path, include
    from django.conf import settings
    from django.conf.urls.static import static
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('articles/', include('articles.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 추가
    ```

  

  ## 3. 이미지 업로드(CREATE)

  - pip install pillow

  - ImageField(upload='') 이용

  - ```python
    # models.py에 ImageField추가
    
    image = models.ImageField(blank=True, upload_to='images/')
    # upload_to='images/'
    # -> saved to 'MEDIA_ROOT/images'
    # blank=True
    # -> 사용자가 이미지를 입력하지 않으면 빈문자열
    # -> ''로 유효성검사 통과가능
    ```

  - form 요소 - enctype속성 설정

    - enctype="multipart/form-data" -> 반드시 작성

    - 파일/이미지 업로드 시에 만드시 사용해야함(전송되는 데이터의 형식을 지정)

    - `<input type="file">`을 사용할 경우에 사용

    - ```html
      <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
      ```

  - 추가적으로 views.py 안에 있는 create함수를 변경해야함

    -> 이미지 URL은 request.POST에 저장되는 것이 아니라

    -> request.FILES에 저장되기 때문에 추가해 줘야함

    - ```python
      # views.py
      @require_http_methods(['GET', 'POST'])
      def create(request):
          if request.method == 'POST':
              # request.FILES 추가!!!
              form = ArticleForm(request.POST, request.FILES)
              if form.is_valid():
                  article = form.save()
                  return redirect('articles:detail', article.pk)
          else:
              form = ArticleForm()
          context = {
              'form': form,
          }
          return render(request, 'articles/create.html', context)
      ```

  - 이미지는 결국 DB에 파일이 저장되는 것이 아니라 경로가 저장되는 것이다!!!

  - 마지막으로 사진을 업로드하면 MEDIA_ROOT/images/ 에 이미지 파일들이 저장된다.

    -> images == upload_to='images/'

## 

## 4. 이미지 업로드(READ)

- 이미지 경로 불러오기
  - article.image.url == 업로드 파일의 경로
  - article.image == 업로드 파일의 이름
  - `<img src="{{ article.image.url }}" alt="{{ article.image }}">`



## 5. 이미지 업로드(UPDATE)

- 이미지는 바이너리 데이터이기 때문에 텍스트처럼 일부만 수정이 불가능

  -> 덮어 쓰기 방식으로 수정

  -> 덮어서 새로 저장하는 것이기 때문에 `<form>`안에 enctype="multipart/form-data" 필수!

- 추가적으로 사용자가 이미지를 등록하지 않았다면 create할때는 나타나지 않았지만 다시 detail페이지로 갔을때 나타나는 오류를 수정(분기문 이용)

- ```python
  # views.py
  
  @require_http_methods(['GET', 'POST'])
  def update(request, pk):
      article = get_object_or_404(Article, pk=pk)
      if request.method == 'POST':
          # request.FILES -> 이미지의 주소는 여기에 있음
          form = ArticleForm(request.POST, request.FILES, instance=article)
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

- ```html
  # detail.html
  
  {% extends 'base.html' %}
  {% load static %}
  
  {% block content %}
    <img src="{% static 'articles/sample.jpg' %}" alt="sample image">
  
    <h2>DETAIL</h2>
    <h3>{{ article.pk }} 번째 글</h3>
    
    # 기존에 설정한 이미지가 있다면 해당 이미지를... 없다면 기본 이미지를 넣어준다 
    {% if article.image %}
      <img src="{{ article.image.url }}" alt="{{ article.image }}">
    {% else %}
    	# 사용자가 기존에 등록한 이미지가 없다면 default이미지를 보여준다
      <img src="{% static 'images/default.jpg' %}" alt="{{ article.image }}">
    {% endif %}
  ```

  

## 6. 이미지 Resizing

- 실제 원본 이미지를 서버에 그대로 업로드 하는 것은 서버의 부담이 큰 작업

- `<img>`에서 직접 사이즈를 조정할 수도 있지만(width, height)

- 업로드 할 때 이미지 자체를 resizing하는 것

- django-imagekit 라이브러리 활용

  - pip install django-imagekit
  - INSTALLED_APPS = ['imagekit',] -> 등록

- 이미지의 크기를 조절하는 다양한 방법이 존재

- ```python
  from django.db import models
  # 아래 2가지 import
  from imagekit.models import ProcessedImageField, ImageSpecField
  from imagekit.processors import ResizeToFill
  
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
      ##############################################################################
      # image = ProcessedImageField(
      #     upload_to='thumbnails/',
      #     processors=[ResizeToFill(100, 50)],
      #     format='JPEG',
      #     options={'quality': 60}
      # )
      ##############################################################################
      image = models.ImageField(blank=True, upload_to='origins/')
      # detail.html도 변경해야함(<img src="{{ article.image_thumbnail.url }}" alt="{{ article.image_thumbnail }}">)
      image_thumbnail = ImageSpecField(
          source='image',
          processors=[ResizeToFill(100, 50)],
          format='JPEG',
          options={'quality': 90},
      )
      ##############################################################################
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return self.title
  
  ```

- ```html
  # detail.html
  
  {% extends 'base.html' %}
  {% load static %}
  
  
  {% block content %}
    <img src="{% static 'articles/sample.jpg' %}" alt="sample image">
  
    <h2>DETAIL</h2>
    <h3>{{ article.pk }} 번째 글</h3>
    
     # 기존에 설정한 이미지가 있다면 해당 이미지를... 없다면 기본 이미지를 넣어준다 
    {% if article.image %}
      <img src="{{ article.image_thumbnail.url }}" alt="{{ article.image_thumbnail }}">
    {% else %}
      <img src="{% static 'images/sample3jpg.jpg' %}" alt="{{ article.image }}">
    {% endif %}
  ```

