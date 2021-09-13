# Django[2021.09.10]



## 1. django form

- form의 역할
  1. validation - 중요!
  2. HTML(`<input>`)생성
- work flow(기억하기)
  - ![workflow](https://user-images.githubusercontent.com/73927750/133128794-e4c244ea-743e-4c43-ac9c-29416a81f37b.JPG)

- models.py에서 CharField(choices=)설정하기

  - ```python
    # models.py
    
    CATEGORY_CHOICES = [
        # (DB에 저장되는 값, 사용자가 보는 값)
        ('python', '파이썬'),
        ('web', '웹'),
        ('django', '장고'),
    ]
    
    class Question(models.Model):
        title = models.CharField(max_length=100)
        # choices=CATEGORY_CHOICES에 써주기
        category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    ```

- 추가적인 validation 설정하기

  - ```python
    # views.py
    
    @require_http_methods(['GET', 'POST'])
    def create(request):
        if request.method == 'POST':
            # 사용자가 전달한 데이터를 내가 확인하기는 좀 그러니까 -> QuestionForm가 대신 열어보고 valid한지 확인해줘!
            form = QuestionForm(request.POST)
            # valid하다면 확인된 깔끔한 데이터(cleaned_data : dict 형태) 중에 is_save의 상태를 보고 on이면 save()해줘! => 그러면 is_save는 어디에?? => forms.py에 직접 설정
            if form.is_valid():
                if form.cleaned_data['is_save']:
                    question = form.save()
                    return redirect('board:detail', question.pk)
                else:
                    return redirect('board:create')
        else:
            form = QuestionForm()
        context = {
            'form': form,
        }
        return render(request, 'board/form.html', context)
    ```

  - ```python
    # forms.py
    
    class QuestionForm(forms.ModelForm):
        """
        <추가적인 validation을 설정하는 방법!!!>
        title = forms.CharField(max_length=100, required=True)
        category = forms.CharField(max_length=100, required=True)
        content = forms.CharField(widget=forms.Textarea, required=True)
        => 자동으로 작성되어 있음 => 덮어 써야함
        """
    
        # model의 필드와 이름이 같다면, DB에 저장이 된다.
        title = forms.CharField(
            min_length=2,
            max_length=100,
            required=True
        )
    
        content = forms.CharField(
            widget=Textarea,
            required=True,
            min_length=2,
            max_length=10000
        )
    
        # model의 필드가 아니면 HTML + 검증은 하되 DB에 저장은 하지 않는다.
        is_save = forms.BooleanField(
            required=False, label='wanna save?', help_text='저장하려면 체크하세요')
    
        class Meta:
            model = Question
            # 아래 필드는 모델(models.py)에 있어야 하며,
            # 데이터 검증 + HTML생성을 합니다.
            fields = ('title', 'category', 'content')
            # exclude = ('field_a')
    
    ```

## 

## 2. static 

- 가장 먼저 settings.py에 등록하기

  - ```python
    # settings.py 
    STATIC_URL = '/static/'
    
    # static 파일을 찾을때 여기도 같이 찾아주세요~ => 홈파일 아래에 static~ 폴더가 있어야함
    STATICFILES_DIRS = [BASE_DIR / 'static', ]
    # 위의 설정이 없다면 django는 자동으로 app아래에 있는 static폴더에만 접근한다.
    ```

  -  ```html
     # base.html
     
     {% load bootstrap5 %}	# bootstrap5을 사용하겠다.
     {% load static %}	    # static을 사용하겠다.
     <!DOCTYPE html>
     <html lang="en">
     <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       # 홈폴더 아래에 있는 static/css~
       <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
       # app 아래에 있는 static/board/css~
       <link rel="stylesheet" href="{% static 'board/css/custom.css' %}">
     </head>
     <body>
       # 같은 templates에 있는 _navbar.html를 가져오겠다! => block와 비슷
       {% include '_navbar.html' %}
       <div class="container">
         {% block content %}{% endblock content %} 
       </div>
       <script src="{% static 'js/bootstrap.min.js' %}"></script>
     </body>
     </html>
     ```



## 3. Pagination

- views.py에서 index()에서 불러온다.

  - ```python
    # views.py
    
    from django.core.paginator import Paginator
    
    @require_safe
    def index(request):
        questions = Question.objects.order_by('-pk')
        # 한 페이지에 2개의 항목씩 가져온다!
        paginator = Paginator(questions, 2)
        # url에 ?page=<숫자> -> 숫자를 가져오는 것임
        page_number = request.GET.get('page')
        # 가져온 page 숫자에 해당하는 객체들을 가져온다
        page_obj = paginator.get_page(page_number)
        context = {
            # 해당 페이지에 존재하는 양만큼의 페이지 내용이 전달
            'page_obj': page_obj,
        }
        return render(request, 'board/index.html', context)
    ```

  - ```html
    # index.html
    
    {% extends 'base.html' %}
    {% load bootstrap5 %}
    {% block content %}
    
    <h1>index page</h1>
    <ul>
      # 해당 페이지에 존재하는 question만 가져옴
      {% for question in page_obj %}
      <li>
        <a href="{% url 'board:detail' question.pk %}">{{ question.title }}</a>
      </li>
      {% endfor %}
    </ul>
    
    <div class="d-flex justify-content-center">
      {% bootstrap_pagination page_obj %}
    </div>
    
    {% endblock content %}
    ```



## 4. 기타

- content에는 분명히 여러줄의 문장을 입력했지만 조회했을 경우 한줄로 나온다(입력한 양식대로 X)

  - ```html
    # detail.html
    
    # question.content 다음에 파이프(|)를 이용해서 linebreaksbr(한 줄씩 br)활용
    <p>{{ question.content|linebreaksbr }}</p>
    ```

    
