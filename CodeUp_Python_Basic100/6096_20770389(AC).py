d = [[0 for i in range(0, 19)] for i in range(0, 19)]

for i in range(0, 19):
    s = input().split()
    for j in range(0, 19):
        d[i][j] = int(s[j])

a = int(input())

while a>0:
    a -= 1
    b, c = input().split()
    for i in range(0, 19):
        d[i][int(c)-1] = int(not(d[i][int(c)-1]))
    for i in range(0, 19):
        d[int(b)-1][i] = int(not(d[int(b)-1][i]))

for i in range(0, 19):
    for j in range(0, 19):
        print(d[i][j], end=' ')
    print()
