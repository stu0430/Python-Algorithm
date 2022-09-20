# 범위를 반씩 좁혀가는 탐색

## 순차 탐색

- `순차 탐색` : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
- 정렬되지 않은 리스트

```python
# 순차 탐색 소스 코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환

print('생성할 원소의 개수와 찾을 문자열을 입력하세요.')
input_data = input().split() 
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 문자열

print('앞서 적은 원소의 개수만큼 문자열을 입력하세요.')
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
```

- 시간 복잡도 : O(N)

## 이분 탐색

- `이분 탐색` : 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해 원하는 데이터를 찾는 방법
- 이미 정렬되어 있는 배열

```python
# 이진 탐색 소스 코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# 이진 탐색 소스 코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
```

- 시간 복잡도 : O(logN)
- 탐색 범위가 2,000만을 넘어가면 이진 탐색으로 문제에 접근

## 트리 자료구조