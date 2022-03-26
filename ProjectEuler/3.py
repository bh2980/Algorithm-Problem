import math

def divisor_list(number):
    a = int(math.sqrt(number))
    list = []

    for i in range(1, a+1):
        if number % i == 0 :
            list.append(i)
            list.append(number//i)

    return list

div_list = []

result_600851475143 = divisor_list(600851475143)

for i in result_600851475143:
    result_i = divisor_list(i)
    if len(result_i) == 2:
        div_list.append(i)

print(max(div_list))