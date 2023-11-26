# BFS
# DFS
# 플로이드 워셜
# 다익스트라

from collections import defaultdict, deque

def solution(N, road, K):
    answer = 0
    
    # 그래프를 선언
    # BFS로 노드 순회
    # 최솟값 업데이트
    # 방문체크를 하면 안된다
    # 대신 합이 이전 최솟값보다 작은 경우에만 queue에 다시 넣어야한다?
    
    graph = defaultdict(lambda: set())
    nodeCount = 0
    
    for start, end, weight in road:
        nodeCount = max(start, end, nodeCount)
        graph[start].add((end, weight))
        graph[end].add((start, weight)) # 양방향 그래프
        
    minDis = [float('inf') for _ in range(nodeCount + 1)]
    
    queue = deque([(1, 0)])
    
    while len(queue) > 0:
        currentNode, distance = queue.popleft()
        
        if distance < minDis[currentNode]:
            minDis[currentNode] = distance
            
        for child, weight in graph[currentNode]:
            if weight + distance < minDis[child]:
                queue.append((child, weight + distance))
                
    for dis in minDis:
        if(dis <= K):
            answer += 1

    return answer