from collections import deque

def solution(n, m, section):
    answer = 0
    
    section = deque(section)
    startTile = -1
    
    while len(section) > 0:
        if startTile > 0 and section[0] < startTile + m:
            section.popleft()
        else:
            startTile = section[0]
            section.popleft()
            answer += 1
        
    return answer