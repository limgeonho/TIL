# Javascript[2021.11.01] 



## 1. AJAX

-  Asynchronous JavaScript And XML(비동기식 JavaScript와 XML)

- 서버와 통신하기 위해 XMLHttpRequest객체를 활용

- JSON, XML, HTML 등 다양한 포멧을 주고 받을 수 있음

- 특징

  - 페이지 전체를 reload(새로고침)를 하지 않고서도 수행되는 '비동기성'
    - 페이지의 일부만 업데이트 가능
  - 서버로부터 데이터를 받고 작업을 수행

- XMLHttpRequest 객체

  - 서버와 상호작용하기 위해 사용되며 전체 페이지의 새로고침 없이 데이터를 받아올 수 있음

  - 사용자의 작업을 방해하지 않으면서 페이지 일부를 업데이트

  - AJAX프로그래밍에서 사용

  - XMLHttpRequest()

  - ```html
    <script>
      const request = new XMLHttpRequest()
      const URL = 'https://jsonplaceholder.typicode.com/todos/1/'
    
      request.open('GET', URL)
      request.send()
    
      const todo = request.response
      console.log(todo)
      // todo에는 아무것도 출력되지 않는다 => console.log()가 request.response를 기다리지 않고 실행
    </script>
    ```

    

## 2. Asynchronous JavaScript

- 동기식
  - 순차적, 직렬적 수행
  - 요청을 보낸 후 응답을 받아야함 다음 동작을 수행(blocking)
  - Javascript는 single-thread(synchronous)
- 비동기식
  - 병렬적 수행
  - 요청을 보낸 후 응답을 기다리지 않고 다음 동작을 수행(non-blocking)
  - Javascript는 single-thread(asynchronous)
- why Asynchronous?
  - 사용자 경험 때문에 사용
- Single threaded인 JavaScript
  - 이벤트를 처리하는 Call Stack이 하나인 언어
  - 단일스레드로 작업 수행
  - 해결 방안
    1. 즉시 처리하지 못하는 이벤트를 Web API로 보냄
    2. 처리된 이벤트들은 처리된 순서대로 Task queue에 세워놓음
    3. Call Stack가 비면 담당자인(Event loop)가 대기 줄에서 가장 먼저 들어온 이벤트를 Call Stack로 보냄
  - Call Stack
    - 요청이 들어올 때마다 해당 요청을 순차적으로 처리하는  Stack자료구조
  - Web API(Browser API)
    - Javascript 엔진이 아닌 브라우저 영역에서 제공하는 API
  - Task Queue
    - 비동기 처리된 callback 함수가 대기하는 Queue자료구조
  - Event Loop
    - Call stack이 비어있는지 확인
    - 비어있는 경우 task queue에 대기 중인 callback함수가 있는지 확인하고 call stack 으로 push
  - ![1](https://user-images.githubusercontent.com/73927750/139694378-d55568e0-78f1-4ab0-8af1-abacc1da94d3.JPG)

- Zero delays 발생

  - setTimeout(func, 0) => 0초 뒤에 실행

    => 하지만, 실제로는 0초가 아니라 call stack에 있는 함수들이 실행이 끝나야 실행된다.

    => 따라서, Web API에 들어오는 순서는 중요하지 않고 어떤 이벤트가 먼저 처리되느냐가 중요해짐

  - 해결방안

    - Async callbacks
    - promise-style



## 3. Callback Function

- 다른 함수에 인자로 전달된 함수

- 외부 함수 내에서 호출됨

- 동기식, 비동기식 모두 사용됨(하지만 대부분 비동기식에서 사용)

- 예시

  ![2](https://user-images.githubusercontent.com/73927750/139695410-2d7579a2-00e7-4249-87af-669409bc185a.JPG)

- 요청이 들어온다면, 특정 이벤트가 발생하면 => 실행 == callback function덕분에 가능

- 비동기 로직에서 callback 함수는 필수!!

- 하지만 순차적인 많은 callback 함수를 사용하면 callback hell~

  => Promise 방식의 콜백 사용!!



## 4. Promise

- 비동기 작업의 최종 완료 또는 실패를 나타내는 객체
- 성공에 대한 약속 => .then(callback)
- 실패에 대한 약속 => .catch(callback)
- .then(callback)
  - 이전 작업이 성공했을 때 수행할 작업을 나타내는 callback

- .catch(callback)
  - 이전 작업이 실패했을 때 수행할 작업을 나타내는 callback(try-catch와 비슷)

- promise methods(.then(callback), .catch(callback))

  - .then(callback)을 여러개 연결해서 사용하여 연쇄적인 작업 수행가능(chaining)

    => 여러 비동기 작업을 차례대로 수행가능

  - 반드시 반환 값이 있어야함

    => 없다면 다음 callback 함수가 이전의 promise 결과를 받을 수 없음

- .finally(callback)

  - 결과와 상관없이 무조건 지정된 callback 함수 실행

    => 이전의 인자가 필요 없음



## 5. Axios

- promise based HTTP client for the browser and Node.js
- 브라우저를 위한 Promise 기반의 클라이언트
- 편리한 AJAX요청이 가능하도록 도와줌

- XMLHttpRequest -> Axios

  ![3](https://user-images.githubusercontent.com/73927750/139697416-3fcdf5bd-9bc5-4c5c-a465-c18546207b78.JPG)

- ```html
  <!-- axios CDN -->
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
      const URL = 'https://jsonplaceholder.typicode.com/todos/1/'
  
      const myPromise = axios.get(URL)
      console.log(myPromise)
  
      // response 는 단순하게전달 되는 값의 명칭임
      myPromise
        .then(response => {
          return response.data
        })
        .then(response =>{
          return response.title
        })
        .then(response =>{
          console.log(response)
        })
        .catch(error =>{
          console.log(error)
        })
        .finally(function(){
          console.log('나는 무조건 실행!')
        })
    </script>
  ```
