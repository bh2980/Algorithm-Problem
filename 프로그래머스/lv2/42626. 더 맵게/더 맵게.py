from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0
    heap = []
    
    for s in scoville:
        heappush(heap, s)
        
    while True:
        first_s = heappop(heap)
        
        if first_s >= K:
            break
        
        try:
            second_s = heappop(heap)
        except:
            return -1
        
        new_s = first_s + 2 * second_s
        answer += 1
        
        heappush(heap, new_s)
        
    return answer