def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # i번째 집은 i만큼 떨어져있고 모든 집은 1자로 되어있음
    # 트럭에는 cap개 싣을 수 있다.
    # 모든 집에 배달/수거해야하는 택배 개수를 알고 있다.
    
    # 최소 이동 거리
    
    # 가장 멀리부터 제거해나가는게 맞다.
    # 택배는 가장 멀리 있는 것부터 배달한다
    # 수거도 가장 멀리 있는 것부터 수거한다.
    # 택배를 최대한 많이 싣고, 수거도 최대한 많이 실어야한다.
    # 택배를 모두 싣는다고 좋은게 아님, 남을 경우에 수거 자리가 애매.
        # 남아 있는 개수를 카운트해서 편도로 이동 시 다 비울 수 있을 만큼만 싣자.
    # 수거는 무조건 최대한 많이 싣는게 좋음.
    
    # 어떻게 리스트를 업데이트할까?
    # dict으로 해야함
    
    # d_dis의 길이를 확인하고 0보다 크다면 이하 과정을 진행
    # d_dis의 마지막 성분을 본다(-1) -> 택배 이동거리
    # 할 수 있는 만큼 제거한다
    # 만약 성분이 0이 됐다면, d_dis에서 pop한다.
    # 반복
    
    # p_dis의 길이를 확인하고 0보다 크다면 이하 과정을 진행
    # p_dis의 마지막 성분을 본다 (-1) -> 수거 이동거리
    # 할수 있는 만큼 제거한다
    # 만약 성분이 0이 됐다면, p_dis에서 pop한다.
    # 반복
    
    # 택배 이동거리와 수거 이동거리 중 큰 쪽을 *2해서 answer에 누적한다.
    
    # 위 과정을 d_dis와 p_dis가 빌 때까지 반복한다.
        
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
    
    while len(d_dis) > 0 or len(p_dis) > 0:
        far_d_distance = 0
        can_deliver = cap

        while can_deliver > 0 and len(d_dis) > 0: # d_dis의 길이가 0보다 클때만 진행
            farest_distance = d_dis[-1] # 가장 멀리 있는 거리를 불러옴.
            # print(f'배달 대상 : {farest_distance}')

            if far_d_distance == 0: # 가장 멀리 이동해야하는 거리 저장
                far_d_distance = farest_distance

            # 가장 멀리 있는 택배 개수를 확인해서 줄일 수 있는 만큼 줄임.
            # can_deliver >= d_dict[farest_distance]: d_dict[farest_distance] = 0
            # can_deliver < d_dict[farest_distance] : d_dict[farest_distance] - can_deliver

            # print(f'배달 가능 횟수 : {can_deliver}')

            if can_deliver >= d_dict[farest_distance]:
                # print(f'{d_dict[farest_distance]}개 배달, 0개 남음')
                can_deliver -= d_dict[farest_distance]
                d_dict[farest_distance] = 0

                d_dis.pop()
            else:
                # print(f'{d_dict[farest_distance]}개 배달, {d_dict[farest_distance] - can_deliver}개 남음')
                d_dict[farest_distance] -= can_deliver
                can_deliver = 0


#             print(f'남은 배달 가능 횟수 {can_deliver}\n')

#         print('최대 배달 이동 거리 :', far_d_distance)

#         print()

        far_p_distance = 0
        can_pickip = cap

        while can_pickip > 0 and len(p_dis) > 0: # p_dis의 길이가 0보다 클때만 진행
            farest_distance = p_dis[-1] # 가장 멀리 있는 거리를 불러옴.
            # print(f'픽업 대상 : {farest_distance}')

            if far_p_distance == 0: # 가장 멀리 이동해야하는 거리 저장
                far_p_distance = farest_distance

            # 가장 멀리 있는 택배 개수를 확인해서 줄일 수 있는 만큼 줄임.
            # can_deliver >= d_dict[farest_distance]: d_dict[farest_distance] = 0
            # can_deliver < d_dict[farest_distance] : d_dict[farest_distance] - can_deliver

            # print(f'픽업 가능 횟수 : {can_pickip}')

            if can_pickip >= p_dict[farest_distance]:
                # print(f'{p_dict[farest_distance]}개 픽업, 0개 남음')
                can_pickip -= p_dict[farest_distance]
                p_dict[farest_distance] = 0

                p_dis.pop()
            else:
                # print(f'{p_dict[farest_distance]}개 픽업, {p_dict[farest_distance] - can_pickip}개 남음')
                p_dict[farest_distance] -= can_pickip
                can_pickip = 0


#             print(f'남은 픽업 가능 횟수 {can_pickip}\n')

#         print('최대 픽업 이동 거리 :', far_p_distance)

        answer += max(far_d_distance, far_p_distance) * 2
        # print()
        # print('현재 이동 거리 :', answer)
        # print()
    
    
    
    return answer