def countYaksu(number):
    count = 0
    
    if number == 1:
        return 1
    
    for divider in range(1, int(number**0.5) + 1):
        if number**0.5 == divider and number % divider == 0:
            count += 1
        elif number % divider == 0:
            count += 2
        
    return count

def solution(number, limit, power):
    answer = 0
    
    for eachPower in range(1, number + 1):
        needSteal = countYaksu(eachPower)
        
        answer += needSteal if needSteal <= limit else power
        
    return answer