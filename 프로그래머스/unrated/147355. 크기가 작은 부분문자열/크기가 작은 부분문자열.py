def solution(t, p):
    answer = 0
    
    numLength = len(p)
    targetNumber = int(p)
    
    for i in range(0, len(t) - numLength + 1):
        sliceNumber = int(t[i:i+numLength])
        
        if targetNumber >= sliceNumber:
            answer += 1
            
    return answer