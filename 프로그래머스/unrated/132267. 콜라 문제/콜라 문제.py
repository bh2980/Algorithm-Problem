def solution(a, b, n):
    answer = 0
    
    # while 문으로 a개 미만일 때까지 반복합니다.
    # plusCola + extraCola개의 콜라를 n개로 나눈 몫을 answer에 더하고, plusCola에 넣습니다.
        # 나머지가 생길 경우 extraCola에 넣습니다.
        
    plusCola = n
    extraCola = 0
    
    while plusCola >= b:
        mok, rest = divmod(plusCola + extraCola, a)
        
        makeCola = mok * b
        
        answer += makeCola
        plusCola = makeCola
        extraCola = rest
        
    return answer