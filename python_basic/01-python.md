# Python[2021.07.19]

### 1. 특징

- 인터프리터 언어 -  한 줄 씩 실행하기 때문에 느릴 수도 있음(하지만 빌드 x)
- 객체지향 언어
- 변수에 별도의 타입지정 필요 x

### 2. 실행환경

- python IDLE(설치하면 따라옴)을 이용(대화형)
- jupyter lab - 웹 환경에서 코드작성 가능(ex. google colab)
- IDE - pycharm, vscode - 직접 파이썬(.py)스크립트 파일을 직접 실행

### 3. 코드 스타일 가이드

- PEP8에서 권장하는 스타일을 습관화 해야함
- 코드는 한 줄에 한 문장이지만 (;)을 사용해서 여러문장 가능(비추)
- docstring(""" """) - 클래스에 대한 설명(javadoc와 비슷한듯)

### 4. 변수

- 변수는 할당연산자(=)를 통해 할당

- id()로 메모리 주소 확인 가능

- (=)로 저장하고 식별자 규칙에 의해 이름을 짓는다

- 데이터 타입

  1. 숫자 - int, float, complex(복소수)
  2. 문자열
  3. 참 / 거짓
  4. None

- 부동소수점을 계산하면 근사치로 나오기 때문에 같아보여도 사실은 False

- ```python
  import math
  math.isclose(3.14 - 3.02, 0.12)
  ```

- complex = 실수부 + 허수부(a.real , a.imag)

### 5. String interpolation

- str.format() == print('안녕!!{}'.format(name)) == 옛날...
- f-string == print(f'안녕!!{name}') == python 3.6부터 ㄱㄱ

### 6. 자료형 변환

- 암묵적 변환(내부에서 알아서)

- 명시적 변환(내가 직접 의도적으로 변환) == 두 변수끼리 연산되지 않는 것을 알기 때문에

  ex) 문자열은 암묵적으로 변환되지 않기 때문에 명시적으로 변환해줘야함...int('7')

### 7. 문장과 표현식

- 표현식(expression) = 하나의 값으로 환원될 수 있는 문장(식별자, 연산자, 값)로 구성
- 문장(statement) = 파이썬이 실행 가능한 최소한의 코드 단위
- 문장이 표현식을 포함하기 때문에 모든 표현식은 문장이라고 할 수 있음.

### 8. 컨테이너(container)

- 여러개의 값을 저장할 수 있는 것(객체)
- 시퀀스형(정렬 X) : list, tuple, range, string, binary => index로 접근가능
- (1) => int임
- (1,) => tuple임
- tuple는 사용자가 사용한다기 보다는 내부적으로 많이 사용함
- tuple와 list의 가장 큰 차이점은 tuple는 값을 변경할 수 없다는 것이다.

### 9. 비시퀀스형 컨테이너(set)

- set()로 생성
- 집합과 같은 구조
- 중복된 값 x

### 10. 비시퀀스형 컨테이너(dict)

- dict(), {}로 생성가능
- key와 value값으로 이루어져있음
- key는 변경불가능 + 중복x
- dict_a = {'a': 1, 'b': 2}
- dict_b  = dict(a = 1, b = 2)

### 11. 변경불가능한 데이터와 변경가능한 데이터

- 변경 불가능 : 리터럴(number, string, boolean), range, tuple
- 변경 가능 : list, dict, set
- 변경 가능한 데이터는 다른 객체로 복사한 뒤에 값을 재할당하면 기존의 객체값도 바뀐다
- => 이유는 두 객체가 같은 주소 값을 참조하고 있기 때문이다.
- 시퀀스형 컨테이너 : list, string, tuple, range
- 비시퀀스형 컨테이너 : dict, set

### 12. 기타...

1. 삼항연산자

   => <True인 경우 값> if <expression> else <False인 경우 값>

2. for ~ else ~ 문

   => 끝까지 for문을 실행시킨 후에 else문을 실행시킴(중간에 break로 종료되면 x)

3. 데이터 값

   => 비어있지 않는다면 무조건 True(공백도 해당)

   => 비어 있으면 무조건 False + 0

4. 단축평가

   => and연산자는  False가 나온 순간 뒤에 있는 정보는 읽지도 않는다.

   => or연산자도 True가 나온 순간 뒤에 있는 정보는 읽지 않고 True를 return한다.
