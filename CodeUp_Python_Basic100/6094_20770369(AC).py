a = input().split()
a = input().split()
min = int(a[0])
for i in a:
    min = int(i) if(min>int(i)) else min
print(min)
