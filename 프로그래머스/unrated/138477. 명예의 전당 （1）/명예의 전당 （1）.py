from heapq import heappop, heappush, nsmallest

def solution(k, score):
    answer = []
    
    heap = []
    
    for s in score:
        heappush(heap, -s)
        
        answer.append(-nsmallest(k, heap)[-1])
    return answer