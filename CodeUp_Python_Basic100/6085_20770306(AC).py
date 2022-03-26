s = input().split()
gop = 1
for i in s:gop *= int(i)
print("%.2f MB" % (gop/8/1024/1024))
