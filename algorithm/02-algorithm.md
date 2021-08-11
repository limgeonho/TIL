# Algorithm[2021.08.11]



## 1. List(2차원 리스트)

- 선언 : 파이썬에서는 리스트를 받을때 split()가 한 줄을 받아오기 때문에 행의 개수를 알고 있으면 2차원 리스트 생성 가능
- arr1 = [list(map(int, input().split())) for _ in range(N)]
- arr2 = [[0]*M for _ in range(N)]
  => 0으로 초기화되어있는 2차원 리스트
- 순회 방향

```python
# 행 우선 순회
for i in range(len(Array)):
  for j in range(len(Array[i])):
    Array[i][j] => 필요연산수행

# 열 우선 순회
for j in range(len(Array[0])):
  for i in range(len(Array)):
    Array[i][j] => 필요연산수행

# 지그재그 순회
for i in range(len(Array)):
  for j in range(len(Array[0])):
    Array[i][j + (m-1-2j) * (i%2)]

# 델타를 이용한 2차원 리스트 탐색
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
=> 시계 방향

for x in range(len(arr)):
  for y in range(len(arr[x])):
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < len(arr) and 0 <= ny < len(arr[x])        
        arr[nx][ny]

# 2차원 리스트를 이용한 순회
for i in range(N):
  for j in range(M):
    for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
      ni = i + dr
      nj = j + dc
      if 0 <= ni < N and 0 <= nj < M:
        arr[ni][nj]
        
# 전치행렬
for i in range(3):
  for j in range(3):
    if i < j:
      arr[i][j], arr[j][i] = arr[j][i], arr[i][j] 


# => 내가 항상 2차원 리스트를 만들거나 순회할때 n, i로 사용하는 것이 열(세로)임. 

```



## 2. 부분집합

```python
# 부분집합
arr = [1, 2, 3, 4]

bit = [0, 0, 0, 0]
for i in range(2):
  bit[0] = i
    for j in range(2):
       bit[1] = j
         for k in range(2):
           bit[2] = k
             for l in range(2):
               bit[3] = l
                 for p in range(4):
                   if bit[p]:
                     print(arr[p], end=' ')                

# 비트연산자
1<<n   =>   부분집합의 개수(n개의 원소일 때)

# 비트연산자를 활용한 부분집합 찾기
arr = [1, 2, 3, 4, 5, 6]
n = len(arr) => 원소의 개수

for i in range(1, 1<<n): => 1<<n: 부분집합의 개수(공집합 제외) 
  for j in range(n): => 원소의 수만큼 비트를 비교함
    if i & (1<<j): => i의 j번째 비트가 1이면 j번째 원소 출력
      print(arr[j], end=", ") 
  print()
print()

```



## 3. 검색(순차검색, 이진검색)

1.  순차 검색

- 순차검색 - 일렬로 되어 있는 자료를 순서대로 검색하는 방법
  - 가장 간단하고 직관적임
  - 배열이나 연결리스트 등 순차구조로 구현된 자료구조에서 유용
  - 대상의 수가 많아지면 시간이 오래걸림

- 정렬O - 검색 실패를 반환하는 경우 평균 비교 회수가 반으로 줄어든다.
- 정렬X - 순서대로 처음부터 전부 돌아야함(마지막까지 갔는데 없으면 실패)

2.  이진 검색

- 처음과 끝의 중간지점을 통해 찾는 수와 비교하며 위치를 결정하고 반복한다
- 반드시 정렬되어 있어야한다

```python
# 이진 탐색 순서
'''
1. 자료의 중앙원소를 고른다
2. 중앙원소와 목표값을 비교한다
3. 목표값이 중앙원소보다 작으면 왼쪽의 반에서 새로검색
4. 반복
'''

# 이진탐색(재귀함수로 구현)
# target 수를 입력 받고 리스트안에서 target의 위치를 반환하는 방법
# 이진탐색을 하기 위해서는 리스트가 정렬이 되어 있는게 전제되어야 한다.

# =====================================================================
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)

# =====================================================================
# 이진탐색(반복문으로 구현)
def binary_search(array, target, start, end):
    while start <= end:

        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)

```

3.  선택정렬 - 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택해서 위치 교환

   

## 4. 기타

- 배열은 전체 길이가 정해지면 더 이상 수정이 불가능
  리스트는 가변적으로 길이가 알아서 조정된다
- matrix.append([0, *map(int, input().split()), 0]) => *은 언팩연산자
  => [0, 1, 2, 3, 4, 5, 0] => *을 사용하면 map객체가 list에 넣지 않아도 자동으로 풀려서 기존 matrix에 누적된다.
- 비트연산자

```python
# 비트 = 0 / 1
3 & 5 = 1
# => 이진수로 변환한 다음 and 연산

1<<2 = 4
1<<3 = 8
# => 1을 왼쪽으로 몇 번 보냄?
# => 1 * 2의 몇 제곱

5<<7
# => 5 * (2**7)

1<<5 == 2**5
# => 1 * (2**5) 
```



