# Python[2021.07.27]

- append 와 extned의 차이
  - append([1,2])했을 때는 리스트에 그대로 [1,2]가 한 덩어리로 추가된다.
  - extend([1,2])했을 때는 리스트에 1, 2가 들어감 => [1,2]을 벗겨내고 기존의 리스트에 추가로 붙여버림.
- 리스트에 있는 내용지우기
  - num = [1,2,3]
    num.clear()
    print(num)
  - num = [1,2,3]
    num = [] => or list()로 하면 새롭게 선언하는거니까 아예다른 주소로 바뀌는 거임
    print(num)
- deepcopy 쓸일이 자주 없으니까 쓰게 되면 다시 한 번 고민해보기 
- 10*10 2중 리스트
  [[0 for _ in range(10)]for _ in range(10)]
- pair = [(boy, girl) for boy in boys for girl in girls] => 이런 것도 있음 boy와 girl의 조합(2중 for문)
- map를 통해 만든 map object는 리스트와 상당히 비슷하다. => 리스트의 기능이라고 생각하는 것들을 거의 다 사용할 수 있음
  => 하지만 그냥 map obj를 list()안에 넣는 것이 좋음 
- map(int, input().split())
  map객체는 한 번 소비하면 그 다음부터 [] 비어있게 된다.
  따라서 계속 사용하기 위해서는 map객체를 list안에 넣어놓는다.
- filter(func, iterable) => iterable을 func에 넣었을때 True값이 나오는 것만 return함(filter obj로)
- zip(*iterable) => 복수의 iterable들을 순서에 맞게 매칭시켜서 묶어줌-튜플로(zip obj)
  만약에 짝이 맞지 않는다면 짝이 없는 element는 안나옴
- set
  .update(*others) - 서로 다른 set들을 합쳐버림
- dictionary
  그냥 dict['a']를 하는 것과 dict.get('a')하는 것은 key가 없을 때 오류를 발생하는 여부에 따라 차이가 있다. .get()에는 default값을 설정할 수 있다.
- for문에 넣을 수 있다? == iterable하다
- 딕셔너리는 거의 key로 접근한다.
- 약간의 활용 예시

```python
sonnet = 
'From fairest creatures we desire increase,
That thereby beauty’s rose might never die,
But as the riper should by time decrease,
His tender heir mught bear his memeory:
But thou, contracted to thine own bright eyes,
Feed’st thy light’st flame with self-substantial fuel,
Making a famine where abundance lies,
Thyself thy foe, to thy sweet self too cruel.
Thou that art now the world’s fresh ornament
And only herald to the gaudy spring,
Within thine own bud buriest thy content
And, tender churl, makest waste in niggarding.
Pity the world, or else this glutton be,
To eat the world’s due, by the grave and thee.'


어떤 단어가 얼마나 등장하는지?
book_title = sonnet.replace(',', '').replace('\n', ' ').lower().split() => 하면 소문자로 연결된 모든 문자가 소문자인 문자열로 바뀜(리스트) 


# 변수명이 book_title인 리스트를 만들어봅시다.
book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

# 2. count 메서드를 활용해 작성해보세요.
# =====
title_counter = {}
for title in book_title:
    title_counter[title] = book_title.count(title)

print(title_counter)

# 3. get 메서드를 활용해 작성해보세요.
# =====
title_counter = {}
for title in book_title:
    title_counter[title] = title_counter.get(title, 0) + 1

print(title_counter)
```

- map => lazy evaluation => 일단은 처리해 놓고 소비하려하면 오류가 날 수 도 있음
- 2차원 리스트 가로로 출력말고도 세로로 출력도 고민하기
- remove는 원하는 요소를 삭제하고 전체 리스트의 빈공간을 당기는 작업을 해야하기 때문에 오래걸림(최후의 수단으로 활용)
- 결국은 iterable한 것에 일관적으로 하나의 func를 적용한다? = map을 떠올리자