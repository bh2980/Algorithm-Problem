from collections import deque
from copy import deepcopy

def combination(list, count):
    if count == 1:
        return [[i] for i in list]

    combi_list = []

    for i in range(len(list)):
        fix_element = list[i]

        for combi in combination(list[i + 1:], count - 1):
            combi_list.append([fix_element] + combi)

    return combi_list

def solution(n, m, lab):
    # 벽을 3개 세울 수 있다.
    # 바이러스는 상하좌우로 퍼져나간다
    # 바이러스가 있는 칸은 2개 이상 9개 이하이다.

    # 안전영역의 최댓값을 구하여라

    EMPTY = 0
    WALL = 1
    VIRUS = 2

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

    check_dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # 안전 영역을 어떻게 구할까?
    # 벽을 세운 조합별로 BFS를 돌린다.
    for combi in combi_list:
        temp_total_empty = total_empty - 3
        temp_lab = deepcopy(lab)
        temp_virus_list = deepcopy(virus_list)

        for wr, wc in combi:
            temp_lab[wr][wc] = WALL

        # 바이러스의 좌표들을 queue에 넣는다.
        # 좌표 하나를 꺼내와서 상하좌우를 체크한다
        # 체크한 칸 중 EMPTY 칸이 있으면 VIRUS로 바꾸고 큐에 넣는다.
        # WALL이나 VIRUS라면 PASS
        # EMPTY를 VIRUS로 바꿀 때마다 total_empty - 1
        # queue가 빌 때까지 계속한다.

        while len(temp_virus_list) > 0:
            vr, vc = temp_virus_list.popleft()

            for dr, dc in check_dir:
                nr, nc = vr + dr, vc + dc

                # nr, nc가 범위를 벗어나면 pass
                if not 0 <= nr < n or not 0 <= nc < m:
                    continue

                # EMPTY인지 체크
                if temp_lab[nr][nc] == EMPTY:
                    temp_lab[nr][nc] = VIRUS #EMPTY라면, VIRUS로 변경
                    temp_total_empty -= 1 # EMPTY칸 감염 시마다 -1

                    # queue에 새 좌표 추가
                    temp_virus_list.append((nr, nc))

        max_empty = max(max_empty, temp_total_empty)

    return max_empty

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, m, lab))