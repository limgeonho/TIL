# Python[2021.07.20]

### 

### 1. iterable

- iterable하다는 것은 for문에 넣을 수 있다는 것이다.
- str, list는 가능하지만 int는 불가능
- 기타...
- 제곱근은 **(0.5)
- http://pythontutor.com/ 를 통해서 웹으로 바로 python가능

### 2. 변경 불가능 데이터 / 변경 가능 데이터

- 변경 불가능(immutable) : 리터럴(number, string, boolean), range, tuple. frozenset

  => 값이 절대 바뀌면 안되고 만약에 내가 생각하는 다른 값을 넣는 것은 새로운 객체가 생성되는 것임... 하지만 mutable인 list에 값을 추가하는 것은 추가전과 후가 id값이 같음

- 변경 가능(mutable) : list, set, dict

- 포인팅과 래퍼런싱

  => 참조 값을 갖기 때문에 예를 들면 list_a를 list_b에 복사 했을때 결국 같은 주소를 가지고 있기 때문에 하나의 list값을 변경하면 list_a와 list_b의 값이 모두 바뀐다.

### 3. sort()와 sorted()

- sorted(<list>) : 오름차순 정렬을 하지만 원본에는 변화가 없고 정렬된 list를 return 해줌

- <list>.sort() : 오름차순 정렬을 하지만 원본에 변화가 있고 return값이 없음

- 문자열 거꾸로 출력

  => 숫자 덧셈과 다르게 더하려는 문자를 앞에서부터 더하면 거꾸로 출력가능