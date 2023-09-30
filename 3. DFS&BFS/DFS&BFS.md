# 꼭 필요한 자료구조 기초

- `탐색` : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
- `자료구조` : 데이터를 표현하고 관리하고 처리하기 위한 구조
  - 삽입(Push) : 데이터를 삽입
  - 삭제(Pop) : 데이터를 삭제
- 스택과 큐를 사용할 때는 삽입과 삭제 외에도 `오버플로`와 `언더플로`를 고민해야 함
- `오버플로` : 특정한 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산을 수행할 때 발생. 즉, 저장 공간을 벗어나 데이터가 넘쳐흐를 때 발생
- `언더플로` : 특정한 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행할 때 발생

## 스택

- 선입후출(First In Last Out) 구조 or 후입선출(Last In First Out) 구조

```python
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력 [5, 2, 3, 1]
print(stack[::-1]) # 최상단 원소부터 출력 [1, 3, 2, 5]
```

## 큐

- 선입선출(First In First Out) 구조

```python
from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력 deque([3, 7, 1, 4])
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력 deque([4, 1, 7, 3])
```

## 재귀 함수

- `재귀 함수` : 자기 자신을 다시 호출하는 함수

```python
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()
```

- 재귀 함수가 언제 끝날지, **종료 조건**을 꼭 명시
- 재귀 함수는 내부적으로 스택 자료구조와 동일

```python
# 반복적으로 구현한 n!
def factorial_iterative(n):
   result = 1
   # 1부터 n까지의 수를 차례대로 곱하기
   for i in range(1, n+1):
       result *= i
   return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
   if n<=1:    # n이 1 이하인 경우 1을 반환
       return 1
   # n! = n * (n-1)!를 그대로 코드로 작성
   return n * factorial_recursive(n-1)

print('반복적으로 구현:', factorial_iterative(5)) # 120
print('재귀적으로 구현:', factorial_recursive(5)) # 120
```

# 탐색 알고리즘 DFS/BFS

## 그래프

- 그래프는 노드(정점)와 간선으로 표현
- 그래프 탐색이란 하나의 노드를 시작으로 다수의 노드를 방문하는 것
- 두 노드가 간선으로 연결되어 있다면 '두 노드는 인접하다'라고 표현
- 그래프는 `인접 행렬`과 `인접 리스트` 크게 2가지 방식으로 표현

  - `인접 행렬` : 2차원 배열로 그래프의 연결 관계를 표현하는 방식

  ```python
  INF = 999999999 # 무한의 비용 (연결 되어 있지 않은 노드) 선언

  # 2차원 리스트를 이용해 인접 행렬 표현
  graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
  ]

  print(graph)
  ```

  - `인접 리스트` : 리스트로 그래프의 연결 관계를 표현하는 방식

  ```python
  # 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
  graph = [[] for _ in range(3)]

  # 노드 0에 연결된 노드 정보 저장(노드, 거리)
  graph[0].append((1, 7))
  graph[0].append((2, 5))

  # 노드 1에 연결된 노드 정보 저장(노드, 거리)
  graph[1].append((0, 7))

  # 노드 2에 연결된 노드 정보 저장(노드, 거리)
  graph[2].append((0, 5))

  print(graph)
  ```

### `인접 행렬`과 `인접 리스트`의 차이

|             | 인접 행렬     | 인접 리스트 |
| ----------- | ------------- | ----------- |
| 메모리 측면 | 불필요한 낭비 | 효율적      |
| 속도 측면   | 효율적        | 비교적 느림 |

## DFS

- `DFS (Depth-First Search)` : 깊이 우선 탐색. 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색
- 동작 과정

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접 노드가 없으면 최상단 노드를 꺼냄
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복

- 데이터의 개수가 N개인 경우 O(N)의 시간 소요

```python
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문한 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

## BFS

- `BFS (Breadth First Search)` : 너비 우선 탐색. 가까운 노드부터 탐색하는 알고리즘
- 동작 과정

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복

- O(N)의 시간 소요
- 일반적인 경우 실제 수행 시간은 `DFS`보다 좋은 편

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문한 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
```

### `DFS`와 `BFS`

|           | DFS       | BFS         |
| --------- | --------- | ----------- |
| 동작 원리 | 스택      | 큐          |
| 구현 방법 | 재귀 함수 | 큐 자료구조 |

## 문제

<details>
  <summary>음료수 얼려 먹기</summary>
  <div markdown="1">

Q. N X M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

`입력 조건` :

- 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1<=N, M<=1,000)
- 두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어진다.
- 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.<br>

`출력 조건` :

- 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

<문제 해설>

- `DFS`로 해결

  </div>
</details>

<details>
  <summary>미로 탈출</summary>
  <div markdown="1">

Q. 동빈이는 N X M 크기의 직사각형 형태의 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

`입력 조건` :

- 첫째 줄에 두 정수 N, M (4<=N, M<=200)이 주어진다. 다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다. 각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.<br>

`출력 조건` :

- 첫째 줄에 최소 이동 칸의 개수를 출력한다.

<문제 해설>

- `BFS`로 해결

  </div>
</details>

<br>
