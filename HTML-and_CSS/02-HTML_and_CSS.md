# HTML_and_CSS[2021.08.03]

## 1. basic_tags

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>

  <!-- 하이퍼링크(default) -->
  <a href="https://naver.com">Naver</a>
  
  <!-- 새 탭에서 열기 추가  -->
  <a href="https://naver.com" target="_blank">Naver</a>
  
  <!-- # == placeholder 공간만 차지하고 현재 동작은 하지 않는다. pass같은 느낌 -->
  <a href="#">Login</a>

  <!-- 같은 위치 안에서 이동하기 -->
  <a href="02_text.html">02 text</a>

  <!-- HTML5에 추가된 Semantic Tags -->
  <header></header>
  <nav></nav>
  <section></section>
  <article></article>
  <footer></footer>

</body>
</html>
```

## 2. text

```html
<h1>heading1</h1>
<h2>heading2</h2>
<h3>heading3</h3>
<h4>heading4</h4>
<h5>heading5</h5>
<h6>heading6</h6>

<div>
  <b>This is bold text</b>
  <i>This is Italic text</i>
</div>

<!-- 수평줄 -->
<hr>

<!-- semantic tags들을 활용하자 -->
<p>
  <strong>This is strong text</strong>
  <em>This is EMPHASIZED text</em>
</p>

<!-- <br>은 가독성을 위해서 줄간격을 위해서만 사용, positioning을 위해서는 절대 사용X => <p>로 묶어라 차라리.... -->
<p>
  Lorem ipsum dolor sit amet consectetur adipisicing elit. <br>Quas expedita esse iste sint laudantium! Quaerat animi magni libero, odio voluptates magnam ut, quod ad nisi nobis sapiente! Sunt, repellendus culpa?
</p>

<!-- 인용문...거의 안씀 -->
<blockquote>
  명언~
</blockquote>
```

## 3. list

```html
<!-- 순서 있는 리스트 -->
<ol>
  <li>HTML</li>
  <li>CSS</li>
    <ol>
      <li>unit</li>
      <li>color</li>
      <li>position</li>
      <li>visibility</li>
    </ol>
  <li>밥먹기</li>
  <li>쉬는시간</li>
</ol>

<!-- 순서 없는 리스트 -->
<ul>
  <li>HTML</li>
  <li>CSS</li>
    <ul>
      <li>unit</li>
      <li>color</li>
      <li>position</li>
      <li>visibility</li>
    </ul>
  <li>밥먹기</li>
  <li>쉬는시간</li>
</ul>

<!-- => <li>, <ol>, <ul> 모두 block -->
```

## 4. table

```html
<!-- 
| col1 | col2 | col3 | 
| ---- | ---- | ---- |
| 1-1  | 1-2  | 1-3  |
| 2-1  | 2-2  | 2-3  |
| 3-1  | 3-2  | 3-3  | 
-->

<!-- 표, table -->
<!-- 맨 위줄, table header -->
<!-- 가 row, table row -->
<!-- 세 col, table column-->
<!-- 표안에 있는 데이터, table data -->

<table>
  <!-- 가로줄 -->
  <tr>
    <th>col1</th>
    <th>col2</th>
    <th>col3</th>
  </tr>
  <tr>
    <!-- 데이터 -->
    <td>1-1</td>
    <td>1-2</td>
    <td>1-3</td>
  </tr>
  <tr>
    <td>2-1</td>
    <td>2-2</td>
    <td>2-3</td>
  </tr>
  <tr>
    <td>3-1</td>
    <td>3-2</td>
    <td>3-3</td>
  </tr>
</table>

```

## 5. form

```html
<form action="어디로 양식을 보낼 것인가">
  <div>
    이름 : <input type="text">
  </div>
  <div>
    나이 : <input type="text">
  </div>
  <div>
    전공 : <input type="text">
  </div>
  <div>
    <input type="submit">
  </div>
</form>

<!-- 위의 방법이 아닌 아래의 방법을 이용한다 -->

