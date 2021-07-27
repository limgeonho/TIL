# Python[2021.07.26]

## 1. 데이터구조

- 문자열
- 리스트
- 세트
- 딕셔너리
- 순서가 있는 데이터 구조(시퀀스)
  - 문자열, 리스트
- 순서가 없는 데이터 구조(비시퀀스)
  - 세트, 딕셔너리

## 2. 문자열

- 순서O, 변경불가능(immutable), 반복O, 인덱싱, 슬라이싱
- immutable, ordered, iterable
- [methods]
  1. str.find(x) - x의 첫 번째 위치를 반환, 없으면 -1을 반환
  2. str.index(x) - x의 첫 번째 위치를 반환, 없으면 ValueError, find()와 다름*
  3. str.replace(old, new[, count]) - 빠꿀 대상 글자를 새로운 글자로 바꿔서 반환(복사본 반환), count지정하면 해당 개수만큼만 시행*
     	'wooooowoo'.replace('o', '!', 2) == w!!ooowoo
     	[]안에 감싸져 있으면 = 선택척인자(BNF표기법)
  4. str. strip([chars]) - 특정 문자를 지정하면 양쪽에 해당 문자를 전부제거, 아니면 공백제거(복사본 반환)*
  5. str.split(sep=None) - 문자열을 특정한 단위로 나눠서 리스트로 반환*
  6. 'separator'.join(iterable) - 반복가능한 컨테이너 요소들을 separator로 합쳐 문자열 반환*
  7. str.capitalize() - 첫 문자를 대문자, 나머지는 소문자
  8. str.title() - '(싱글쿼트) 나 공백 이후의 단어 첫 문자를 대문자로
  9. str.upper() - 대문자로*
  10. str.lower() - 소문자로*
  11. str.swapcase() - 대문자 => 소문자, 소문자 => 대문자*
  12. str.isalpha() - 알파벳 문자 여부*
  13. str.isupper() - 대문자 여부
  14. str.islower() - 소문자 여부
  15. str.istitle() - 타이틀 형식 여부

## 3. 리스트

- mutable, ordered, iterable

- [methods]

  - 추가

  1. list.append(x) - 리스트의 끝에 값을 추가함
  2. list.extend(iterable) - 리스트에 iterable를 추가함
  3. list.insert(idx, x) - 정해진 위치 idx에 값x를 추가함

  - 삭제

  1. list.remove(x) - 리스트에서 값이 x인 첫번째 항목 삭제, 없으면 ValueError
  2. list.pop(idx) - 정해진 위치 idx에 있는 값을 삭제하고, 그 항목을 반환함, idx가 없으면 마지막 항목 삭제
  3. list.clear() - 모든 항목을 삭제함

  - 탐색 및 정렬

  1. list.index(x) - x의 첫 번째 위치를 반환, 없으면 ValueError
  2. list.count(x) - 원하는 값 x의 개수를 반환함, 없으면 0을 반환
  3. list.sort() - 원본 리스트를 정렬함, None를 반환
  4. sorted(list) - 리스트를 정렬함, 원본은 변화가 없고 정렬된 새로운 리스트를 반환함
  5. list.reverse() - 순서를 반대로 뒤집음(정렬x), sort()와 같은 맥락

- 얕은 복사

  1. 리스트는 mutable이기 때문에 복사해도 같은 주소를 참조한다.
     => 따라서 리스트를 복사 하기 위해서는 
     a = [1,2,3]
     b = a[:] 처럼 a리스트를 전체를 출력한 결과 값을 저장해주면된다.
  2. a = [1,2,3]
     b = list(a) 도 가능하다
  3. 얕은 복사 주의사항
     리스트안에 다른주소를 참조하는 리스트가 원소로 있다면 그 값을 바꿨을 때 원본도 바뀜...
     => 해결하기 위해서는 deep copy를 해야함

- 깊은 복사

  1. import copy
     a = [1,2,['a', 'b']]
     b = copy.deepcopy(a)
     하면 내부 리스트의 원소까지 바꿀 수 있음!!

- List comprehension

  - 1~3의 세제곱의 결과가 담긴 리스트를 만드시오
    a = []
    for num in range(1, 4):
        a.append(num**3)
    => [num**3 for num in range(1, 4)]
    => <표현식> for 변수 in range()
  - a = []
    for num in range(1, 4):
        if num % 2 == 0:    
            a.append(num)
    => [num for num in range(1, 4) if num % 2 == 0]
    => <표현식> for 변수 in range() <if문, 조건문>
    ==> 하지만 가독성 측면에서는 원래 있던 식이 더 좋음

- map(function, iterable) - iterable 의 모든 요소에 function을 적용하고 그 결과를 map object로 반환

- filter(function, iterable) - map과 다 같지만 function의 True값만 반환함

- zip(*iterable) - 복수의 iterable을 모아 튜플을 원소로하는 zip object를 반환, 각각의 iterable들을 순차적으로 1:1매칭해서 튜플로 반환해줌...

## 4. 세트

- mutable, unordered, *iterable
- [methods]
  1. .add(elem) - 세트에 값을 추가
  2. .update(*others) - 여러 값을 추가
  3. .remove(elem) - 세트에서 삭제하고 없는 값이면 ValueError
  4. .discard(elem) - 세트에서 삭제하고 없어도 에러가 발생하지 않음
  5. .pop() - 순서가 없기 때문에 임의의 원소를 제거해 반환, 세트가 비어있는 경우 KeyError

## 5. 딕셔너리

- mutable, unordered, *iterable
- [methods]
  1. .get(key[, default]) - key에 대응하는 value값을 가져옴, default값을 설정하여 key가 없을때 default로 조회
  2. .pop(key[, default]) - key에 대응하는 value값을 뽑아서 반환, default값을 설정하여 key가 없을때 default로 조회
  3. .update() - 기존의 키를 입력해서 value값을 갱신, .update(apple = '사과') => 특징은 원래 dict에 넣을때 key는 문자열이지만 여기서는 그냥 apple= 구조로 추가함
  4. .keys() - key값을 반환함
  5. .values() - value값을 반환함
  6. *.items() - key, value 깂을 튜플로 반환함

## 6. 기타

- 사실상 1)변경 2)조회가 주 목적임
- 자료구조가 가지고 있는 메서드를 알고 싶으면 dir('string')하면 다나옴
- .메서드() / 함수() => 앞에 .의 여부
- 변경하는 기능만!! / 조회는 return이 있겠지... 당연히
  - str은 변경불가능하기 때문에 원본을 바꿀 수 없음 => return값으로 결과를 보여준다. => 다른 변수에 새롭게 할당해줘야함
  - 하지만!! list는 변경가능하고 추가가능하기 때문에 새로운 원소를 추가하였을때 return해주지 않아도 된다. => 다른 변수에 할당할 필요X