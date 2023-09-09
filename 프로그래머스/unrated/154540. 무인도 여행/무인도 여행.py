from collections import deque

SEA = 'X'

def BFS(maps, start_p):
    _sum = 0
    
    row_length = len(maps)
    col_length = len(maps[0])
    
    queue = deque([start_p])
    
    s_x, s_y = start_p
    maps[s_x][s_y] *= -1
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    while(len(queue) > 0):
        land = queue.popleft()
        l_x, l_y = land
        
        _sum += -maps[l_x][l_y]
        
        for i in range(4):
            n_x, n_y = l_x + dx[i], l_y + dy[i]
            
            if 0 <= n_x < row_length and 0 <= n_y < col_length and (n_x, n_y):
                if maps[n_x][n_y] != SEA and maps[n_x][n_y] > 0:
                    maps[n_x][n_y] *= -1
                    queue.append((n_x, n_y))

    return _sum

def solution(maps):
    answer = []
    
    row_length = len(maps)
    col_length = len(maps[0])
    
    for i in range(len(maps)):
        maps[i] = list(map(lambda x : SEA if x == SEA else int(x), list(maps[i])))
    
    for i in range(row_length):
        for j in range(col_length):
            if maps[i][j] != SEA and maps[i][j] > 0:
                answer.append(BFS(maps, (i, j)))
    
    # for문을 돌리다가 바다가 아닌 섬을 찾으면 BFS 시작(큐에 추가)
    # 꺼내서 합하고, 상하좌우를 돌면서 바다가 아닌 곳이 있으면 큐에 추가
    # 큐에 길이가 들어있지 않을때까지 반복
    # 합한 값 return -> 받아서 answer에 추가
    # sort 후 answer return
    return sorted(answer) if len(answer) > 0 else [-1]