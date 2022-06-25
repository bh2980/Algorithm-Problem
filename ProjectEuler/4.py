max = -1

# 100부터 1000까지는 다 곱해서 분해하기는 오래 걸린다.
# 거꾸로 내려오면서 palindorme 수를 곱하기로 표현 가능한지 찾는다.

def ispalindorme(number):
    string = str(number)
    s1 = string[:(len(string)//2)]
    tmp = list(string[-(len(string)//2):])
    tmp.reverse()
    s2 = ''
    for i in tmp:
        s2 += i

    return s1 == s2

def checkmultiple(number):
    for i in range(999, 99, -1):
        if number % i == 0 :
            if number // i <= 999:
                print(number, i)
                return True
        
    return False

for i in range(998001, 10000, -1):
    if ispalindorme(i):
        print(i, 'is palindorme')
        if checkmultiple(i):
            max = i
            break

print(max)