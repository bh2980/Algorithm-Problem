def solution(price, money, count):
    sum = 0
    
    for index in range(1, count + 1):
        sum += price * index
        
    return sum - money if sum > money else 0