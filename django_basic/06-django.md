# Django[2021.09.07]

## 1. views.py

```python
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.shortcuts import redirect, render, get_object_or_404
from .models import Article
from .forms import ArticleForm

# 사용자가 HTML을 받기 위해 필요
# def new(request):
#     # <form> 내부의 HTML 만들기
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)

# 사용자가 데이터를 제출 + 저장하기 위해 사용
# def create(request):
#     form = ArticleForm(request.POST)
#     # 데이터 검증(+ HTML)
#     if form.is_valid():
#         article = form.save() # ModelForm이라 .save() 가능(그냥 Form이면 불가능)
#         return redirect('articles:detail', article.pk)
#     else:
#         # <form> 내부의 HTML 만들기 + valid를 실패했을 경우 에러메세지를 포함해서 render한다(만약에 redirect로 보내면 에러메세지가 안보임)
#         context = {
#             'form': form,
#         }
#         return render(request, 'articles/new.html', context)


# new와 create를 하나로 합치기(분기문 이용)
@require_http_methods(['POST', 'GET'])
def create(request):
    # 5. 사용자가 데이터 입력 & POST/articles/create로 요청 -> 데이터가 invalid라고 가정
    # 10. 사용자가 데이터 입력 & POST/articles/create로 요청 -> 데이터가 valid라고 가정
    if request.method == 'POST':
        # 6. 데이터를 검증할 ArticleForm 인스턴스 초기화 -> 내용 있음
        # 11. 데이터를 검증할 ArticleForm 인스턴스 초기화 -> 내용 있음
        form = ArticleForm(request.POST)
        # 7. 데이터 검증(+ HTML) -> 실패
        # 12. 데이터 검증(+ HTML) -> 성공
        if form.is_valid():
            # 13. form을 통해 데이터 저장
            article = form.save()  # ModelForm이라 .save() 가능(그냥 Form이면 불가능)
            # 14. /articles/<pk>/ 로 redirect 하도록 응답
            return redirect('articles:detail', article.pk)
    # 1. GET/articles/create로 빈 HTML을 요청함
    else:
        # 2. 비어있는 ArticleForm 인스턴스 초기화 -> 빈 HTML 생성
        form = ArticleForm()

    # 3. 빈 form을 context에 담음
    # 8. 에러메세지를 담은 form을 dontext에 담음
    context = {
        'form': form,
    }
    # 4. 사용자에게 빈 form을 제공
    # 9. 에러메세지를 포함한 form 제공
    return render(request, 'articles/form.html', context)


@require_safe
def index(request):
    # pk 내림차순 정렬
    articles = Article.objects.order_by('-pk')
    # 가장 마지막에 수정된 article가 맨 위에 오도록
    # articles = Article.objects.order_by('-updated_at')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# 500에러 = 개발자 잘못
@require_safe
def detail(request, article_pk):
    # 만약에 찾는 데이터가 없으면 404에러(사용자가 잘못 검색함~)
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_http_methods(['POST', 'GET'])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/form.html', context)


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')
```



## 2. templates/articles/form.html

```html
{% comment %} form 의 action에 아무것도 없다면 현재 요청된 url로 돌아간다 
-> create와 update를 하나로 합칠 수 있다(이 둘은 같은 역할을 하니까!) {% endcomment %}
<form method="POST">
  {% csrf_token %}

  {% comment %} form은 input관련해서만 생성 {% endcomment %}
  {{ form.as_p }}

  <button>제출</button>
</form>
```

- action에 url이 없을 경우에는 요청이 왔던 주소로 돌아간다는 점을 이용해서 form의 action을 없애고 create와 update를 하나도 합친 form.html을 활용

  -> 하지만 method="POST"는 있어야함
