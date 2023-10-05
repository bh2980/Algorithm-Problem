# https://www.acmicpc.net/problem/20058
# n x n 지도, 각 칸은 얼음의 양, 0이면 얼음이 없음.
# Q번 2^L만큼으로 나누어서 시계방향으로 돌린다.
# 상하좌우 인접한 칸 중 얼음이 있는 칸이 3개 이하인 칸은 얼음의 양이 1 줄어든다.

# 남아있는 얼음의 총합
# 남아있는 얼음 덩어리 중 가장 큰 것의 크기

# 얼음의 총합과 가장 큰 것의 크기는 DFS(BFS)로 구한다.

# 돌리는 로직
# 2^N개를 가져온다. -> 시계 방향으로 돌린다.
# start, end를 받는다.
# 테두리를 시계 방향으로 돌린다.
# 내부 네모에 대해 재귀적으로 돌린다.

def printMap(iceMap):
    for line in iceMap:
        for char in line:
            print(char, end=' ')
        print()
    print()

def rotateBorder(start, end, iceMap):
    si, sj = start
    ei, ej = end

    if si == ei:
        return

    up = [iceMap[si][j] for j in range(sj, ej)]
    right = [iceMap[i][ej] for i in range(si, ei)]
    down = [iceMap[ei][j] for j in range(ej, sj, -1)]
    left = [iceMap[i][sj] for i in range(ei, si, -1)]

    # up
    idx = 0
    for j in range(sj, ej):
        iceMap[si][j] = left[idx]
        idx += 1

    # right
    idx = 0
    for i in range(si, ei):
        iceMap[i][ej] = up[idx]
        idx += 1

    # down
    idx = 0
    for j in range(ej, sj, -1):
        iceMap[ei][j] = right[idx]
        idx += 1

    # left
    idx = 0
    for i in range(ei, si, -1):
        iceMap[i][sj] = down[idx]
        idx += 1

    return

def rotateSquare(start, end, iceMap):
    si, sj = start
    ei, ej = end

    if si == ei:
        return

    mid = (ei - si) // 2 + 1

    # print(mid)

    for move in range(mid):
        nsi, nsj = si + move, sj + move
        nei, nej = ei - move, ej - move

        rotateBorder((nsi, nsj), (nei, nej), iceMap)

    return

from copy import deepcopy

# 얼음 감소 시키기
# 상하좌우에 인접한 칸 중 얼음이 있는 칸이 3개 미만이라면 1 감소
# deepcopy하지 않고 할 수 있는 방법
def decreaseIce(iceMap):
    refMap = dict()
    LENGTH = len(iceMap)

    di = [-1, 0, 1, 0]
    dj = [0, -1, 0, 1]

    for i in range(LENGTH):
        for j in range(LENGTH):
            if iceMap[i][j] == 0:
                continue

            count = 0

            # 인접해 있는 칸 중 얼음이 있는 칸이 3개 미만이면 -1
            for idx in range(4):
                ni, nj = i + di[idx], j + dj[idx]

                if 0 <= ni < LENGTH and 0 <= nj < LENGTH:
                    if (ni, nj) in refMap:
                        if refMap[(ni, nj)] != 0:
                            count += 1
                    else:
                        if iceMap[ni][nj] != 0:
                            count += 1

            if count < 3:
                refMap[(i, j)] = iceMap[i][j]
                iceMap[i][j] -= 1

    return

from collections import deque

# DFS, BFS를 통해 가장 큰 얼음 면적 구하기
# 돌면서 남아잇는 얼음 총 면적 구하기
def calcRestIce(iceMap):
    LENGTH = len(iceMap)
    totalIce = 0
    maxSize = 0
    visitedSet = set()

    for i in range(LENGTH):
        for j in range(LENGTH):
            totalIce += iceMap[i][j]

            if iceMap[i][j] == 0 or (i, j) in visitedSet:
                continue

            queue = deque([(i, j)])
            visitedSet.add((i, j))
            iceSize = 0

            di = [-1, 0, 1, 0]
            dj = [0, -1, 0, 1]

            while len(queue) > 0:
                ci, cj = queue.popleft()
                iceSize += 1

                for idx in range(4):
                    ni, nj = ci + di[idx], cj + dj[idx]

                    if 0 <= ni < LENGTH and 0 <= nj < LENGTH and (ni, nj) not in visitedSet and iceMap[ni][nj] != 0:
                        visitedSet.add((ni, nj))
                        queue.append((ni, nj))

            maxSize = max(iceSize, maxSize)

    return [totalIce, maxSize]

def solution(N, Q, L, iceMap):
    # 2^L개로 얼음을 나눈다.
    # Q번 rotate 한다.

    for idx in range(Q):
        iceCut = 2**L[idx]

        # print(L, f'{idx}번 째: {iceCut}')

        for i in range(0, 2**N, iceCut):
            for j in range(0, 2**N, iceCut):
                start = (i, j)
                end = (i + iceCut - 1, j + iceCut - 1)

                rotateSquare(start, end, iceMap)

        decreaseIce(iceMap)

    return calcRestIce(iceMap)

N, Q = map(int, input().split())
iceMap = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

for ans in solution(N, Q, L, iceMap):
    print(ans)

# printMap(iceMap)