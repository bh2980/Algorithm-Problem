# 진수 변환

def changeToK(n, k):
    k_string = ''
    
    while n != 0:
        k_string = str(n % k) + k_string
        n //= k
            
    return k_string
        

# 조건 만족
# 그냥 0으로 끊으면 모든 조건에 포함.

def isSatisfy(num_string):
    return [string for string in num_string.split('0') if len(string) > 0]

# 소수 판별

def isPrime(num):
    num = int(num)
    
    if num == 1:
        return False
    
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            return False
    
    return True

def solution(n, k):
    return len([i for i in isSatisfy(changeToK(n, k)) if isPrime(i)])