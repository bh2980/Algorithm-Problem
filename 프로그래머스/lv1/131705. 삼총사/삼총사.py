def combinations(_list, n):
    combi = []
    
    if n == 1:
        return [[num] for num in _list]
    
    #n을 제외하고 n-1개를 뽑는 경우의 수
    for idx in range(0, len(_list)):
        exceptElement = _list[idx]
        exceptList = _list[idx+1:]
        
        for subCombi in combinations(exceptList, n-1):
            combi.append([exceptElement] + subCombi)
            
    return combi
        

def solution(number):
    answer = 0
    
    for subCombi in combinations(number, 3):
        if sum(subCombi) == 0:
            answer += 1
    
    return answer