# 최소 신장 트리
# 크루스칼
# 가중치 순으로 간선을 정렬한다
# 사이클이 생기지 않는지 확인하면서 추가한다.  
    # 사이클 확인 
    # 0-3을 추가한다고 가정
    # 0 - x - 3이 있는지 확인
    # 포함시킨 간선 중에 0과 이어진 간선을 확인
    # 각 간선의 도착지 노드가 3과 이어져있는지 확인
    
# 결국 각 노드가 어느 root에 속하는지 알아내는 작업이다.

def union(unionFindSet, node1, node2):
    x = find(unionFindSet, node1)
    y = find(unionFindSet, node2)
    
    if x == y: 
        return
    
    unionFindSet[y] = x
    
def find(unionFindSet, node):
    # 어느 root에 속하는지 찾는다.
    if unionFindSet[node] == node:
        return node
    
    return find(unionFindSet, unionFindSet[node])

def solution(n, costs):
    answer = 0
    
    costs = sorted(costs, key=lambda x:(x[2], x[0], x[1]))
    
    nodeCount = 0
    
    unionFindSet = [idx for idx in range(101)]
    
    for node1, node2, cost in costs:
        if find(unionFindSet, node1) != find(unionFindSet, node2):
            union(unionFindSet, node1, node2)
            answer += cost
    
    return answer