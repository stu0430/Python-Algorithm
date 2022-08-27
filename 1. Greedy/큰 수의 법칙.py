N, M, K = map(int, input().split())

num = list(map(int, input().split()))

num.sort()

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += num[-1]
        M -= 1
    if M == 0:
        break
    result += num[-2]
    M -= 1

print(result)

# N, M, K를 공백으로 구분하여 입력받기
# n,m,k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))

# data.sort() # 입력받은 수 정렬
# first = data[n-1] # 가장 큰 수
# second = data[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
# count = int(m / (k + 1)) * k
# count += m % (k + 1)

# result = 0
# result += (count) * first # 가장 큰 수 더하기
# result += (m - count) * second # 두 번째로 큰 수 더하기

# print(result) # 최종 답안 출력
