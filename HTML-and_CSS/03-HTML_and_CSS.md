# HTML_and_CSS[2021.08.04]

## 1. CSS Layout

- display
- position
- float
- flexbox
- bootstrap grid system.

## 2. CSS Float Layout

- float = 두둥실 뜬다

- 한 요소가 정상 흐름으로부터 빠져 텍스트 및 인라인 요소가 그 주위를 감싸 해당 요소의 좌, 우측을 따라 배치되는 것

- none = 기본값

  left : 요소를 왼쪽으로 띄움
  right : 요소를 오른쪽으로 띄움

- float를 사용하면 block요소로 인해 올라오지 못하는 요소들을 옆으로 올라오게할 수 있음

- 원래는 이미지에만 적용하려고 사용했지만 이 후에는 다른 요소들의 배치에 사용
  => 모든 요소가 float를 감싸는것이 아니라 텍스트나 inline요소가 감싸는 것임

- float의 clearfix
  float설정한 요소때문에 아래에 있는 또 다른 요소가 따라 올라올때 가상의 벽을 만드는 행위(못 올라오게 하기위해서)
  float된 요소의 부모에 작성

```python
.clearfix::after {
      content: "";
      display: block;
      clear: both;
    }
```

- => float는 과거에 grid와 flexbox가 나오기 전에 사용했음... => 그래도 여전히 쓰이긴함.

## 3. CSS Flexible Box Layout

- float 및 positioning 밖에 없었기 때문에 한계가 있었음
  => flexbox 등장 => 정렬 짱!

- 단방향 레이아웃

- **요소 + 축
  요소
  1. flex container(부모요소)
  2. flex item(자식요소)

  축

  1. main axis(메인축)
  2. cross axis(교차축)

- flex container(부모요소)

  flexbox 레이아웃을 형성하는 기본적인 모델
  flexitem들이 놓여있는 영역
  display: flex or display: inline-flex로 지정
  => flexitem들을 control 함

- flex-direction : 메인축의 방향을 가로로할지 세로로할지 설정(row, row-reverse, column, column-reverse)

- justify-content : 메인축 방향 정렬

- align-items, align-self, align-content : 교차축 방향 정렬(content-여러 줄, items-한 줄, self-개별요소)

- flexbox안에 flexbox를 또 선언할 수 있음
  다양한 메인축 방향이 존재할 수 있기 때문에 flexbox를 만날때마다 메인축 방향을 반드시 알고 있어야 한다.

- display: flex

  - 정렬하려는 부모 요소에 작성

- flex-direction

  - item이 쌓이는 방향 설정
  - main-axis가 변경됨
  - row(기본), row-reverse, column, column-reverse

- flex-wrap

  - 요소들이 강제로 한 줄에 배치 되게 할 것인지 여부 설정
  - nowrap(기본) - 전부 한 줄로(넘쳐도 그냥 튀어나옴), wrap - 넘치면 다음줄로, wrap-reverse - 넘치면 그 윗줄(역순)

- flex-flow

  - flex-direction과 flex-wrap의 shorthand

- justify-content

  - main-axis 정렬
  - flex-start, flex-end, center, space-between, space-around, space-evenly

- align-items

  - cross-axis 정렬
  - stretch(늘리기), flex-start, flex-end, center, baseline(item 내부의 text에 기준선)

- align-self

  - 개별 item에 적용하는 속성
  - auto(기본)
  - align-items와 동일함

- order

  - 작은 숫자 일수록 앞으로 이동(우선 쌓이는 방향)
  - 0(기본)

- flex-grow

  - 주축에서 남는 공간을 항목들에게 분배하는 방법
  - 아이템의 상대적 비율이 아님
  - 0(기본)

## 4. Bootstrap

- 프론트엔드 라이브러리 1등
- 라이브러리안에 클래스들로 적용해 놨음 - 엄청 길게...

- 추가

```html
<link rel="stylesheet" href="bootstrap.css">
<script src="bootstrap.bundle.js"></script>
```

- 매번 파일로 bootstrap를 추가하지말고 
  => bootstrap사이트에 있는 CDN파일을 복붙해서 사용한다.

- CDN = content delivery network
  세계 곳곳에 있는 분산 서버를 이용해서 사용자의 물리적 위치와 가까운 곳에 있는 서버를 이용해서 접근, 제공
  사용자와 가까운 서버를 통해 빠르게 전달 가능
  외부 서버를 사용하기 때문에 회사에서도 서버부하가 적어짐

- 같은 파일이더라도 각각의 브라우저에 따라 약간씩 다르게 나타난다
  => css / reset, normalize를 해야한다.(초기화) - 각각의 브라우저의 기본 값을 통일시켜준다.
  => 하지만 bootstrap를 사용하면 자동으로 초기화를 해준다

- 모든 브라우저는 각자의 `user agent stylesheet` 를 가지고 있는데 

  (웹사이트를 보다 읽기 편하게 하기 위해)

  문제는 이 설정이 브라우저마다 상이하다는 것

  모든 브라우저에서 웹사이트를 동일하게 보이게 만들어야하는 개발자에겐 골치거리

- Normalize CSS

  gentle solution

  W3C의 표준을 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정한다.

  경우에 따라 IE 또는 EDGE 는 표준에 따라 수정할 수 없는 경우도 있는데, 이 경우 Normalize 는 IE 또는 EDGE 의 스타일을 나머지 브라우저에 적용시킨다.

  실제 bootstrap 에서는 normalize.css를 자체적으로 커스텀해서 `bootstrap-reboot.css` 라는 이름으로 사용한다.

- Reset CSS

  aggressive solution

  브라우저의 기본 스타일이 전혀 필요 없다는 방식으로 접근한다.

  따라서 브라우저의 user agent와 함께 제공되는 모든 스타일을 재설정한다.

  Reset CSS의 문제점은 너무나 많은 선택자가 엉켜있고, 불필요한 오버라이드가 많이 발생하며 디버깅 시 제대로 읽을 수 없다.

- Grid system(12)
  => flexbox로 제작됨
- container => row => column
- Grid system
  1. 12개의 column
  2. 6개의 grid breakpoints
- 합이 12이기 때문에 안에서 원하는 만큼 약수를 이용해서 분할한다.
  12가 넘어가면 다음줄로 내려감
- 반드시 부모에 .row가 있어야 .col사용가능
- gutter = column사이의 padding라고 생각하면됨.
- col
  col의 max는 12
  백분율로 움직인다.
  내용은 column에 작성된다.
  오직 column만이 row의 자식이 될 수 있다.
- Grid breakpoints(6)
  다양한 디바이스에서 적용하기 위해 특정 px조건에 대한 지점을 정해둠 = breakpoint
  6개의 points가 있다.
  xs, sm, md, lg, xl, xxl
  col-<sm>-4
  => 해당 컬럼은 sm사이즈 범위내에서는 4칸을 차지한다.
- Nesting
  Grid system안에 또 다른 Grid system을 적용하는 것
  접어보기 기능을 활용해서 큰 틀부터 확인해나간다.
- Offset
  지정한 만큼의 column무시하고 다음 공간부터 나타나게함
  설정한 크기부터 나타나게 하는 것

> 각각의 기술은 저마다 용도와 장단점이 있기 때문에 어떤 기술도 독립적인 용도로 설계되지 않았다.
>
> => 많은 경험을 통해 어떤 상황에서 어떤 기술이 적합한지에 대해 적절하게 선택하는 능력을 길러야 한다.
