import sys
from collections import deque

KEY_SIZE = 'size'
KEY_EAT_FISH = 'eatFish'
KEY_POINT = 'point'

def input():
    return sys.stdin.readline().strip()

# BFS가 아니라, 우선순위 큐?

def calcDistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)

# BFS에서 같은 거리를 전부 뽑는다.
# 가장 가까운 거리에 있는 먹을 수 있는 것을 뽑는다. 같은 거리 내에서 상단 같다면 왼쪽에 있는 애를 뽑는다.
def BFS(seaMap, babyShark, visitedMap):
    global KEY_SIZE
    global KEY_POINT
    global KEY_EAT_FISH

    VISITED = 1
    BLANK = 0

    ROW_LENGTH = len(seaMap)
    COL_LENGTH = len(seaMap[0])

    currentPoint = babyShark[KEY_POINT]
    sharkSize = babyShark[KEY_SIZE]

    queue = deque([currentPoint])
    i, j = currentPoint
    visitedMap[i][j] = VISITED

    levelCount = 1
    distance = 0

    minNode = (999, 999)

    # queue를 돌면서 가장 가까운 먹을 수 있는 물고기를 찾는다.
    while len(queue) > 0:
        i, j = queue.popleft()
        levelCount -= 1

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        for idx in range(4):
            ni, nj = i + dx[idx], j + dy[idx]

            if 0 <= ni < ROW_LENGTH and 0 <= nj < COL_LENGTH and visitedMap[ni][nj] != VISITED:
                if seaMap[ni][nj] <= sharkSize:
                    visitedMap[ni][nj] = VISITED
                    queue.append((ni, nj))

        if seaMap[i][j] != BLANK and seaMap[i][j] < sharkSize:
            # 먹을 수 있는 칸
            if (i, j) < minNode:
                minNode = (i, j)

        if levelCount == 0:
            levelCount = len(queue)

            if minNode != (999, 999):
                return (minNode, distance)

            distance += 1

    return (False, 0)

def solution(n, seaMap):
    global KEY_SIZE
    global KEY_POINT
    global KEY_EAT_FISH

    SHARK = 9

    answer = 0

    babyShark = dict()
    babyShark[KEY_SIZE] = 2
    babyShark[KEY_EAT_FISH] = 0
    babyShark[KEY_POINT] = None

    for i in range(n):
        for j in range(n):
            if seaMap[i][j] == SHARK:
                babyShark[KEY_POINT] = (i, j)
                seaMap[i][j] = 0
                break

        if babyShark[KEY_POINT] != None:
            break

    visitedMap = [[0 for _ in range(n)] for _ in range(n)]

    while True:
        result, distance = BFS(seaMap, babyShark, visitedMap)

        if result == False:
            break
        else:
            answer += distance
            # print(f'{babyShark[KEY_POINT]}에서 {result}이동까지 {distance}초 걸림')
            babyShark[KEY_POINT] = result
            babyShark[KEY_EAT_FISH] += 1

            fi, fj = result
            seaMap[fi][fj] = 0

            # print(f'{answer}초')
            # for idx in range(n):
            #     for jdx in range(n):
            #         print(seaMap[idx][jdx] if (idx, jdx) != babyShark[KEY_POINT] else '★', end=' ')
            #     print()

            if babyShark[KEY_EAT_FISH] == babyShark[KEY_SIZE]:
                babyShark[KEY_SIZE] += 1
                babyShark[KEY_EAT_FISH] = 0
                # print(f'상어 크기 : {babyShark[KEY_SIZE]}, 위치 : {babyShark[KEY_POINT]}')

            visitedMap = [[0 for _ in range(n)] for _ in range(n)]

    return answer

n = int(input())
seaMap = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, seaMap))