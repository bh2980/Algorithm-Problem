n = int(input())
i = 1
count = 1

while True:
    n = n - i
    if n == 0 or n < 0 :
        break
    i = 6 * count
    count = count + 1
    
print(count)