def solution(scoville, K):
    from collections import deque
    INF = 9223372036854775807

    count = 0
    
    scoville = deque(sorted(scoville)) #원래 scoville
    mix = deque() #새로운 값
        
    while True:
        min_val = INF
        
        if len(mix) == 0:
            #mix가 비었다면 scoville의 왼쪽 값을 min값으로 설정
            min_val = scoville[0]
            
            if min_val < K:
                min_val = scoville.popleft()
                try:
                    second_val = scoville.popleft()
                except: #하나 밖에 없는 원소가 K보다 작다면
                    return -1
                
                new_val = min_val + second_val * 2
                mix.append(new_val)
                count += 1
            else:
                return count
        else:
            #mix가 비지 않았다면 두 queue 중 최솟값을 설정
            if scoville[0] <= mix[0]:
                min_val = scoville.popleft()
            else:
                min_val = mix.popleft()
            
            if min_val < K:
                #scoville이나 mix가 비었을 수도 있음
                temp1 = INF
                temp2 = INF

                if len(scoville) > 0:
                    temp1 = scoville[0]
                    
                if len(mix) > 0:
                    temp2 = mix[0]
                    
                if temp1 == INF and temp2 == INF:
                    #둘 다 비었으면 하나 밖에 없는 원소 < K이므로 return -1
                    return -1
                
                second_val = scoville.popleft() if temp1 <= temp2 else mix.popleft()
                
                new_val = min_val + second_val * 2
                mix.append(new_val)
                count += 1
            else:
                return count
        
        #scoville이 비었다면 mix의 모든 원소를 scoville로 옮김
        if len(scoville) == 0:
            while len(mix) > 0:
                scoville.append(mix.popleft())