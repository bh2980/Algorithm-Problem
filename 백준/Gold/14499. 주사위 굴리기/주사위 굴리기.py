def rollDice(dice_state, order):
    # 동으로 구르면
    # NS 유지, U -> E, E -> D, D -> W, W -> U
    # 서로 구르면
    # NS 유지, E -> U, D -> E, W -> D, U -> W
    # 북으로 구르면
    # EW 유지, S -> U, U -> N, N -> D, D -> S
    # 남으로 구르면
    # EW 유지, U -> S, S -> D, D -> N, N -> U,

    EAST = 1
    WEST = 2
    NORTH = 3
    SOUTH = 4

    if order == EAST:
        dice_state['U'], dice_state['E'], dice_state['D'], dice_state['W'] =  \
            dice_state['E'], dice_state['D'], dice_state['W'], dice_state['U']
    elif order == WEST:
        dice_state['E'], dice_state['D'], dice_state['W'], dice_state['U'] = \
            dice_state['U'], dice_state['E'], dice_state['D'], dice_state['W']
    elif order == NORTH:
        dice_state['S'], dice_state['U'], dice_state['N'], dice_state['D'] = \
            dice_state['U'], dice_state['N'], dice_state['D'], dice_state['S']
    elif order == SOUTH:
        dice_state['U'], dice_state['N'], dice_state['D'], dice_state['S'] = \
            dice_state['S'], dice_state['U'], dice_state['N'], dice_state['D']

def solution(map_size, dice_origin, k, _map, order_list):
    # 주사위의 모든 면에는 0이 쓰여있는채로 dice_origin에 놓여있다.
    # 칸에 0이 있으면, 주사위의 바닥면의 수가 칸에 복사
    # 칸이 0이 아니면, 바닥에 있는 수가 주사위의 바닥면에 복사되고 칸의 수는 0
    # 지도를 넘어가는 명령은 무시

    # 이동할 때마다 주사위 상단에 있는 수를 출력

    direction = dict([[1, (0, 1)] ,[2, (0, -1)], [3, (-1, 0)], [4, (1, 0)]]) #동서북남
    # 방향대로 1칸씩 움직이는 듯

    # 주사위 굴리는 알고리즘
    # 주사위는 1~6을 key로 0을 값으로 가진다.
    dice = dict([[i, 0] for i in range(1, 7)])
    # 주사위의 면과 실제 주사위의 상태 매칭
    # 위, 아래, 북, 동, 서, 남
    dice_state = dict([['U', 1], ['D', 6], ['N', 2], ['S', 5], ['E', 3], ['W', 4]])

    cr, cc = dice_origin

    for order in order_list:
        dr, dc = direction[order]

        nr = cr + dr
        nc = cc + dc

        if not 0 <= nr < n or not 0 <= nc < m: #벗어나는 명령이면 pass
            continue

        # 위치 업데이트
        cr, cc = nr, nc

        # 주사위 굴리기
        rollDice(dice_state, order)

        # 지도, 주사위 숫자 업데이트
        if _map[cr][cc] == 0:# 칸에 0이 있으면, 주사위의 바닥면의 수가 칸에 복사
            _map[cr][cc] = dice[dice_state['D']]
        else:# 칸이 0이 아니면, 바닥에 있는 수가 주사위의 바닥면에 복사되고 칸의 수는 0
            dice[dice_state['D']] = _map[cr][cc]
            _map[cr][cc] = 0

        print(dice[dice_state['U']])

    return

n, m, r, c, k = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(n)]
order_list = list(map(int, input().split()))

solution((n, m), (r, c), k, _map, order_list)