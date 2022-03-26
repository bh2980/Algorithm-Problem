i = input().split()
gop = 1
for s in i:
    gop *= int(s)
print("%.1f MB" % (gop/8/1024/1024))
