def solution(n, results):
    answer = 0
    INF = float('inf')
    # 모든 노드에 대해 각 노드가 다른 모든 노드를 방문 가능한가? -> 플로이드 워셜
    
    ad_matrix = [[INF for _ in range(n)] for _ in range(n)]
    
    # 그래프 초기화
    for winner, loser in results:
        ad_matrix[winner - 1][loser - 1] = 1
    
    for k in range(n): # 경유지 선정
        for i in range(n):
            if i == k:
                continue
                
            for j in range(n):
                if i == j or j == k:
                    continue
                    
                ad_matrix[i][j] = min(ad_matrix[i][j], ad_matrix[i][k] + ad_matrix[k][j])
                
    # 이긴사람 + 진사람 == n - 1
    
    row_count = [sum([1 if line[i] != INF else 0 for i in range(n)]) for line in ad_matrix]
    col_count = [sum([1 if line[i] != INF else 0 for i in range(n)]) for line in zip(*ad_matrix)]
    
    for i in range(n):
        if row_count[i] + col_count[i] == n - 1:
            answer += 1
                
    return answer