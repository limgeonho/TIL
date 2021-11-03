# Vue.js[2021.11.01] 



## 1. Vue(FE)

- 대표적인 프론트엔드 프레임워크

  - Vue.js, React, Angular

- 사용자 인터페이스를 만들기 위한 진보적인 자바스크립트 프레임워크

- 다양한 라이브러리를 통해 SPA(Single Page Application)를 지원

- SPA

  - Single Page Application == 단일 페이지 애플리케이션

  - 현재 페이지를 동적으로 렌더링함으로써 사용자와 소통하는 웹 애플리케이션

  - 단일 페이지로 구성되며 서버로부터 최초에만 페이지를 다운로드하고 이후에는 동적으로 DOM을 구성

    => 처음에 페이지를 받고 이후에는 전체를 다시 받는 것이 아닌 일부분만 동적으로 다시 작성함

    => 사용자 경험(UX)을 향상시킴

  - 동작 원리의 일부가 CSR의 구조를 따름

- CSR

  - Client Side Rendering

  - 서버에서 화면을 구성하는 SSR방식과 달리 클라이언트에서 화면을 구성

  - 최초에는 HTML, CSS, JS 등 데이터를 제외한 각종 리소스를 응답받고 이후 클라이언트에서는 필요한 데이터만  JS로 DOM을 렌더링하는 방식

    => 처음에는 뼈대만 이후에 브라우저에서 동적으로 DOM을 그림

  - SPA가 사용하는 렌더링 방식임

  - ![1](https://user-images.githubusercontent.com/73927750/140012111-a89e8d7b-3f27-406d-9f06-7495c5ce8927.JPG)

  - 장점 

    1. 서버와 클라이언트 간 트래픽 감소
    2. 사용자 경험 향상

  - 단점

    1. SSR에 비해 전체 페이지 렌더링 시점이 느림
    2. SEO(검색 엔진 최적화)에 어려움이 있음 => 최초 문서에 데이터가 없기 때문

- SSR

  - Server Side Rendering
  - 서버에서 클라이언트에게 보여줄 페이지를 모두 구성하여 전달하는 방식
  - JS 웹 프레임워크 이전에 사용되던 전통적인 렌더링 방식
  - ![2](https://user-images.githubusercontent.com/73927750/140048578-a6663ae5-519b-4090-aeee-ec16f2b20119.JPG)

  - 장점
    1. 초기 구동 속도가 빠름
    2. SEO에 적합
  - 단점
    1. 모든 요청마다 새로운 페이지를 구성하여 전달
    2. 반복되는 새로고침으로 사용자 경험이 떨어짐

- 최종 모습

  ![4](https://user-images.githubusercontent.com/73927750/140049257-eaa16ae3-13dd-4bd1-aeaf-b4c98b9c0269.JPG)



## 2. Why Vue.js?

- 사용자와의 상호작용이 많이 이루어지는 상황에서 Vanilla JS만으로는 관리하기 어려움...

- 페이스북에서 이름을 수정했을 때 해당 이름은 전체 다 바꾸는 것은 무리...

- 모든 요소를 전부 선택해서 바꾸는 것 => 낭비

  => 하지만, Vue.js는 DOM과 Data가 연결되어 있으면

  => Data를 변경하면 이에 연결된 DOM은 알아서 변경

  => 따라서, 신경 쓸 부분은 Data관리



## 3. MVVM Pattern

- 디자인 패턴임

- 구성 요소

  1. Model
  2. View
  3. View Model

- 형태

  ![5](https://user-images.githubusercontent.com/73927750/140049953-0d6ae015-2d2a-4fc1-b318-c4e03810b46c.JPG)

- Model

  - Vue의 Model == JavaScript의 Object

  - 해당 Model은 Vue Instance의 data로 사용된다

    => 바뀌면 => DOM도 바뀜

- View 

  - Vue의 View == DOM(HTML)이다
  - data가 바뀌면 바뀌는 대상임

- ViewModel

  - Vue의 ViewModel == 모든 Vue Instance
  - View와 Model 사이에서 Data와 DOM에 관련된 모든 일을 처리



## 4. Syntax of Vue.js

- Vue Instance

  - 인스턴스 만들기

    ```html
    const app = new Vue({
    
    })
    ```

  - Vue Instance == Vue Component

- el

  - Vue Instance에 연결(마운트)할 기존 DOM 엘리먼트가 필요

  - CSS, HTML element로 작성

    ```html
    const app = new Vue({
    	el: '#app'
    })
    ```

- data

  - Vue Instance의 데이터 객체

  - Model

  - template에서 interpolation으로 접근 가능

  - Vue 객체 내 다른 함수에서 this키워드로 접근 가능

  - 주의

    - 화살표 함수를 data에 사용하면 안 됨
    - 화살표 함수가 부모 컨텍스트를 바인딩하기 때문에 this는 내가 원하는 Vue Instance를 가리키지 않음

    ```html
    const app = new Vue({
    	el: '#app',
    	data: {
    		message: 'Hello',
    	}
    })
    ```

- methods

  - Vue Instance에 추가할 메서드

  - template에서 interpolation으로 접근 가능

  - 주의

    - 화살표 함수를 메서드를 정의하는데 사용하면 안 됨
    - 화살표 함수가 부모 컨텍스트를 바인딩하기 때문에 this는 Vue Instance가 아니며 this.a는 정의되지 않음

    ```html
    const app = new Vue({
    	el: '#app',
    	data: {
    		message: 'Hello',
    	},
    	methods: {
    		greeting: function(){
    			console.log('hello')
    		}
    	}
    })
    ```

- this keyword

  - Vue 객체 내에서 Vue Instance를 가리킴



## 5. Template Syntax

- 렌더링 된 DOM을 기본 Vue 인스턴스의 데이터에 선언적으로 바인딩할 수 있는 HTML 기반 템플릿 구문을 사용
- 종류
  - Interpolation
  - Directive
- Interpolation(보간법)
  - {{ message }}
- Directive(디렉테브)
  - v-접두사가 있는 특수 속성
  - 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 역할을 함
  - 종류
    - v-text
      - 엘리먼트의 textContent를 업데이트 == innerText
      - 내부적으로 interpolation 문법이 v-text로 컴파일 됨
    - v-html
      - 엘리먼트의 innerHTML을 업데이트 => XSS 공격에 취약
      - 사용자에게 받은 데이터는 절대로 v-html로 사용금지!
    - v-show
      - 조건부 렌더링
      - 엘리먼트는 항상 렌더링되고 DOM에 남아있지만 display CSS속성을 토글
    - v-if, v-else-if, v-else
      - 조건부 렌더링
      - 조건에 따라 블록을 렌더링
      - directive의 표현식이 true일 때만 렌더링 => false이면 아예 생성 x
    - v-for
      - 여러번 렌더링
      - item in items 구문 사용
      - v-for사용시 반드시 key 속성을 사용
      - v-if와 함께 사용하는 경우 v-for가 우선순위가 더 높음 => 같이 쓰지마~
    - v-on
      - 엘리먼트에 이벤트 리스너를 연결
      - 특정 이벤트가 발생했을때 주어진 코드가 실행 됨
      - 약어
        - @
        - v-on:click => @click
    - v-bind
      - HTML요소의 속성에 Vue의 상태 데이터를 값으로 할당
      - Object 형태로 사용하면 value가 true인 key가 class바인딩 값으로 할당
      - 약어
        - :
        - v-bind:href => :href
    - v-model
      - HTML form 요소의 값과 data를 양방향 바인딩
      - 수식어
        - .lazy
          - input 대신 change 이벤트 이후에 동기화
        - .number
          - 문자열을 숫자로 변경
        - .trim
          - 입력에 대한 trim을 진행
  - computed
    - 데이터를 기반으로 하는 계산된 속성
    - 반드시 return값이 존재해야함 => ()없이 호출
    - 종속된 데이터에 따라 캐싱됨
    - 종속된 데이터가 변경될 때만 함수를 실행!!!
  - computed vs methods
    - methods는 호출하면 매번 함수를 실행하지만 computed는 종속 대상이 변경되지 않으면 다시 실행하지 않고 가지고 있는 값을 반환함
  - watch
    - 데이터를 감시
    - 데이터에 변화가 일어났을 때 실행되는 함수
  - computed vs watch
    - computed
      - 특정 데이터를 직접적으로 사용/가공하여 다른 값으로 만들 때 사용
      - 선언형 프로그래밍 방식
    - watch
      - 특정 데이터의 변화 상황에 맞춰 다른 data 등이 바뀌어야할 때 사용
      - 감시할 데이터를 지정하고 그 데이터가 바뀌면 특정 함수를 실행하는 방식
      - 명령형 프로그래밍 방식
      - 감시하던 대상이 변경되면 콜백 함수를 실행함
  - filter
    - 텍스트 형식화를 적용할 수 있는 필터
    - interpolation 혹은 v-bind를 이용할 때 사용 가능
    - 파이프(|)와 함께 사용
    - chaining가능



## 6. Lifecycle Hooks

-  각 Vue 인스턴스는 생성될 때 일련의 초기화를 거침

- 그 과정에서 사용자 정의 로직을 실행할 수 있는 Lifecycle Hooks도 호출됨

  ![7](https://user-images.githubusercontent.com/73927750/140058320-11255808-2274-4838-b31a-2eb27bf6d745.JPG)



## 7. lodash library

- 모듈성, 성능 및 추가 기능을 제공하는 Javascript유틸리티 라이브러리
- array, object등 자료구조를 다룰 때 사용하는 유용하고 간편한 함수 제공
- 함수 예시(앞에 _.function를 붙여준다)
  - reverse, sortBy, range, random
