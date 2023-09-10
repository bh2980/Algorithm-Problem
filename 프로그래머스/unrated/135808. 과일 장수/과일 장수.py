def solution(k, m, score):
    answer = 0
    
    if len(score) < m:
        return 0
    
    score.sort(reverse = True)
    
    startIdx = 0
    
    return sum(score[m - 1::m]) * m