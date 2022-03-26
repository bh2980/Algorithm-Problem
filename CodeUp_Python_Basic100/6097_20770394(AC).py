w, h = input().split()
w = int(w)
h = int(h)
matrix = [[0 for i in range(0, h)] for i in range(0, w)]
n = int(input())

while n>0:
    n -= 1
    l, d, x, y = input().split()
    l = int(l)
    d = int(d)
    x = int(x)
    y = int(y)

    if d:
        for i in range(x, x+l):
            matrix[i-1][y-1] = 1
            
    else:
        for i in range(y, y+l):
            matrix[x-1][i-1] = 1

for i in range(0, w):
    for j in range(0, h):
        print(matrix[i][j], end=' ')
    print()

