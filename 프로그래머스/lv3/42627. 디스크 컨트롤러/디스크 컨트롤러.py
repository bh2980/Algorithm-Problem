from heapq import heappop, heappush, heapify
from collections import deque

def solution(jobs):
    JC = len(jobs)
    time = 0 # 누적 시간
    total_ask_end_time = 0 # 총 요청-처리 시간
    
    jobs = deque(sorted(jobs))
    heap = []

    # 힙 초기화
    ask_time, processing_time = jobs.popleft()
    heappush(heap, (processing_time, ask_time))
    
    # 0초에 시작하지 않을 수도 있으므로
    time += ask_time
    
    # 디스크 컨트롤러가 작업을 마치는 시간을 구한다.
        # 종료 시간은 작업 시작 시간 + 작업 진행 시간
    # 디스크 컨트롤러가 작업을 마칠 때까지, 도착한 작업을 jobs에서 빼 heap에 넣는다.
        # heap의 우선 순위는 작업 시간
    # 디스크 컨트롤러가 작업을 마치면 heap에서 꺼내 작업을 부여한다.
    # 반복
    
    while len(heap) > 0:
        cur_processing_time, cur_ask_time = heappop(heap)
        
        print(f'{cur_ask_time}초 요청 작업, {time}초 시작')
        time += cur_processing_time
        print(f'{cur_processing_time}초 걸림, {time}초 종료')
        
        # end_time보다 전에 들어온 작업을 heap에 넣음.
        while len(jobs) > 0 and jobs[0][0] <= time:
            next_ask_time, next_processing_time = jobs.popleft()
            heappush(heap, (next_processing_time, next_ask_time))
        
        # 요청-처리 시간 누적
        total_ask_end_time += (time - cur_ask_time)
        print(f'{cur_ask_time}초 요청, {time}초 완료, 누적 {total_ask_end_time}초')
        print()
        
        # 현재 시간까지 도착한 작업이 없다면, 작업이 도착할 때까지 대기 후 새 작업 부여
        if len(jobs) > 0 and len(heap) == 0:
            next_ask_time, next_processing_time = jobs.popleft()
            heappush(heap, (next_processing_time, next_ask_time))
            time = next_ask_time
        
    # 모든 작업이 끝나면, answer를 JC로 // 나눔.
    
    return total_ask_end_time // JC