a = int(input(), 16)

for i in range(0, 15):
        print("%X*%X=%X" % (a, i+1, a*(i+1)))
