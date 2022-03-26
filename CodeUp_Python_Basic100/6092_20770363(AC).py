a = int(input())
num = [0 for i in range(23)]
s = input().split()
for i in s:
    num[int(i)-1] += 1

for i in num:
    print(i, end=' ')
