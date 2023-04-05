from collections import deque
from copy import deepcopy

EMPTY = 0
WALL = 1
VIRUS = 2

def combination(list, count):
    if count == 1:
        return [[i] for i in list]

    combi_list = []

    for i in range(len(list)):
        fix_element = list[i]

        for combi in combination(list[i + 1:], count - 1):
            combi_list.append([fix_element] + combi)

    return combi_list

# def calcPlusVirusAreaDFS(lab, room):
#     n = len(lab)
#     m = len(lab[0])
#
#     r, c = room
#
#     if not 0 <= r < n or not 0 <= c < m:# 범위 밖이면 return
#         return 0
#
#     if lab[r][c] != EMPTY:# EMPTY가 아니면 return
#         return 0
#
#     # EMPTY라면 VIRUS로 바꾼다.
#     lab[r][c] = VIRUS
#
#     check_dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#
#     changeVirus = 0
#
#     # 상하좌우를 조사 후 상하좌우로부터 virus로 바뀐 칸을 누적한다.
#     for dr, dc in check_dir:
#         nr, nc = r + dr, c + dc
#
#         changeVirus += calcPlusVirusAreaDFS(lab, (nr, nc)) # 상하좌우 중 칸을 호출
#
#     # 바이러스로 바뀐 칸들에 나 자신을 더해 return한다.
#     return changeVirus + 1
#
# def calcSafeAreaDFS(lab, virus_list, total_empty, new_wall):
#     temp_total_empty = total_empty - 3
#     temp_lab = deepcopy(lab)
#
#     for wr, wc in new_wall:
#         temp_lab[wr][wc] = WALL
#
#     check_dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#
#     # 바이러스가 있는 칸의 상하좌우를 조사한다.
#     for vr, vc in virus_list:
#         for dr, dc in check_dir:
#             nr, nc = vr + dr, vc + dc
#
#             temp_total_empty -= calcPlusVirusAreaDFS(temp_lab, (nr, nc))
#
#     return temp_total_empty

def calcPlusVirusAreaDFS(lab, room):
    n = len(lab)
    m = len(lab[0])

    r, c = room

    # 방을 VIRUS로 바꾼다.
    lab[r][c] = VIRUS

    check_dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    changeVirus = 0

    # 상하좌우를 조사 후 상하좌우로부터 virus로 바뀐 칸을 누적한다.
    for dr, dc in check_dir:
        nr, nc = r + dr, c + dc

        if not 0 <= nr < n or not 0 <= nc < m:  # 범위 밖이면 PASS
            continue

        if lab[nr][nc] != EMPTY: # EMPTY가 아니면 PASS
            continue

        # EMPTY인 칸을 넣음
        changeVirus += calcPlusVirusAreaDFS(lab, (nr, nc))

    # 바이러스로 바뀐 칸들에 나 자신을 더해 return한다.
    return changeVirus + 1
def calcSafeAreaDFS(lab, virus_list, total_empty, new_wall):
    temp_total_empty = total_empty - 3 + len(virus_list)
    temp_lab = deepcopy(lab)

    for wr, wc in new_wall:
        temp_lab[wr][wc] = WALL

    # 바이러스가 있는 칸으로부터 조사를 시작한다
    for vr, vc in virus_list:
        temp_total_empty -= calcPlusVirusAreaDFS(temp_lab, (vr, vc))

    return temp_total_empty

def calcSafeAreaBFS(lab, virus_list, total_empty, new_wall):
    temp_total_empty = total_empty - 3
    temp_lab = deepcopy(lab)
    temp_virus_list = deepcopy(virus_list)

    for wr, wc in new_wall:
        temp_lab[wr][wc] = WALL

    # 바이러스의 좌표들을 queue에 넣는다.
    # 좌표 하나를 꺼내와서 상하좌우를 체크한다
    # 체크한 칸 중 EMPTY 칸이 있으면 VIRUS로 바꾸고 큐에 넣는다.
    # WALL이나 VIRUS라면 PASS
    # EMPTY를 VIRUS로 바꿀 때마다 total_empty - 1
    # queue가 빌 때까지 계속한다.

    check_dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while len(temp_virus_list) > 0:
        vr, vc = temp_virus_list.popleft()

        for dr, dc in check_dir:
            nr, nc = vr + dr, vc + dc

            # nr, nc가 범위를 벗어나면 pass
            if not 0 <= nr < n or not 0 <= nc < m:
                continue

            # EMPTY인지 체크
            if temp_lab[nr][nc] == EMPTY:
                temp_lab[nr][nc] = VIRUS  # EMPTY라면, VIRUS로 변경
                temp_total_empty -= 1  # EMPTY칸 감염 시마다 -1

                # queue에 새 좌표 추가
                temp_virus_list.append((nr, nc))

    return temp_total_empty

def solution(n, m, lab):
    virus_list = deque()
    empty_list = list()
    total_empty = 0

    # EMPTY의 모든 좌료를 구해서 성분이 3개인 조합을 만든다.

    for i in range(n):
        for j in range(m):
            if lab[i][j] == EMPTY:
                empty_list.append((i, j))
                total_empty += 1
            elif lab[i][j] == VIRUS:
                virus_list.append((i, j))

    combi_list = combination(empty_list, 3)

    # 각 MAP에 대해서 안전 영역을 구해 최댓값을 구한다.

    max_empty = -1

    # 안전 영역을 어떻게 구할까?
    # 벽을 세운 조합별로 BFS를 돌린다.
    for combi in combi_list:
        max_empty = max(max_empty, calcSafeAreaDFS(lab, virus_list, total_empty, combi))

    return max_empty

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, m, lab))