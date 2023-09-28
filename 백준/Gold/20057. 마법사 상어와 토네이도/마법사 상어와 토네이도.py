# n x n 사막, n은 홀수
# x에서 y로 이동
# y와 x 좌표 차이를 구함
# y를 기준으로

# 격자 밖으로 나간 모래의 양

from copy import deepcopy

def printMap(sand):
    new_sand = deepcopy(sand)

    for line in new_sand:
        for char in line:
            print(char, end=' ')
        print()

    print()

def moveSand(prev_pos, current_pos, sand):
    N = len(sand)

    ci, cj = current_pos
    pi, pj = prev_pos
    di, dj = ci - pi, cj - pj

    ALPHA = 'ALPHA'

    diff = [((ci + di * 2, cj + dj * 2), 5), ((ci + dj, cj + di), 7), ((ci - dj, cj - di), 7), ((ci + dj * 2, cj + di * 2), 2), ((ci - dj * 2, cj - di * 2), 2), ((pi + dj, pj + di), 1), ((pi - dj, pj - di), 1), ((ci + di + dj, cj + dj + di), 10), ((ci + di - dj, cj + dj - di), 10), ((ci + di, cj + dj), ALPHA)]

    total_sand = sand[ci][cj]
    move_sand = 0
    out_sand = 0

    for pos, percent in diff:
        ni, nj = pos

        if percent != ALPHA:
            new_sand = total_sand * percent // 100

            if 0 <= ni < N and 0 <= nj < N:
                sand[ni][nj] += new_sand
                move_sand += new_sand
            else:
                move_sand += new_sand
                out_sand += new_sand
        else:
            if 0 <= ni < N and 0 <= nj < N:
                sand[ni][nj] += total_sand - move_sand
            else:
                out_sand += total_sand - move_sand

    sand[ci][cj] = 0

    return out_sand

def solution(n, sand):
    oi, oj = n // 2, n // 2

    # center를 기준으로 회오리 모양으로 순회

    # left, down, right, up
    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]

    idx = 0

    ci, cj = oi, oj

    out_sand = 0

    for length in range(1, n+1):
        for _ in range(2):
            dci, dcj = di[idx], dj[idx]

            for _ in range(length):
                pi, pj = ci, cj
                ci, cj = ci + dci, cj + dcj

                out_sand += moveSand((pi, pj), (ci, cj), sand)

                # printMap(sand)

                if (ci, cj) == (0, 0):
                    break

            if (ci, cj) == (0, 0):
                break

            idx = (idx + 1) % 4

        if (ci, cj) == (0, 0):
            break

    return out_sand

n = int(input())
sand = [list(map(int, input().split())) for _ in range(n)]

answer = solution(n, sand)

print(answer)
