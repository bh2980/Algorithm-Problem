from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    cards1, cards2 = deque(cards1), deque(cards2)
    
    for string in goal:
        if len(cards1) > 0 and string == cards1[0]:
            cards1.popleft()
        elif len(cards2) > 0 and string == cards2[0]:
            cards2.popleft()
        else:
            return 'No'
        
    return 'Yes'