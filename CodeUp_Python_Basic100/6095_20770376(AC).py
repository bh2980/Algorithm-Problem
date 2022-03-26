d = [0 for i in range(0, 19)]
for i in range(0, 19):
    d[i] = [0 for i in range(0, 19)]

num = int(input())
while num>0:
    num -= 1
    a, b = input().split()
    d[int(a)-1][int(b)-1] = 1


for i in range(0, 19):
    for j in range(0, 19):
        print(d[i][j], end=' ')
    print()