<!-- <input> 는 inline -->
<form action="어디로 양식을 보낼 것인가">
  <div>
    <!-- lable의 for값과 input의 id값을 연결한다. -->
    <!-- 서버에서는 input의 name값을 지정하여 연결함 -->
    <label for="name">이름</label>
    <input id="name" name="name" placeholder="What's your name" type="text">
  </div>
  <div>
    <label for="age">나이</label>
    <input id="age" required type="number">
  </div>
  <div>
    <!-- value에 값을 지정하는 것은 기본 값을 설정하는 것임 -->
    <label for="major">전공</label>
    <input id="major" value="CS" type="text">
  </div>
  <div>
    <!-- 전송!을 누르면 form의 action에 있는 주소로 전달된다. -->
    <input type="submit" value="전송!">
  </div>
</form>

```

## 6. selector

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
  <style>
    /* 전체 셀렉터 */
    * { color: crimson; }
    /* 요소 셀렉터 */
    h1 { color: red; }
    p { color: blue; }
    
    /* 복수 셀렉터 */
    h2, h3 { color: green;}

    /* id, class 셀렉터 */
    #p1, .intro {color: darkmagenta;}

    /* 속성(attribute) 셀렉터 */
    a[target="_blank"] { color: blue;}

    /* 후손(모든 자손) 셀렉터 */
    div p { color: skyblue; }

    /* 자식(직계 자식) 셀렉터 */
    section > p { color: orange;}

    /* 가상(pseudo) 클래스 셀렉터 */
    p:hover { background-color: tan; }
    article > p:nth-child(3) { color: tomato; }
    article > p:nth-of-type(1) { color: deeppink;}

  </style>
</head>
<body>
  <h1>Hello World</h1>
  <h2>02 Web</h2>
  <h3>CSS selector</h3>
  <p>HIHI</p>
  HHHHHH
  <p id="p1">id p1</p>
  <p class="intro">class intro</p>

  <a href="https://naver.com">Naver</a>
  <a href="htpps://google.com" target="_blank">Google</a>

  <p>Not in DIV</p>
  <div>
    <p>In DIV</p>
    <article>
      <p>In DIV</p>
    </article>
  </div>

  <section>
    <p>section > p</p>
    <span>
      <p>section > span > p</p>
    </span>
  </section>

  <article>
    <h3>제목</h3>
    <p>내용1</p>
    <p>내용2</p>
    <p>내용3</p>
  </article>

</body>
</html>

```

## 7. position

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
  <style>
    div.parent {
      width: 150px;
      height: 150px;
      background-color: deepskyblue;
      border: 1px solid black;
      color: brown;
    }

    div.static {
      position: static;
      background-color: green;
      color: white;
      text-align: center;
      line-height: 150px;
    }

    div.relative {
      /* 화면 좌표만 달라짐 그 외에는 static과 동일 */
      position: relative;
      top: 10px;
      left: 10px;
      
      background-color: violet;
      color: black;
      text-align: center;
      line-height: 150px;
    }

    div.absolute {
      /* 화면 좌표만 달라짐 그 외에는 static과 동일 */
      position: absolute;
      top: 10px;
      left: 10px;
      width: 100px;
      background-color: pink;
      color: black;
      text-align: center;
      line-height: 100px;
    }

    footer.fixed {
      position: fixed;
      bottom: 0px;
      color: white;
      background-color: black;
      text-align: center;
      width: 100%;
    }
  </style>
</head>
<body>
  <!-- div.parent>div.static -->
  <!-- block 요소 => 부모의 maximum 가로를 가진다 / content의 세로를 가진다. -->
  <div class="parent">
    <div class="static">static box</div>
  </div>
  
  <div class="parent">
    <div class="relative">relative box</div>
  </div>

  <!-- absolute는 자기 멋대로기 때문에 block 요소 => 부모의 maximum 가로를 가진다 => 무시 => body까지는 못나감 -->
  <div class="parent">
    <div class="relative">relative box
      <div class="absolute">absolute box</div>
    </div>
  </div>

  <!-- fixed => width == content 길이 -->
  <footer class="fixed">
    This is footer 
  </footer>

  <!-- CSS를 적용하고 저장하고 확인하는 것 보다 개발자 도구 => element.style => 적용하고 우클릭 => copy declaration으로 복사해서 적용  -->
</body>
</html>
```

## 8. 기타

- 중앙정렬

  inline요소 => text-align : center 
  block요소 => margin auto

- margin과 margin이 겹치면 상쇄되지만

  margin과 padding는 상쇄되지 않는다. 
