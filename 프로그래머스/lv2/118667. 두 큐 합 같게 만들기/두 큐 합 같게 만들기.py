from collections import deque

def solution(queue1, queue2):
    count = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    dequeue1 = deque(queue1)
    dequeue2 = deque(queue2)
    
    while sum1 != sum2 and count < len(queue1) * 4:
        if sum1 > sum2:
            move_element = dequeue1.popleft()
            dequeue2.append(move_element)
            
            sum1 -= move_element
            sum2 += move_element
            
            count += 1
        else:
            move_element = dequeue2.popleft()
            
            dequeue1.append(move_element)
            sum1 += move_element
            sum2 -= move_element
            count += 1
            
    if sum1 != sum2:
        return -1
            
    return count