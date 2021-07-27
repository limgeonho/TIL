- # Python[2021.07.22]

  ## 1. 스코프

  - 전역스코프 - 그 외 공간(어디에서든 접근 할 수 있음)
  - 지역스코프 - 함수 안에서 생성된 공간
  - 지역스코프는 전역스코프에 접근 할 수 있다.
  - 지역스코프 안에서 할당되기 전에 참조하면 에러가 난다...전역스코프에 할당이 되어 있다고 하더라도
  - 파이썬에서 모듈 = 파일
  - 인터프리터가 끝남 = 프로그램 종료
  - ex) 기존의 built-in안에는 print라는 이름으로 출력 로직이 저장되어 있다. 하지만 새롭게 global scope에서 print = 'hello'를 선언하면 built-in의 print를 덮어 쓰는것이 아니라 global안에 print가 하나 더 생성되는 것이기 때문에 이후에 print(3)을 하면 에러가 발생한다. 이유는 global에 있는 print를 참조하기 때문이다. 이를 해결하기 위해서 del print를 명령해서 global안에 있는 print를 제거한다. 그리고 난 후에는 print()를 다시 사용할 수 있다.
  - built-in영역은 건드릴 수 없음...
  - 코드가 진행되고 있는 구간은 local 결국 local, enclosed도 서버와 클라이언트 관계처럼 상대적인 개념이다.(사용되는 상황에 따라 달라짐.)
  - scope는 함수에서만 적용되는 말임... =함수가 아니면 scope는 적용되지 않는다.
  - LEGB rule
  - global : 전역변수에 접근하고 싶음 nonlocal : local에서 enclosed에 있는 변수에 접근하고 싶음

  ## 2. 재귀함수

  - return을 사용하면 함수를 무조건 강제 종료 시킬 수 있음
  - 반복문보다는 메모리 사용공간이 많이 필요하다.
  - while문과 비슷하다.
  - **종료조건을 만들어 줘야한다.(base-case)
  - 최대 재귀 깊이가 정해져 있음...(내부설정)

  ```python
  팩토리얼
  def factorial(n):
      if n == 1:
          return 1
      else:
          return n * factorial(n-1)
  
  피보나치 수열
  def fib(n):
      if n < 2:
          return n
      else:
          return fib(n-1) + fib(n-2)
  ```

  ## 3. 기타

  - 동적계획법 = 기록하기 = 메모이제이션

  - 리스트는 복수형으로 작성한다.

  - 함수 이름은 동사형으로 작성한다. => 함수 이름에서 return을 추측할 수 있으면 더 좋음

  - break는 가장 가까운 반복문 1개만 멈추게 한다.

  - global은 할당연산자(=)와 묶어서 생각

  - map(일=>함수, 대상(list)) => 대상 list는 그대로, 모든 일을 적용한 새로운 map객체를 return ex) map(int, lists) => 값이 보이지 않지만 list(map(int, lists)) 로 하면 보임

  - if not elem: => elem이 비었기를 기대함 pass # 0이거나, 비었거나

     => 결국 if문안에 있는 로직이 실행되기 위해서는 비어있어야함.