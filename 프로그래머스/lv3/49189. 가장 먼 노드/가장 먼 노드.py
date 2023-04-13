from heapq import heappush, heappop
from collections import Counter, defaultdict

def solution(n, edge):
    INF = float('inf')
    
    answer = 0
    # 1번 노드에서 가장 멀리 떨어진 노드 -> 다익스트라
    # BFS도 가능
    
    ad_list = defaultdict(lambda : [])
    
    # 그래프 초기화
    for v1, v2 in edge:
        ad_list[v1 - 1].append(v2 - 1)
        ad_list[v2 - 1].append(v1 - 1)
        
    # 다익스트라
    # 최소 거리를 갱신하는 것
    min_dis = [INF for _ in range(n)]
    heap = []
    visited_set = set()
    
    # 다익 초기화
    min_dis[0] = 0
    heappush(heap, (0, 0))
    
    while len(heap) > 0:
        current_dis, current_node_idx = heappop(heap)
        
        # 방문했다면 패스
        if current_node_idx in visited_set:
            continue
            
        visited_set.add(current_node_idx)
        
        # 인접 노드 최소 거리 갱신
        for near_node in ad_list[current_node_idx]:
            if near_node in visited_set:
                continue
            
            min_dis[near_node] = min(min_dis[near_node], current_dis + 1)
            
            # 힙에 넣자.
            heappush(heap, (min_dis[near_node], near_node))

    return Counter(min_dis)[max(min_dis)]