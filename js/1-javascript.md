# Javascript[2021.10.27] 



## 1. Intro

- 브라우저 화면을 동적으로 만들 수 있음

- 브라우저를 조작할 수 있는 유일한 언어

- 브라우저

  - 웹 서버에서 이동하며 클라이언트와 서버 간 양방향으로 통신하고, HTML문서나 파일을 출력하는 GUI기반 소프트웨어
  - == 웹 브라우저

  

## 2. DOM(Document Object Model)

- 브라우저에서 할 수 있는 일

  1. DOM 조작(HTML조작)
  2. BOM 조작
  3. Javascript Core(ECMA Script)

- DOM 이란?

  - HTML, XML 과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
  - 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
  - 문서가 구조화되어 있으며 각 요소는 객체로 취급
  - 메서드, 프로그래밍 언어적 조작가능
  - 주요 객체
    - window : 최상위 객체
    - document : body 등...
    - navigator, location, historym, screen
  - ![1](https://user-images.githubusercontent.com/73927750/139025027-016dc940-8d2d-493c-8e6e-4943949ac5e4.JPG)

- BOM(Browser Object Model)

  - 자바스크립트가 브라우저와 소통하기 위한 모델
  - DOM 보다 상위에 존재하는 모델
  - window.open() 등... => 직접 페이지 기능을 접근

- DOM 조작

  - Document는 문서 한 장(HTML)에 해당
  - DOM 조작 순서
    1. 선택(Select)
    2. 변경(Manipulation)

- DOM 선택

  - 메서드
    - Document.querySelector(selector) - 단일
      - 제공한 선택자와 일치하는 element 하나 선택
      - 없다면 null
    - Document.querySelectorAll(selector) - 다중
      - 제공한 선택자와 일치하는 여러 element를 선택
      - 지정된 셀렉터에 일치하는 NodeList를 반환 => 유사배열이기 때문에 forEach함수 및 다양한 메서드 사용 가능 + Static Collection으로 실시간으로 변화가 반영되지 않음
    - getElementById(id) 등 여러 비슷한 메서드가 있지만 id, class 그리고 tag선택자 등을 모두 사용할 수 있는 querySelector('#id')와 querySelectorAll('.classname')을 사용하자

- DOM 변경

  - 매서드
    - Document.createElement()
      - 작성한 태그 명의 HTML요소를 생성하여 반환
    - Element.append()
      - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node객체가 DOMstring을 삽입(여러개 가능)
    - Node.appendChild()
      - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입(Node만 가능)(한 번에 하나 가능)
  - 변경 관련 속성
    - Node.innerText
    - Element.innerHTML

- DOM 삭제

  - 메서드
    - ChildeNode.remove()
    - Node.removeChild()

- DOM 속성

  - 메서드
    - Element.setAttribute(name, value)
      - 지정된 요소의 값을 설정
    - Element.getAttribute(attributeName)
      - 해당 요소의 지정된 값을 반환

- DOM 조작 - 정리

  ![2](https://user-images.githubusercontent.com/73927750/139032848-c215863c-13fe-4346-be39-3a2430b0c1b2.JPG)

- ```html
  <body>
  
      <h1>Todo App</h1>
      <input type="text">
      <button>go</button>
  
      <ul>
        
      </ul>
  
    <script>
      // go버튼을 누르면 
      // input 태그에 
      // 사용자가 입력한 내용을 콘솔에 찍는다.(1) 
      // 사용자가 입력한 내용을 'ul 태그'에 넣는다.(2)
      const buttonTag = document.querySelector('button')
      const inputTag = document.querySelector('input')
      const ulTag = document.querySelector('ul')
      
      function onSubmit(){
        const userInput = inputTag.value
        // console.log('시용자 입력은' + userInput)
        
        const liTag = document.createElement('li')
        liTag.innerText = userInput
        ulTag.appendChild(liTag)
  
        inputTag.value = ''
      }
  
      buttonTag.addEventListener('click', onSubmit)
      // inputTag.addEventListener('keydown', onSubmit)
  
    </script>
  ```

- ```html
  <body>
    <h1>Hello SSAFY</h1>
    <h2 id="location-header">Location</h2>
    <div>
      <ul>
        <li class="ssafy-location">서울</li>
        <li class="ssafy-location">대전</li>
        <li class="ssafy-location">광주</li>
        <li class="ssafy-location">구미</li>
        <li class="ssafy-location">부울경</li>
      </ul>
    </div>
    <script>
      // 1. Selection
      // 1-1. window & document
      console.log(window)
      console.log(document)
      console.log(window.document)
  
      // 1-2. querySelector
      const h1 = document.querySelector('h1')
      const h2 = document.querySelector('h2')
      const secondH2 = document.querySelector('#location-header')
      const selectUlTag = document.querySelector('div > ul')
  
      // 1-3. querySelectorAll
      const liTags = document.querySelectorAll('li')
      const secondLiTags = document.querySelectorAll('.ssafy-location')
  
      // 2. Creation & Append
      // 2-1. createElement
      const ulTag = document.querySelector('ul')
      const newLiTag = document.createElement('li')
  
      // 2-2. append
      const ulTag = document.querySelector('ul')
      const newLiTag = document.createElement('li')
      newLiTag.innerText = '새로운 리스트 태그'
      ulTag.append(newLiTag)
      ulTag.append('문자열도 추가 가능')
  
      const new1 = document.createElement('li')
      new1.innerText = '리스트 1'
      const new2 = document.createElement('li')
      new2.innerText = '리스트 2'
      const new3 = document.createElement('li')
      new3.innerText = '리스트 3'
      ulTag.append(new1, new2, new3)
      
      // 2-3. appendChild
      const ulTag = document.querySelector('ul')
      const newLiTag = document.createElement('li')
      newLiTag.innerText = '새로운 리스트 태그'
      ulTag.appendChild(newLiTag)
      ulTag.appendChild('문자열은 추가 불가')
  
      const new1 = document.createElement('li')
      new1.innerText = '리스트 1'
      const new2 = document.createElement('li')
      new2.innerText = '리스트 2'
      ulTag.appendChild(new1, new2)
  
      // 2-2. innerText & innerHTML
      const ulTag = document.querySelector('ul')
      const liTag1 = document.createElement('li')
      liTag1.innerText = '<li>춘천</li>'
      const liTag2 = document.createElement('li')
      liTag2.innerHTML = '<li>춘천</li>'
      ulTag.append(liTag1, liTag2)
  
      const ulTag = document.querySelector('ul')
      ulTag.innerHTML = '<li><a href="javascript:alert(\'당신의 개인정보 유출\')">춘천</a></li>'
  
      // 3. Delete
      // 3-1. remove
      const header = document.querySelector('#location-header')
      header.remove()
  
      // 3-2. removeChild
      const parent = document.querySelector('ul')
      const child = document.querySelector('ul > li')
      const removedChild = parent.removeChild(child)
      console.log(removedChild)
  
      // 4. 속성
      // 4-1. setAttribute
      const header = document.querySelector('#location-header')
      header.setAttribute('class', 'ssafy-location')
  
      // 4-2. getAttribute
      const getAttr = document.querySelector('.ssafy-location')
      getAttr.getAttribute('class')
      getAttr.getAttribute('style')
  
      //2-5. Element Styling
      li1.style.cursor = 'pointer'
      li2.style.color = 'blue'
      li3.style.background = 'red'
    </script>
  </body>
  ```

  

## 3. Event

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체

- 마우스 클릭, 키보드 누르는 행윈 등등...

- UI Event

  - MouseEvent, KeyboardEvent, inputEvent, FocusEvent

- Event의 역할

  - 특정 이벤트가 발생하면, 할 일을 등록한다.

- Event handler

  - EventTarget.addEventListener()

  - target.addEventListener(type, listener[, options])

    - type
      - 반응 할 이벤트 유형
    - listener
      - 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체, 함수

  - ![3](https://user-images.githubusercontent.com/73927750/139034851-0ed151eb-5f72-4636-b652-b2643b4c6424.JPG)

  - ```html
    <body>
      <!-- 1. onclick -->
      <button onclick="alertMessage()">나를 눌러봐!</button>
    
      <!-- 2-1. addEventListener -->
      <button id="my-button">나를 눌러봐!!</button>
      <hr>
    
    	<!-- 2-2. addEventListener -->
      <p id="my-paragraph"></p>
    
      <form action="#">
        <label for="my-text-input">내용을 입력하세요.</label>
        <input id="my-text-input" type="text">
      </form>
      <hr>
    
      <!-- 2-3. addEventListener -->
      <h2>Change My Color</h2>
      <label for="change-color-input">원하는 색상을 영어로 입력하세요.</label>
      <input id="change-color-input"></input>
      <hr>
    
      <script>
        // 1
        const alertMessage = function () {
          alert('메롱!!!')
        }
    
        // 2-1
        const myButton = document.querySelector('#my-button')
        myButton.addEventListener('click', alertMessage)
    
        // 2-2
        const myTextInput = document.querySelector('#my-text-input')
        myTextInput.addEventListener('input', function(event){
          const myPtag = document.querySelector('#my-paragraph')
          myPtag.innerText = event.target.value
        })
    
    
        // 2-3
        const colorInput = document.querySelector('#change-color-input')
        colorInput.addEventListener('input', function(event){
          const h2Tag = document.querySelector('h2')
          h2Tag.style.color = event.target.value
        })
      </script>
    </body>
    ```

- Event 취소

  - Event.preventDefault()
    - 현재 이벤트의 기본 동작을 중단
    - 태그의 기본 동작을 작동하지 않게 막음
    - ex) a 태그의 기본동작은 클릭 시 링크로 이동 / form 태그의 기본 동작은 form 데이터 전송
    - 취소할 수 없는 이벤트도 존재함(ex : scroll...)

- practice

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <form action="#">
      <input type="text">
      <button>Add</button>
    </form>
    <ul>
  
    </ul>
  
    <script>
      const form = document.querySelector('form')
  
      const addTodo = function(event){
        event.preventDefault()
  
        const input = document.querySelector('input')
        const content = input.value
        
        if (content.trim()){
          const liTag = document.createElement('li')
          liTag.innerText = input.value
    
          const ulTag = document.querySelector('ul')
          ulTag.appendChild(liTag)
        } else {
          alert('할 일을 입력해주세요!!')
        }
        
        // input.value = '' 보다는 event.target.reset()
        event.target.reset()
      }
  
      form.addEventListener('submit', addTodo)
    </script>
  </body>
  </html>
  ```

  

