knight = input()
row = int(knight[1])
column = int(ord(knight[0])) - 97 + 1
way = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, 2], [1, -2], [2, 1], [2, -1]]
cnt = 0
for i in way:
    nrow = row + i[0]
    ncolumn = column + i[1]
    if nrow >= 1 and nrow <= 8 and ncolumn >= 1 and ncolumn <= 8:
        cnt += 1
print(cnt)
