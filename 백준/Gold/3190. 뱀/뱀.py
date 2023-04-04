def solution(n, k, apple_list, rotation_list):
    # n x n의 판 위에서 뱀은 (0, 0)에서 오른쪽을 향해 시작
    # 보드의 상하좌우 끝에 벽이 존재 -> 보드 밖에 벽이 존재
    # 매 1초마다 뱀은 향하는 방향으로 몸을 늘림
        # 몸을 늘린 방향에 사과가 있으면 꼬리 유지
        # 몸을 늘린 방향에 사과가 없다면 몸을 당김
    # x초가 끝난 뒤에 왼쪽 L또는 오른쪽 D 방향으로 90도 회전
    # 자기 몸에 닿거나 벽에 닿으면 게임 오버

    LEFT = 'L'
    RIGHT = 'D'

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오 하 좌 상 -> 시계 방향
    # D라면 idx + 1
    # L이라면 idx - 1

    dir_idx = 0
    head = (0, 0)
    snake = dict([[ head , 0 ]])

    time = 0

    while True:
        # 1초 시작
        time += 1

        # 머리를 뻗음
        cr, cc = head
        nr = cr + direction[dir_idx][0]
        nc = cc + direction[dir_idx][1]

        # 벽에 부딪히거나 머리가 몸체와 부딫혔을 때 return time
        if not 0 <= nr < n or not 0 <= nc < n or (nr, nc) in snake:
            return time

        snake[(nr, nc)] = time

        #사과가 있다면 사과 제거
        if (nr, nc) in apple_list:
            apple_list.remove((nr, nc))
        else: # 사과가 없다면 snake에서 꼬리 위치 제거
            tail = list(snake.keys())[0]
            snake.pop(tail)

        head = (nr, nc)

        # x초가 끝나면 따라 방향 전환
        if time in rotation_list:
            if rotation_list[time] == LEFT:
                dir_idx = dir_idx - 1 if dir_idx - 1 >= 0 else 3
            else:  # RIGHT
                dir_idx = dir_idx + 1 if dir_idx + 1 < 4 else 0

    return 0

n = int(input())
k = int(input())

apple_list = set([tuple(map(lambda x : int(x) - 1, input().split())) for _ in range(k)])

r = int(input())
rotation_list = dict()

for _ in range(r) :
    x, c = input().split()
    rotation_list[int(x)] = c

print(solution(n, k, apple_list, rotation_list))