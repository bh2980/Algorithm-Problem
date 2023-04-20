def solution(cap, n, deliveries, pickups):
    answer = 0
 	
    # 초기화
    d_dis = []
    d_dict = dict()
    
    p_dis = []
    p_dict = dict()
        
    for distance in range(n):
        if deliveries[distance] != 0:
            d_dis.append(distance + 1)
            d_dict[distance + 1] = deliveries[distance]
        
        if pickups[distance] != 0:
            p_dis.append(distance + 1)
            p_dict[distance + 1] = pickups[distance]
    
    # 이동 거리 계산
    while len(d_dis) > 0 or len(p_dis) > 0:
        far_d_distance = 0
        can_deliver = cap

        while can_deliver > 0 and len(d_dis) > 0: # d_dis의 길이가 0보다 클때만 진행
            farest_distance = d_dis[-1] # 가장 멀리 있는 거리를 불러옴.

            if far_d_distance == 0: # 가장 멀리 이동해야하는 거리 저장
                far_d_distance = farest_distance

            if can_deliver >= d_dict[farest_distance]:
                can_deliver -= d_dict[farest_distance]
                d_dict[farest_distance] = 0

                d_dis.pop()
            else:
                d_dict[farest_distance] -= can_deliver
                can_deliver = 0

        far_p_distance = 0
        can_pickip = cap

        while can_pickip > 0 and len(p_dis) > 0:
            farest_distance = p_dis[-1]

            if far_p_distance == 0:
                far_p_distance = farest_distance

            if can_pickip >= p_dict[farest_distance]:
                can_pickip -= p_dict[farest_distance]
                p_dict[farest_distance] = 0

                p_dis.pop()
            else:
                p_dict[farest_distance] -= can_pickip
                can_pickip = 0

        answer += max(far_d_distance, far_p_distance) * 2

    return answer