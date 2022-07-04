import math
import time

def divisor_list(number):
    a = int(math.sqrt(number))
    list = []

    for i in range(1, a+1):
        if number % i == 0 :
            list.append(i)
            list.append(number//i)

    return list

def isprime(divisor):
    if len(divisor) == 2:
        return True
    return False

number = 1
prime = 0
count = 0

while count != 10001:
    number += 1
    div_list = divisor_list(number)
    if isprime(div_list):
        count += 1
        prime = number
        print(count, number)

print(count, number)
