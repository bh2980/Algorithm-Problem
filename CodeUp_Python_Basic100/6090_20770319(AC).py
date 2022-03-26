a, m, d, n = input().split()
a= int(a)
for i in range(0, int(n)-1):
    a = int(m)*a + int(d)
print(a)
