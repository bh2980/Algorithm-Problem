def nNumber(n, number):
    num_string = ''
    
    if number == 0:
        return '0'
    
    while number != 0:
        mok, rest = divmod(number, n)

        number = mok
        
        if rest == 10:
            rest = 'A'
        elif rest == 11:
            rest = 'B'
        elif rest == 12:
            rest = 'C'
        elif rest == 13:
            rest = 'D'
        elif rest == 14:
            rest = 'E'
        elif rest == 15:
            rest = 'F'
            
        num_string = str(rest) + num_string
        
    return num_string

def solution(n, t, m, p):
    #특정 진법의 t개의 수를 string으로 잇습니다.
    #다 이은 수에서 p번째부터 m개마다 t개를 가져옵니다.
    #2진법부터 16진법까지 모두 구현해야하는거야?
    
    number_string = ''
    
    num = 0
    
    while len(number_string) <= t * m + p:
        number_string += nNumber(n, num)
        num += 1
    
    return number_string[p-1:t*m:m]