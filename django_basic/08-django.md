# Django[2021.09.09]

## 1. static

```python
# settings.py 

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static',]  # 추가로 탐색해 주세요
```

```html
# base.html

<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
<script src="{% static 'js/bootstrap.min.js' %}"></script>
-> bootstrap 압축파일을 다운로드 받아서 프로젝트 내부에 저장하고 사용(BASE_DIR/static/css and js)
-> STATICFILES_DIRS = [BASE_DIR / 'static',] 이거 설정해야 사용가능
===============================================================================
# index.html

{% load static %}
{% load bootstrap5 %}
<img class="rounded mx-auto d-block" src="{% static 'articles/images/ssafy.png' %}" alt="ssafy banner">
-> app 내부의 static/articles/images 내부에 sample 이미지 저장(logo...)
-> 장고가 알아서 app안에 있는 static 파일에 접근해서 불러온다
```



## 2. mediafiles

```python
# settings.py 

# Media Files => master url에 추가 작업 필요
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # 여기에 media 파일을 모으겠습니다.
```

```python
# urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# import와 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 추가
```

```python
# models.py

from imagekit import processors
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail, ResizeToFill, ResizeToFit

class Article(models.Model):
    image = ProcessedImageField(
        upload_to='articles',
        blank=True,
        processors=[ResizeToFit(500, 500),],  # 가로/세로중에 더 긴 곳을 500에 맞추고 비율대로 축소/확대함
        format='JPEG',
        options={'quality': 100, }
    )
    thumbnail_image = ImageSpecField(
        source='image',
        processors=[Thumbnail(50, 50), ],
        format='JPEG', 
        options={'quaility': 50, }
    )
# ImageField나 resizing tool인 imagekit을 설치해서 사용자가 업로드한 이미지를 등록한다.
# pip install django-imagekit
# ImageField(upload_to='images') -> BASE_DIR/media/images에 이미지 url 모음(MEDIA_ROOT에서 설정함)
```

```html
# form.html

{% load bootstrap5 %}

<form method="POST" enctype="multipart/form-data">
  {% csrf_token %}
  {% bootstrap_form form %}
  {% buttons submit='제출' reset='재작성' %}{% endbuttons %}
</form>
-> 이미지를 넘기기 위해서는 반드시 enctype="multipart/form-data" 작성!! 
```

```python
# views.py

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        # <form>에서 온 이미지는 POST에 들어있지 않고 request.FILES에 들어있기 때문에 반드시 작성!! 
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    
    context = {'form': form, }
    return render(request, 'articles/form.html', context)
```



## 3. pagination

```python
# views.py

from django.core.paginator import Paginator

@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    
    # 한 페이지에 5개씩 가져올거임
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'articles/index.html', context)
```

```html
# index.html

<h1>Article Index</h1>

# 5개씩 가져올거임
{% for article in page_obj %}
<hr>
<div>
  <p>글 번호: {{ article.pk }}</p>
  <p>글 제목: {{ article.title }}</p>
  <p>
    # 썸네일 이미지가 존재한다면 썸네일 이미지를 보여주고 -> {{ article.thumbnail_image.url }} .url까지!!
    {% if article.thumbnail_image %}
    <img src="{{ article.thumbnail_image.url }}" alt="">
    # 존재하지 않는다면 default 이미지를 보여줌
    {% else %}
    <img width="50" src="https://image.shutterstock.com/image-vector/male-default-placeholder-avatar-profile-260nw-387516193.jpg" alt="placeholder">
    {% endif %}
  </p>
  <p>글 내용: {{ article.content }}</p>
  <p>
    <a href="{% url 'articles:detail' article.pk %}">
      [DETAIL]
    </a>
  </p>
</div>
{% empty %}
<div>
  No articles... YET!
</div>
{% endfor %}

# 페이지 아래쪽에 pagination (bootstrap으로)
<div class="d-flex justify-content-center">
  {% bootstrap_pagination page_obj  %}
</div>
```

```html
# detail.html

{% block content %}
<h1>{{ article.title }}</h1>

# content(TextField)에서 \n를 쳤을 경우 나중에 조회했을 때도 \n가 적용되게 하는 방법
# -> |linebreaksbr
<p>{{ article.content|linebreaksbr }}</p>
  
<div>
  # 이미지가 존재한다면(article.image) -> {{ article.image.url }} .url 작성!! 해서 보여주기 
  {% if article.image %}
    <img src="{{ article.image.url }}" alt="{{ article.image }}" width="300">
  {% endif %}
</div>
```

