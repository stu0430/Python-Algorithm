n = int(input())

students = []

for i in range(n):
    a, b = map(str, input().split())
    b = int(b)
    students.append((a, b))

students = sorted(students, key=lambda x:x[1])

for i in students:
    print(i[0], end=' ')