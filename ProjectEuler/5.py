# 최소 공배수
import math
from collections import Counter

UNTIL = 20

prime_n_list = []
divisor = []

def divisor_list(number):
    a = int(math.sqrt(number))
    list = []

    for i in range(1, a+1):
        if number % i == 0 :
            list.append(i)
            list.append(number//i)

    return list

for i in range(1, UNTIL+1):
    divisor = divisor_list(i)
    if len(divisor) == 2:
        prime_n_list.append(i)

prime_n_list.remove(1)
print(prime_n_list)

# 1이 될 때 까지 소수 목록을 2부터 차례대로 올라가면서 나누어 떨어지는 것 divisor에 추가
# 추가한 list를 전체 list에 추가

total = []
divisor = []

for i in range(1, UNTIL+1):
    number = i
    print(number)

    while number != 1:
        for j in prime_n_list:
            if number % j == 0:
                number //= j
                divisor.append(j)
                break

    print(divisor)
    total.append(divisor)
    divisor = []

for i in total:
    if len(i) % 2 == 1:
        i.insert(0, 1)

total[0].append(1)

print(total)

fin_list = [0] * 20

for i in total:
    counter = Counter(i)
    for j in prime_n_list:
        if counter[j] > fin_list[j] :
            fin_list[j] = counter[j]

print(fin_list)

answer = 1

for i in range(0,UNTIL):
    if fin_list[i] != 0:
        answer *= pow(i, fin_list[i])

print(answer)