# HTML_and_CSS[2021.08.02]

## 1. WEB

- 웹어플리케이션 개발을 하기 위해 공부

- sw 개발 방법 및 학습 과정을 익히기 위해 공부

- 웹 표준

  W3C < WHATWG(IT대기업들이 주도)

## 2. HTML(https://developer.mozilla.org/ko/docs/Web/HTML)

- Hyper Text MarkUp Language

  Hyper Text  = 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트 - hyperlink
  MarkUp = 텍스트에 크기를 변화시키고 역할과 의미를 부여한다
  MarkUp Language = 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

  => hyperlink를 통해서 약속된 명시언어로 표현한 것(구조를 잡는 것) - 프로그래밍언어 아님

- 웹 페이지를 작성하기 위한(구조를 잡기 위한)언어
  => 웹 컨텐츠의 *의미와 구조를 정의

- .html 확장자

- DOM 트리 구조(string 덩어리를 해석(구조화)한 결과)
  = Document Object Model = 태그별로 하나의 객체로 본다 = 문서에 접근할 때 각각의 태그에 접근해서 수정
  => 웹 페이지의 객체 지향 표현

- 2spaces로 들여쓰기 한다.

- html의 요소
  태그(요소)와 내용으로 구성되어 있다.

```html
<h1>contents</h1>
태그 = 역할 표시 기능
요소는 중첩될 수 있음
여는 태그와 닫는 태그의 쌍을 잘 확인해야함
```

- 속성
  태그별로 사용할 수 있는 속성은 다르다
  속성을 작성할 때는 공백X, " "사용(href="http://~")
  모든 태그에서 사용할 수 있는 태그도 존재함(global attribute : id, class...)
- ***https://developer.mozilla.org/ko/docs/Web/HTML***참고하기

```html
이 문서는 html5로 작성된 문서입니다.(브라우저에게...)
<!DOCTYPE html>
<html>
  <meta charset="UTF-8">
  <title>제목(브라우저 상단에 나옴)</title>
<head>
브라우저에 보이지는 않지만 body의 속성을 설정하는 부분
</head>

<body>
브라우저에서 보이는 내용부분
</body>

</html>
```

- 시맨틱 태그

  header, footer, aside...
  div, span와 같은 역할을 하지만 태그를 보고 대략적인 의미를 알 수 있다.
  단순히 구역을 나누는 것 뿐만 아니라 의미를 가지는 태그들을 활용하기 위한 노력

- 시맨틱 웹
  기존의 단순한 데이터의 집합이었던 웹페이지를 의미와 관련성을 가지는 거대한 데이터베이스로 구축하고자 하는 발상

- block vs inline

  block - 한 덩어리(높이와 폭이 존재함), 한 줄 전체를 차지함

  inline - 한 줄(높이가 있어보이지만 사실 높이X, 폰트사이즈는 조정O), 띄어쓰기로 작성 가능

- form태그

  action(반드시 존재해야함) - 어디로 보낼지 -> 아래의 submit을 통해 전달된다.

  method(GET, POST)

- label 태그

  for 속성은 id 중 같은 값과 연결한다
  ex) input id="1", label for="1" 처럼 같은 1을 공유하는 것 끼리 연결시킴

- input에서 type="submit" 을 설정해야 서버로 전달가능 

```html
<form action="#">
    <label for="name">이름</label>
    <input id="name" type="text">
</form>
label은 for가 name을 가지고 있기 때문에 같은 name을 id로 갖는 input태그와 연결된다.
```

## 3. CSS_1(basic)

- Cascading Style Sheet
- HTML에 붙어서 사용되기 때문에 구조화된 HTML문서가 반드시 필요하다(단독적으로 쓰일 수 없음)

```html
h1 {
	color: black;
	font-size: 10px;
}
선택자 {
  속성: 값; => 한 줄을 선언이라고함
  속성: 값;
}
```

- css정의 방법
  1. 해당 태그안에 직접 작성(인라인)
  2. head안에 style안에 작성(임베드)
  3. css파일을 따로 만들어서 작성(외부로 파일 분리) - 모듈화 - head안에 link를 통해서 
  => 사용하는 상황에 따라 다르게 선택

- 선택자(selector)
  1. 기본선택자
  2. 결합자
  3. 의사 클래스(pseudo class)

- 기본선택자

  *=> 전체 선택자
  h1, h2 => 요소 선택자
  .green => class 선택자(여러개 가능)
  #purple => id 선택자(무조건 한개)
  
- 하나의 태그에는 여러 개의 클래스를 작성할 수 있다.(띄어쓰기로 구분)

```html
<div> class="green box"></div>
```

- 결합자
  1. 자식 결합자
  2. 자손 결합자
  3. 일반 형제 결합자
  4. 인접 형제 결합자

```html
자식 결합자
.box > p {  => >로 구분
  font-size: 10px;
}
=> .box 바로 아래(1번) 직계 자식 p만 해당

자손 결합자
.box p {  => 띄어쓰기로 구분
  color: blue;
}
=> .box 아래에 있는 모든 p가 해당 

=> 자식결합자와 자손결합자의 차이는 바로 아래 1번인지 아니면 하위에 있는 전부인지에 있다.
============================================================================================

일반 형제 결합자
=> selectorA의 형제 요소 중 뒤에 위치하는 selectorB요소를 모두 선택(자손과 비슷)
p ~ span {  => ~로 구분
  color: red;
}
 
인접 형제 결합자
=> selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB요소만 선택(자식과 비슷)
p + span {  => +로 구분
  color: red;
}
```

