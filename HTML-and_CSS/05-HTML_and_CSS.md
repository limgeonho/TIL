# HTML_and_CSS[2021.08.06]

- 반응형 웹페이지 구성
- media query
- font-icon
- bootstrap
- css-specificity
- naming convention

## 1. media-query

- 미디어 쿼리 = 디바이스마다 다르게 나타나는(가로)화면의 구성을 하는 것

```html

@media (max-width: 500px) {
      h2 {color: green;}
    }
@media (orientation: landscape){
      p.orientation::after {content: '가로입니다.'}
    }

```

## 2. font-icon

- google font에서 다운로드

- font-awesome에서 다운로드

- bootstrap-icon에서 다운로드

- favicon = `<title>`옆에 있는 작은 아이콘

  favicon generator에서 다운로드

## 3. css-specificity

- css-specificity = 명시도
  => style를 지정하는 것마다 다른 우선 순위를 가진다.
  => 점수가 높은 항목이 브라우저에 나타난다.
  인라인, id, !important는 사용하지 말자...

## 4. naming convention

- BEM = block element modifier

- block = 혼자 독립적으로 사용할 수 있는 태그
  element = 반드시 block안에 소속되어서 세부적인 기능을 담당하는 태그(종속적)
  modifier = block나 element의 상태를 나타낼때

  => .block__element--modifier

- width에서 100%는 부모요소 안에서의 100%를 의미한다.

