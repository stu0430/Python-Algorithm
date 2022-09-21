n = int(input())
arr = set(map(int, input().split()))

m = int(input())
arr_2 = list(map(int, input().split()))

for i in arr_2:
    if i in arr:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 이분 탐색 이용  
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid +1
#     return None

# n = int(input())
# arr = list(map(int, input().split()))

# arr.sort()

# m = int(input())
# arr_2 = list(map(int, input().split()))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

# for i in arr_2:
#     x = binary_search(arr, i, 0, n -1)
#     if x != None:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# 계수 정렬 이용
# n = int(input())
# arr = [0] * 1000001

# for i in input.split():
#     arr[int(i)] = 1
    
# m = int(input())
# arr_2 = list(map(int, input().split()))

# for i in arr_2:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end= ' ')