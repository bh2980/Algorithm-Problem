sum = 0
a = 1
b = 2

sum = 2

while True:
    a = a + b

    if a > 4000000:
        break

    if a % 2 == 0:
        sum += a

    b = a + b

    if b % 2 == 0:
        sum += b
    
    if b > 4000000:
        break

print(sum)

