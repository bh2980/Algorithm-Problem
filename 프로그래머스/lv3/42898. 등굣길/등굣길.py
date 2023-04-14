INF = float('inf')

def solution(m, n, puddles):
    # 오른쪽과 아래쪽으로만 움직이니까 모든 경로가 최단 경로
    # 즉, 최단 경로가 중요한게 아니라 그 타일까지 올 수 있는 경우의 수를 계산하는 것
    
    # 최단 경로의 개수 % 1000000007
    
    # D[i][j] = D[i-1][j] + D[i][j-1]
    D = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    D[1][1] = 1
    
    puddles = set([tuple((p_r, p_c)) for p_c, p_r in puddles])
    
    #(1, 1) 제외, puddles 제외 하고 좌, 상 더해서 업데이트
    
    for i in range(1, n+1):
        for j in range(1, m + 1):
            if (i, j) == (1, 1) or (i, j) in puddles:
                continue
            
            D[i][j] = D[i-1][j] + D[i][j-1]
    
    for line in D:
        print(line)
        
    return D[n][m] % 1000000007