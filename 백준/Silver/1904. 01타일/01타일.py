n = int(input())
pre = 1
prepre = 1

for i in range(2, n+1):
  prepre, pre = pre, (pre+prepre) % 15746

print(pre)