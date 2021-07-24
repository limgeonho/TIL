# 1주차 Keywords(7.19 ~ 7.23)

## [python 기초]

1. 주석
2. 변수
3. 할당연산자
4. 식별자
5. 데이터타입(숫자, 문자, 참/거짓)
6. 부동소수점(float)
7. 소수의 뺼셈
  abs(a-b)<=1e-10 | sys.float_info.epsilon | math.isclose(a,b)
8. 복소수(complex)
9. 문자열
10. 이스케이프 시퀀스
11. string interploation(f-string)
12. 참/거짓
13. None타입(값이 없음을 표현하는 것)
14. 형변환
15. 암시적형변환(정수, 소수, 복소수, 참/거짓)
16. 명시적형변환(나머지 전부) - string -> Integer은 형식에 맞아야만 가능
    a = '3.5' -> float(a)을 먼저해서 float로 만들어주고 -> int(float(a))==3 소수에서 소수점부분이 없는 정수부분으로 변환
17. 연산자
18. 산술연산자(+, -, *, /, //, %, **)
19. 비교연산자(<, <=, >, >=, ==, !=, is, is not)
20. 논리연산자(and, or, not)
21. 단축평가
22. 복합연산자(+=...)
23. 기타주요연산자
24. Concatenation(숫자가 아닌 자료형을 +연산자로 합침)
25. Containment test(in연산자를 사용해서 속해있는지 여부파악)
26. Identity(is연산자를 통해 동일한 object인지 확인)
27. indexing, slicing
28. 연산자우선순위((),slicing,indexing,**,+-,산술,in is, not,and,or)
29. 표현식(하나의 값으로 환원될 수 있는 문장)
30. 문장(실행 가능한 최소한의 코드)
    표현식은 문장에 포함된다.

## [Container]

1. 시퀀스형 컨테이너(정렬x, 특정위치의 데이터지목가능, 순서o)

2. 리스트

3. 튜플(immutable)

4. 레인지

5. 시퀀스에서 활용할 수 있는 연산자

   x in s, x not in s, s1 + s2, s*n, s[i], s[i:j], s[i:j:s], len(s), min(s), max(s), s.count(x)

6. 비시퀀스형 컨테이너(순서x)

7. set - set()를 통해서 만들어야함 - 합집합(|), 차집합(-), 교집합(&)연산 가능

8. 딕셔너리(key, value) - (immutable)

   dict_a.keys(), dict_a.values(), dict_a.items()

9. 컨테이너 형변환(range, dict빼고는 다됨) - string, list, tuple, set

10. 데이터의 분류

11. immutable(변경 불가능) - 리터럴(숫자, 글자, 참/거짓), range, tuple, frozenset

12. mutable(변경 가능) - list, dict, set

## [Control Statement]

1. control flow(조건문, 반복문)

2. 조건문(if-else, if-elif-else)

3. 중첩조건문

4. 조건표현식(삼항연산자) - 참일때 값 if <expression> else 거짓일때 값

5. 반복문

6. while 반복문

7. for 문(시퀀스형 객체를 순회함)

   enumerate -> idx와 value를 돌려줌(튜플로)

8. 반복제어(break, continue, for-else)

9. break

10. continue

11. for-else

12. pass

## [function_1]

1. 함수 - 일의 단위, (가독성, 재사용성, 유지보수)

2. parameter(매개변수), argument(인자)

3. return(한 개의 객체만)

4. 매개변수 - 함수의 정의 부분에서 보임

5. (전달)인자 - 전달되는 값

6. 함수의 인자

7. 위치인자(positional argument)

8. 기본인자(default argument)

   위치 - 기본 순(정의시 parameter순서)

9. 키워드인자(keyword)

   위치 - 키워드 순(호출시 argument순서)

10. 정해지지 않은 여러 개의 인자처리

11. 가변 인자 리스트(*args) - args는 튜플로 받아옴

12. 가변  키워드 인자(**kwargs) - kwargs는 딕셔너리로 받아옴

## [function_2]

1. 함수와 스코프

2. 변수의 생명주기(빌트인, 전역, 지역)

3. 이름검색규칙(LEGB)

4. global, nonlocal

5. 재귀함수

6. 반복문과 비슷(특히, while 문)

7. base case

8. 재귀함수와 반복문의 장단점

   재귀함수는 직관적, 변수사용적음 하지만 메모리, 시간 많음

## [에러 & 예외처리]

1. 에러

2. 문법에러

   EOL, EOF

3. 예외(Exception) - 발생하면 프로그램 멈춤

4. ZeroDivisionError, NameError, TypeError, ValueError, IndexError, KeyError, ModuleNotFoundError, ImportError, KeyboardInterrupt

5. 예외처리

6. try ~, except ~

7. try ~, except ~, except ~, else ~

8. try ~, except ~, except ~, else ~, finally ~

9. 에러메시지 처리(as)

10. 예외 발생 시키기

11. raise

12. assert

