from collections import defaultdict, deque

def solution(N, road, K):
    answer = 0
    
    # 그래프를 선언
    # BFS로 노드 순회
    # 최솟값 업데이트
    # 방문체크를 하면 안된다
    # 대신 합이 이전 최솟값보다 작은 경우에만 queue에 다시 넣어야한다?
    
    nodeCount = 0
    
    for start, end, weight in road:
        nodeCount = max(nodeCount, start, end)
    
    minDis = [[float('inf') if i != j else 0 for i in range(nodeCount + 1)] for j in range(nodeCount + 1)]
    
    for start, end, weight in road:
        minDis[start][end] = min(weight, minDis[start][end])
        minDis[end][start] = min(weight, minDis[start][end])
    
    for stopover in range(1, nodeCount + 1):
        for start in range(1, nodeCount + 1):
            if start == stopover:
                continue
                
            for end in range(1, nodeCount + 1):
                if start == end or end == stopover:
                    continue
                    
                minDis[start][end] = min(minDis[start][stopover] + minDis[stopover][end], minDis[start][end])
                
    for dis in minDis[1][1:]:
        if dis <= K:
            answer += 1

    return answer