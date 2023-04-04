def solution(n, m, water_map, order_list):
    direction = dict([[1, (0, -1)],[2, (-1, -1)],[3, (-1, 0)],[4, (-1, 1)],[5, (0, 1)],[6, (1, 1)],[7, (1, 0)],[8, (1, -1)]])

    # 구름의 초기 위치는 (n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)
    cloud_point = set([(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)])

    for d, s in order_list: #100 M
        # 구름 이동
        mr, mc = direction[d]

        move_cloud_point = set()

        for cr, cc in cloud_point: #250 N
            nr = cr + (s % n) * mr
            nc = cc + (s % n) * mc

            if nr < 0:
                nr += n
            elif nr >= n:
                nr -= n

            if nc < 0:
                nc += n
            elif nc >= n:
                nc -= n

            move_cloud_point.add((nr, nc))


        # 구름이 있는 칸 + 1
        for r, c in move_cloud_point: # N
            water_map[r][c] += 1

        # 구름이 있는 칸을 대상으로 물복사 버그
        check_dir = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        for r, c in move_cloud_point: # N
            in_water_count = 0

            for mr, mc in check_dir:
                nr = r + mr
                nc = c + mc

                if 0 <= nr < n and 0 <= nc < n and water_map[nr][nc] > 0:
                    in_water_count += 1

            water_map[r][c] += in_water_count

        # 구름 생성
        temp_cloud_point = set()

        for i in range(n): #N
            for j in range(n): #N
                # 구름이 생기지 않았으면서, 물의 양이 2인 곳에 구름 생성 후 물이 2만큼 줄어즘
                if water_map[i][j] >= 2 and (i, j) not in move_cloud_point:
                    temp_cloud_point.add((i, j))
                    water_map[i][j] -= 2

        cloud_point = temp_cloud_point

    # 구름은 d방향으로 s칸만큼 이동 후 구름이 있는 칸의 물 + 1 => 구름 제거
    # 물이 증가한 칸에 대각선 방향으로 거리가 1인 바구니 중 물이 있는 바구니 수만큼 바구니만큼 물 증가
        # 1, N 경계는 취급 X
    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고 물의 양이 2가 줄어듬.
        # 이 때, 이전에 구름이 사라진 칸은 제외

    return sum([sum(line) for line in water_map])

n, m = map(int, input().split())
water_map = [list(map(int, input().split())) for _ in range(n)]
order_list = [list(map(int, input().split())) for _ in range(m)]

print(solution(n, m, water_map, order_list))