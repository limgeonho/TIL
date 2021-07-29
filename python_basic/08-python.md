# Python[2021.07.29]

- self 는 인스턴스 자신을 의미한다
- def test(self) = self는 메서드의 매개변수에 맨 처음에 반드시 들어가지만 호출될 대는 없어도 알아서 인식함
- Person() = 이것도 함수처럼 호출되는데() 그러면 뭐가 실행되는거지?
  => 생성자가 실행되는 것임 __init__(self, name): self.name = name
- 메서드 내부에서 self를 사용하지 않아도 정의할 때는 매개변수로 써준다 = self는 고정값이니 무조건 써준다!!!
- 매직메서드는 내가 실행하는 것이 아니라 내부적으로 알아서 실행된다.(실행되는 시점이 정해져 있음)

```python
def __str__(self): 
    return f'나는 {self.name}' 
p2 = Person()
print(p2) 
# 출력을 실행하면 나는 {self.name}으로 실행됨 
# __str__(self)을 바꿔줬기 때문에(자바 toString와 비슷한듯) - 이 행위자체가 오버라이딩

```

- self, other활용 예시

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return self.age > other.age
    def __eq__(self, other):
        return self.age == other.age

# self는 메서드를 호출하는 인스턴스가 들어가고 other은 인자로 들어오는 인스턴스

p1 = Person('1', 1)
p2 = Person('2', 2)
p3 = Person('3', 1)

print(p1 > p2)    => False
print(p1 == p3)  => True
print(p1 == p2)  => False
```

- 모든 객체는 속성과 메서드를 갖는다

- 클래스 또한 객체이다

- 따라서 클래스도 속성과 메서드를 가져야한다.(그러면 어디에 정의해야 할까?)

  => 인스턴스 안에 정의할 수 없고 상위 클래스인 Meta class에도 정의할 수 없기 때문에
  => 클래스의 속성과 메서드도 클래스 내부에 저장해야한다.(어쩔수 없음)

- self.<속성>, 인스턴스.<속성> => 인스턴스의 속성에 접근

- 클래스.<속성> => 클래스 속성에 접근

- 이름공간 탐색 순서
  1. 클래스를 정의하면, 클래스가 생성됨과 동시에 이름 공간(namespace)이 생성됩니다.
  2. 인스턴스를 만들게 되면, 인스턴스 객체가 생성되고 해당되는 이름 공간이 생성됩니다.
  3. 인스턴스의 속성이 변경되면, 변경된 데이터를 인스턴스 객체 이름 공간에 저장합니다.
  4. 인스턴스에서 특정한 속성에 접근하게 되면 인스턴스 => 클래스 순으로 탐색을 합니다.

- 클래스 메서드 - @classmethod 데코레이터 붙여줘야함

```python
class Circle:
    @classmethod
    def intro(cls):
        print(cls)
Circle.intro()

# 인스턴스와 같은 맥락으로 intro()안에는 먼저 cls라고 클래스가 호출했다고 알려줘야함
```

- 인스턴스는 인스턴스메서드만 호출하고
  클래스는 클래스메서드와 스태틱메서드만 사용하자(Convention)

- 인스턴스 메서드를 정의할 때 첫 번째 인자 = self
  클래스 메서드를 정의할 때 첫 번째 인자 = cls

- 상속

  DRY = Don't Repeat Yourself

- class Student(Person):
  부모클래스 Person의 속성과 메서드를 활용할 수 있다.

- super()

  - 자식클래스에서 부모클래스의 메서드를 일부 활용하고 추가하려고 할 때(오버라이딩)
  - super() = 또한 하나의 클래스다(type(super())해보면 class super로 나옴)

```python
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        self.student_id = student_id

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # Person 클래스
        super().__init__(name, age, number, email)
        self.student_id = student_id

# 부모클래스의 생성자 앞에 super().~으로 써주고 이후에 자식클래스에서 추가할 속성 추가
```

- @property

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    @property
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

r1 = Rectangle(4, 8)
print(r1.area)
print(r1.perimeter())

# 원래는 r1.area() 로 호출해야하지만 @property 덕분에 r1.area로 호출가능해짐 = 속성값처럼
# 하지만 def area(self, x): = 처럼 추가인자가 들어가야하는 경우에는 불가능 => 추가적이지 않은 고정된 값을 갖는 메서드 위에만 사용할 수 있도록하자

```

- 메서드 내부일때,
  self.attr 일때, attr은 클래스 이름공간 탐색의규칙을 따른다(인스턴스 => 클래스 => 부모클래스 => ... => type)
  var은 함수 내부의 이름공간 탐색규칙을 따른다.
  =
  함수는 어떤 상황에서든지 변수를 local에서 찾아보고 없으면 global로 넘어간다(LEGB)
  하지만 self.<속성>일때 <속성>을 인스턴스 => 클래스 순으로 찾아나간다