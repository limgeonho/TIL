# HTML_and_CSS[2021.08.05]

## 1. basic

- 부모 태그에서 상속하려고해도 자식태그가 자신만의 class를 가진다면 cascading때문에 상속되지 않고 자식태그의 속성을 갖는다.
- container > row > col => 12칸
- .container-fluid하면 제한되지 않은 화면 전체의 container을 사용할 수 있다.

## 2. grid system

- container은 필수

- row는 12개로 쪼개는 가로 공간

- col은 12칸 중 얼마나 차지할지

- 만약에 전체는 12로 고정되어 있지만 1/24를 사용하고 싶다면?

  col-6으로 나눈 결과 내부에 새로운 row를설정하고 다시 분배하면 가능하다.

  (row는 가로공간을 12로 분할 하는 것)

- 반응형 웹

  1 source multi use

## 3. breakpoint

- col-12 col-md-8
  => 원래는 col-12가 전체를 12를 차지하고 있었지만
  => col-md-8이 나온 순간 부터 col-12는 처음부터 md가 나오는 순간까지만 12의 공간을 차지한다
  => md를 넘어서는 순간 8의 공간을 차지한다
  => col-<size>-<num> : 진행해 오다가 size가 나오는 순간 부터 설정하는 값으로 바뀜
- 요즘 대부분 브라우저는 md로 잡고 시작한다.
- offset
  offset도 col과 같은 방식으로 동작함
  offset-8 => 앞에서 부터 8칸을 빈칸으로 차지한다
  offset-md-8 => md크기부터 8칸짜리 빈칸(offset)가 적용된다. 
