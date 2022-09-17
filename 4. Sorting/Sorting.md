# 기준에 따라 데이터를 정렬

- `정렬` : 데이터를 특정한 기준에 따라서 순서대로 나열
- 정렬 알고리즘은 `이진 탐색`의 전처리 과정

## 선택 정렬

- `선택 정렬` : 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 과정을 반복하는 정렬

```
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)
```
- 시간 복잡도 : O(N^2)

## 삽입 정렬

- `삽입 정렬` : 특정한 데이터를 적절한 위치에 삽입하는 정렬

```
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
```

- 시간 복잡도 : O(N^2)
- 거의 정렬된 상태인 경우 매우 빠르게 동작

## 퀵 정렬

- `퀵 정렬` : 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 정렬
- 피벗 : 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 기준

```
# 퀵 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

# 파이썬의 장점을 살린 퀵 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```

- 시간 복잡도 : O(NlogN)
- 거의 정렬된 상태인 경우 매우 느리게 동작

## 계수 정렬

- `계수 정렬` : 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬
- *데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때*만 사용
- 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용

```
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
    
for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
```

- 시간 복잡도 : O(N + K), K(데이터 중 최대값의 크기)
- 데이터의 크기가 한정되어 있고, 데이터의 크기가 많이 중복되어 있을수록 유리

## 문제

<details>
  <summary>위에서 아래로</summary>
  <div markdown="1">

Q. 하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다. 이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다. 수열을 내림차순으로 정렬하는 프로그램을 만드시오.

`입력 조건` :

- 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다. (1<=N<=500)
- 둘째 줄부터 N + 1번째 줄까지 N개의 수가 입려고딘다. 수의 범위는 1 이상 100,000 이하의 자연수이다.<br>

`출력 조건` :

- 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다. 동일한 수의 순서는 자유롭게 출력해도 괜찮다.

<문제 해설>

- 파이썬의 기본 정렬 라이브러리 이용

  </div>
</details>

<details>
  <summary>성적이 낮은 순서로 학생 출력하기</summary>
  <div markdown="1">

Q. N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.

`입력 조건` :

- 첫 번째 줄에 학생의 수 N이 입력된다. (1<=N<=100,000)
- 두 번째 줄부터 N + 1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다. 문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.<br>

`출력 조건` :

- 모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.

<문제 해설>

- 파이썬의 기본 정렬 라이브러리 이용

  </div>
</details>

<details>
  <summary>두 배열의 원소 교체</summary>
  <div markdown="1">

Q. 동빈이는 두 개의 배열 A와 B를 가지고 있다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다. 동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다. 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며, 여러분은 동빈이를 도와야 한다.
N, K, 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오.

`입력 조건` :

- 첫 번째 줄에 N, K가 공백으로 구분되어 입력된다. (1<=N<=100,000, 0<=K<=N)
- 두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.
- 세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.<br>

`출력 조건` :

- 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력한다.

<문제 해설>

- 배열 A에서 가장 작은 원소를 골라 배열 B에서 가장 큰 원소와 교체
- O(NlogN)을 보장하는 정렬 알고리즘 이용

  </div>
</details>

<br>