#자기자신을 제외한 가장 큰 약수
def maxYaksuExceptMe(number):
    if number == 1:
        return 0
    
    for i in range(2, int(number**0.5)+1):
        if number % i == 0 and number // i <= 10000000:
            return number // i

    return 1

def solution(begin, end):
    answer = []
    
    for num in range(begin, end+1):
        answer.append(maxYaksuExceptMe(num))
    
    return answer