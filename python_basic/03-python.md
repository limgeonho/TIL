# Python[2021.07.21]

## 1. 함수(1)

- 재사용성
- 유지보수 용이
- 함수의 이름, 매개변수, 바디(로직), 반환값
- docstring : 함수에 관한 설명을 담당하는 부분(""" """)
- __str__처럼 => __< >__ 형태의 함수를 매직메서드라고함

## 2. 함수의 선언

- def 키워드 이용
- 매개변수를 넘겨 줄 수 있음
- 동작 후에는 return을 통해 결과를 전달함 - 반드시 하나의 객체만 반환
- 함수는 호출되면 코드를 실행하고 return값을 반환하고 종료된다.
- 반드시 하나의 객체만 반환?

```python
1. 복수의 객체를 return?
def foo(a, b):
    return a+b, a-b
결과 값은 (a+b, a-b) => 처럼 튜플을 통해서 하나의 객체만 return가능
2. 명시적인 return 값이 없는 경우
def greetings():
    print('hi')
결과 값은 hi 이지만 type(greetings())는 Nonetype로 나옴 
=> 따라서, 복수의 값(tuple), 하나의 값, return이 없는경우(None)를 반환하기 때문에 함수는 하나의 객체만 반환한다.
```



## 3. 함수 input, 매개변수, 인자

```python
1.위치인자 - 함수 호출 시 인자는 위치에 따라 함수 내에 전달된다.
매개변수 - 함수에 입력으로 전달된 값을 받는 변수
def func(a, b)
위치인자 - 함수를 호출 할 때 전달하는 변수 값
def func(1, 2)
=> 명확하게는 둘의 의미가 다름!!

2.기본 인자 값
def add(x, y=0):
    return x + y
print(add(2)) = 2 + 0 = 2

3.키워드 인자
def add(y=1, x=2):
키워드와 함께 인자값을 전달하면 순서와 상관없이 원하는 인자를 전달가능

4.가변 인자 리스트
def add(*args):
    for arg in args:
        print(arg)
=> 인자 값이 1개가 와도 되지만 여러 수가 와도 된다. 
하지만 여러개의 인자 값을 전달하기 위해서는 튜플로!
add(2,3,4,5)

5.가변키워드 인자 리스트
def add(**kwargs):
=> dict형태로 저장

서로 사용하는 순서를 주의해야함
ex) def my_info(x, y, *args, **kwargs)
- 정의할 때 parameters 순서 : 위치인자, 기본인자 순으로 정의 해야함(basic -> default)
- 호출할 때 arguments순서 : position -> kword
```

## 4. 함수의 scope

- 코드 내부에 지역 스코프(local scope) - 함수안에서 만들어지는 스코츠
- 그 외 공간 = 전역 스코프(global scope)
- 변수(지역변수, 전역변수)
- 스코프의 이름 검색규칙(LEGB rules)
- Local scope
- Enclosed scope
- Global scope
- Built-in scope
- global, nonlocal은 인위적으로 local에서 전역변수의 값을 변경하도록 하는 명령이기 때문에 가급적 사용하지 않도록 한다.

## 5. 함수(2)

- 결국 함수도 사실 def cube(): 에서 cube라는 변수 안에 로직이 저장되어 있는 꼴임.

- 숫자, 문자열, T/F를 제외한 변수들 처럼 주소값을 갖는 경우와 같다고 생각

  => 이를 통한 아이디어에서 나온것이 람다식 cube = lambda num: num**3

- 일반 함수를 람다식으로 바꾸는 방법

  1. def 와 함수명을 지운다.
  2. 그자리에 lambda라고 쓴다.
  3. 매개변수를 감싸는 괄호를 지우고 띄어쓰기를 한다.
  4. 엔터와 return을 지운다.
  5. 새로운 변수에 할당한다.

## 6. 재귀함수(recursive function)

- 자기 자신을 호출하는 함수

- 종료되는 상황이 있어야함

- 큰 문제를 풀기 위해 작은 문제들로 나눠가면서 적용

- base case 설정

- 파이썬의 재귀 깊이 = 1000번

- 재귀 / 반복문

- 재귀를 사용하면 가독성이 올라가고 변수 사용 개수가 적어진다

  하지만 재귀횟수가 늘어나면 속도가 느려진다.

## 7. 에러 및 예외처리

- 디버깅
  1. print()문
  2. 개발환경툴(IDE)
  3. python tutor
- 에러메시지 = 해당위치에 메시지가 나옴
- 로직에러 = 원하는 결과값을 만들어내지 못함
- 문법에러
- 예외(Exception)
  1. 문법적으로 올바르더라도 발생함.
  2. 실행중에 감지되는 에러(문법에러 제외)들 = 예외
  3. 모든 예외는 Exception안에 포함되어 있음
- 예외처리

```python
1. [try ~ except ~] - if else와 같은 구조임
try:
    <예외가 발생할 수 있는 문장>
except (한번에 여러 개 사용가능):
    <예외가 발생했을 경우 실행하는 문장>
=> 예외처리를 하면 에러가 났을 경우 프로그램이 중지되지 않고 except문을 실행한 후
이후 문장들을 실행할 수 있다.(프로그램 유지 가능)

2. [try ~ except ~ except ~ except ~...] 
except문은 순차적으로  처리되기 때문에 위에서부터 작은 에러부터 처리한다.
ex) 맨 위 except에 Exception을 설정하면 다음 에러들은 처리되지 않는다!

3. [try ~ except ~ else~ finally ~]
try : 코드 실행
except : try에서 예외발생 시 실행
else : try에서 예외가 발생하지 않았을 경우 실행
finally : 예외와 상관없이 무조건 실행  
=> 결론은 에러의 O, X에 따라 except가 실행되냐 아니면 else가 실행되냐 문제임

4. as키워드를 활용하여 원본 에러 메시지 사용가능
Indexerror as err:
print(f'{err}발생')
```

- 예외를 강제로 발생시키기
  1. raise를 통해 강제로 예외 발생
  2. assert <표현식>, <메시지> - 디버깅 용도
- [try ~ except ~]와 [if ~ else ~]의 차이
  =>일단 시도해보고 성공여부를 따지는지, 
  성공여부를 확인후 시도하는지 차이