- CSS 적용 우선순위
  1. 중요도 - !importance - 선언문 마지막에 선언하면 절대 안바뀜(쓰지 말자...)
  2. 우선순위 - 인라인 > id선택자 > class선택자(거의 class만 씀) > 요소선택자
  3. 소스순서(작성된 순서)
- CSS상속
  <>안에 들어와 있는 새로운 태그</> => 상속관계
  부모요소의 특성을 자식이 모두 상속받는 것은 아니다.
  상속되는 것은 Text관련 요소들이다.(font, color, opacity, visibility)
- CSS 크기 단위
  1. px(픽셀) - 고정적인 단위 - 모니터의 해상도에 따라 달라짐
  2. % - 가변적인 레이아웃에서 사용
  3. em - 부모요소에 상속을 받음(부모 10px, 자식=2em 이면 자식은 20px) - 부모에 대해 상대적인 값을 가짐 - 부모가 또 부모를 가질 경우 계속 곱해짐(복잡)
  4. rem - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐 - 부모에 영향을 받지 않음
  5. viewport - 사용자가 웹페이지를 방문했을 때 보이는 영역 - 디바이스에 따라 다름 - vw, vh, vmax, vmin
- CSS 색상 단위
  1. 색상 키워드
  2. RGB 색상 - # + 16진수 표기법, rgb()함수형 표기법
  3. HSL 색상 - 색상, 채도, 명도

## 4. CSS_2(advanced)

- Box model
  1. border = 테두리
  2. margin = border의 바깥
  3. padding = 테두리와 안쪽의 내부 여백(border ~ 내부 content)
  4. content = 내용

- margin and border examples

  margin: 10px; = margin 상하좌우 10px
  margin: 10px 20px; = margin 상하10px 좌우20px
  margin: 10px 20px 30px; = margin 상10px 좌우20px 하30px
  margin: 10px 20px 30px 40px;= margin 상10px 우20px 하30px 좌40px

  auto = 균등하게 나눔

  border: 2px dashed black; = 한 번에 크기, 스타일, 색상 전부 가능

- **box-sizing: border-box; 

  => box-sizing의 default는 content-box이기 때문에 원하는 크기가 아니고 추가적으로 padding, margin, border지정시 content에서 크기가 늘어난다
  => 따라서 box-sizing: border-box 설정을 통해 추가값이 지정되어도 설정한 전체 크기 안에서 움직일 수 있도록 한다.

- **마진상쇄
  => blockA의 top과 blockB의 bottom에 적용된 각각의 margin이 겹칠 때 둘 중 큰 마진 값으로 결합하는 현상

- CSS Display

  CSS는 원래 전부 네모임

- block vs inline

  block - 줄 바꿈이 일어나는 요소 - 화면 크기 전체의 가로를 차지

  inline - 줄 바꿈이 일어나지 않는 요소 - content의 너비만큼 차지 - width, height 지정 불가, line-height는 가능
  => inline를 줄 바꿈하기 위해서는 br태그 사용

- block 정렬

  margin-left: auto; = 마진을 왼쪽으로 전부 다줌 = 우측정렬

- inline 정렬

  text-align: right; = inline는 content가 중요하기 때문에 오른쪽으로 밀면 = 우측정렬

- display

  display: inline-block; = 두 속성을 모두 갖는다

  visibility: hidden; = 공간에는 존재하지만 눈에 보이지 않음

  display: none; = 공간조차 지워버림(조심해야함)

- **CSS Position
  문서 상에서 요소를 배치하는 방법을 지정
  static - 기준위치(좌측 상단)
  relative - 상대 위치 - 레이아웃에서 요소가 차지하는 공간은 static와 같음 - 외출 - 기존에 있던 위치를 기준으로 이동
  absolute - 절대위치 - 기존의 위치에서 공간을 차지하지 않고 가장 가까이 있는 부모/조상 요소를 기준으로 이동(relative, absolute에 만 붙음) - 출가 - 가까이에 있는 부모가 보이면 그 부모를 기준으로 새로운 위치를 잡는다 
  fixed - viewport 기준으로 이동(스크롤해도 같은 곳에 위치함) - 집을 나가도 부모를 안찾음

  => absolute를 사용하기 위해서는 먼저 static이 아닌 부모를 만들어야 한다.

## 5. 기타

- HTML : 웹 페이지가 어떻게 구조화되어 있는지 알 수 있도록 하는 마크업 언어
  CSS : 사용자에게 문서(HTML)를 표시하는 방법을 지정하는 언어
- **Position
  - relative : static 기준으로 감(실제 문서상에 존재하는 위치와 눈에 보이는 위치가 다름 - 기존의 위치를 가지고 있지만 눈에는 조정된 위치로 보임)
  - absolute : 부모/조상을 계속 타고 올라간다. 그 중에 static가 아닌 요소를 발견하면 해당 요소를 기준으로 위치한다. (아예 위치를 옮겨버림)
  - fixed : viewport 기준으로 일정 공간에 알박기
- 상대경로 vs 절대경로

```html
#abc > p:nth-child(2) {
  color: red;
}
=> id가 abc인 선택자의 바로 아래(1번)에 여러 자식들 중에 2번째 자식이 p태그라면 color은 red로

#abc > p:nth-of-type(2) {
  color: blue;
}
=> id가 abc인 선택자의 자식인 p태그 중 2번째 자식의 color은 blue로 

```
