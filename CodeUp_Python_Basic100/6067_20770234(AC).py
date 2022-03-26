a = input()
a= int(a)

# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)

if a<0:
    if(a%2 == 0):
        print("A")
    else:
        print("B")
else:
    if(a%2 == 0):
        print("C")
    else:
        print("D")
