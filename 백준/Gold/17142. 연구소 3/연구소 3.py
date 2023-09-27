# 연구소는 N x N, M개의 바이러스를 활성 상태로
# 바이러스는 상하좌우로 퍼져나가며, 비활성 상태 바이러스를 만날 경우 활성 상태로 바꿈

# 바이러스가 다 퍼지는 최소 시간

# 모두 다 해봐야함.
# BFS를 사용하는 것 같음.
# 계층 별 초를 계산해야함.
# 계속 최소 시간을 업데이트하면서 최소 시간보다 더 걸릴 경우 끊어내는 전략으로 최적화

# 0 빈 칸
# 1 벽
# 2 비활성 바이러스

# 비활성 바이러스의 좌표를 모두 구한다.
# 바이러스 m개의 조합을 만든다.
# m개의 조합을 활성 상태로 한 상태로 바이러스 확산을 시뮬레이션한다.

# 시뮬레이션
# 바꾼 즉시는 0초
# 상하좌우 칸을 조사하여 빈 칸이면 바이러스를 복제하고 queue에 넣는다.
    # 바이러스가 있다면 활성 상태로 바꾸고 queue에 넣는다.
    # 벽이라면 PASS한다.
# queue의 각 층이 끝날 때마다 +1초를 한다.
    # 만약 time이 min_time보다 크다면 즉시 중지하고 return한다.
# queue가 빈 칸이 되었을 때 time을 return한다.

# time을 받아서 최솟값으로 업데이트한다.
# 조합에 대해 반복한다.

# 불가능한 경우 -1
# virus를 1개씩 만들 때마다 count + 1
# queue가 0라서 time을 return하는데 벽을 제외한 count와 virus count가 다를 경우 -1

from collections import deque
from copy import deepcopy

def combinations(_list, n):
    # n개에서 c개를 뽑는 조합은
    # n개에서 첫 번째 원소를 제외하고 c-1개를 뽑은 다음 첫 번째 원소를 넣는 거 + n개에서 첫 번째 원소를 제외하고 c개를 뽑는 것.

    combi_list = []

    if n == 1:
        return [[x] for x in _list]

    for idx in range(len(_list)):
        except_element = _list[idx]
        rest_list = _list[idx+ 1:]

        for sub_combi in combinations(rest_list, n-1):
            new_combi = [except_element] + sub_combi
            combi_list.append(new_combi)

    return combi_list

def printLab(lab):
    for line in lab:
        for char in line:
            print(char, end=' ')
        print()

def BFS(combi, lab, min_time, BLANK_COUNT):
    LENGTH = len(lab)

    BLANK = ' '
    WALL = '-'
    VIRUS = 2

    queue = deque(combi)
    visited_pos_set = set(combi)

    time = 0
    queue_length = len(queue)

    di = [-1, 0, 1, 0]
    dj = [0, -1, 0, 1]

    fill_blank_count = 0

    while len(queue) > 0:
        i, j = queue.popleft()
        queue_length -= 1

        if lab[i][j] == BLANK:
            fill_blank_count += 1

        # lab[i][j] = time

        for idx in range(4):
            ni, nj = i + di[idx], j + dj[idx]

            if 0 <= ni < LENGTH and 0 <= nj < LENGTH and (ni, nj) not in visited_pos_set and lab[ni][nj] != WALL:
                visited_pos_set.add((ni, nj))
                queue.append((ni, nj))

        if queue_length == 0:
            if fill_blank_count == BLANK_COUNT:
                return time

            time += 1
            queue_length = len(queue)

            # printLab(lab)
            # print()

    return 2500
def solution(n, m, lab):
    # 바이러스 좌표 계산

    BLANK = ' '
    WALL = '-'
    VIRUS = 2

    virus_pos_list = []

    BLANK_COUNT = 0

    for i in range(n):
        for j in range(n):
            if lab[i][j] == 1:
                lab[i][j] = WALL

            if lab[i][j] == VIRUS:
                virus_pos_list.append((i, j))

            if lab[i][j] == 0:
                lab[i][j] = BLANK
                BLANK_COUNT += 1

    min_time = 2500

    for combi in combinations(virus_pos_list, m):
        new_lab = deepcopy(lab)
        time = BFS(combi, new_lab, min_time, BLANK_COUNT)
        # print(time)
        # print()

        min_time = min(min_time, time)

    return min_time if min_time != 2500 else -1

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

answer = solution(n, m, lab)

print(answer)