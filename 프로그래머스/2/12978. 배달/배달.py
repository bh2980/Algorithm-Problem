from heapq import heappush, heappop
from collections import defaultdict

def solution(N, road, K):
    answer = 0
    INF = float('inf')

    # 1번 마을에서 다른 모든 마을까지의 최소 거리를 알아야함.
    # 다익스트라
    # 그래프 초기화 -> 인접 리스트 dict
    graph = defaultdict(lambda: [])
    
    for start, end, weight in road:
        graph[start].append((end, weight))
        graph[end].append((start, weight))
    
    # (node, weight)
    # 최소 거리 배열을 만들어서 업데이트
    
    minDis = [INF for _ in range(N + 1)]
    minDis[1] = 0
    
    # heap에 현재 그래프로부터 다른 노드까지의 최소 거리를 뽑는다.
    
    heap = []
    visitedSet = set()
    
    heappush(heap, (0, 1))
    
    while len(heap) > 0:
        dis, node = heappop(heap)
            
        # 방문한 노드라면 pass
        # 방문하지 않은 노드라면 최소 거리 배열에 값을 업데이트한다
        # 해당 노드로부터 방문하지 않은 노드로 이어지는 값을 해당 노드까지의 거리를 더해 추가한다.
        
        if minDis[node] < dis:
            continue
        
        for end, weight in graph[node]:
            if dis + weight < minDis[end]:
                minDis[end] = min(minDis[end], dis + weight)
                heappush(heap, (minDis[end], end))
                
    for idx in range(len(minDis)):
        if minDis[idx] <= K:
            answer += 1

    return answer