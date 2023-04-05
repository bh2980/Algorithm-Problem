CLEANER = -1
EMPTY = 0

EAST = (0, 1)
WEST = (0, -1)
NORTH = (-1, 0)
SOUTH = (1, 0)

def solution(R, C, T, room):
    # 1초 동안
    # 미세먼지가 모든 칸에서 동시에 확산
        # 인접한 네방향으로 그 칸 // 5만큼 확산
        # 확산시킨 칸의 미세먼지는 원래 미세먼지 - (원래 미세먼지 // 5) * 확산한 방 수
        # 공기청정기가 있거나 칸이 없다면 확산 X
    # 공기 청정기 작동
        # 위쪽은 반시계, 아랫쪽은 시계 방향으로 미세먼지가 한 칸 씩 이동
        # 공기 청정기는 1열(0)에 있고 2칸을 차지하며 -1로 표시
        # 위, 아래로 2칸 이상 떨어진 곳에만 위치

    # T초 후 남은 미세먼지의 양

    while T > 0:
        # 전처리
        # 미세먼지 좌표, 공기 청정기 좌표
        dust_location = dict()
        cleaner_location = []

        # N^2
        for i in range(R):
            for j in range(C):
                if room[i][j] == CLEANER:
                    cleaner_location.append((i, j))
                    continue

                if room[i][j] != EMPTY:
                    dust_location[(i, j)] = room[i][j]

        # 미세먼지 확산

        check_dir = [EAST, SOUTH, WEST, NORTH]

        # N
        for location, dust in dust_location.items():
            dust_r, dust_c = location

            spread_dust = dust // 5
            spread_count = 0

            for dr, dc in check_dir:
                check_r, check_c = dust_r + dr, dust_c + dc

                # 범위 벗어나거나 공기청정기가 있다면 PASS
                if not 0 <= check_r < R or not 0 <= check_c < C or (check_r, check_c) in cleaner_location:
                    continue

                spread_count += 1
                room[check_r][check_c] += spread_dust

            room[dust_r][dust_c] -= spread_dust * spread_count

        # 공기청정기 작동

        top_cleaner, bottom_cleaner = cleaner_location

        # top - 반시계 방향으로 이동
        move_counter_clock = [EAST, NORTH, WEST, SOUTH]

        # EAST 첫 칸은 무조건 0
        # SOUTH 마지막 칸은 버린다.

        # 현재 칸과 prev 교체
        # 다음 칸에서 반복
        # 벽에 부딫히면 move idx + 1

        # 공기 청정기 다음 칸부터 시작
        change_r, change_c = top_cleaner[0], top_cleaner[1] + 1
        prev_val = 0
        move_idx = 0

        #N
        while (change_r, change_c) != top_cleaner:
            if (change_r, change_c) in [(0, 0), (0, C - 1), (top_cleaner[0], C - 1)]:
                move_idx += 1

            prev_val, room[change_r][change_c] = room[change_r][change_c], prev_val

            dr, dc = move_counter_clock[move_idx]

            change_r += dr
            change_c += dc

        # bottom - 시계 방향으로 작동

        move_clock = [EAST, SOUTH, WEST, NORTH]

        # 공기 청정기 다음 칸부터 시작
        change_r, change_c = bottom_cleaner[0], bottom_cleaner[1] + 1
        prev_val = 0
        move_idx = 0

        #N
        while (change_r, change_c) != bottom_cleaner:
            if (change_r, change_c) in [(R - 1, C - 1), (R - 1, 0), (bottom_cleaner[0], C - 1)]:
                move_idx += 1

            prev_val, room[change_r][change_c] = room[change_r][change_c], prev_val

            dr, dc = move_clock[move_idx]

            change_r += dr
            change_c += dc

        # 1초 감소
        T -= 1

    total_sum = 0

    # N^2
    for line in room:
        total_sum += sum(line)

    return total_sum + 2


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

print(solution(R, C, T, room))