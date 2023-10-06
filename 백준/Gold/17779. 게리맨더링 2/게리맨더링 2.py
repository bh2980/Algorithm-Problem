# 노가다 다 돌려봐야할 듯 -> 커트 혹은 backtracking이 중요함.
# 한 번 싹 훑으면서 각 구역의 인구 수를 한번에 더하는게 좋을 것 같음.
# 기준점 하나에 대해서 가능한 모든 조합을 전부 계산
# 각 거리만큼 띄워진 좌표를 적하고, 그 좌표에 대해서 아래 교점을 계산
# n*n을 돌면서 각 구역별로 인구 수를 계산
# 최소 최대 값 체크

# 0 <= X < N-2
# 1 <= Y < N-1

# 2차원 슬라이딩 윈도우?

from copy import deepcopy

def printMap(CITY, origin, left, right, bottom):
    PRINT_CITY = deepcopy(CITY)
    for i in range(N):
        for j in range(N):
            if isArea1((i, j), origin, left, N):
                PRINT_CITY[i][j] = 1
            elif isArea2((i, j), origin, right, N):
                PRINT_CITY[i][j] = 2
            elif isArea3((i, j), bottom, left, N):
                PRINT_CITY[i][j] = 3
            elif isArea4((i, j), bottom, right, N):
                PRINT_CITY[i][j] = 4
            else:
                PRINT_CITY[i][j] = 5

    for line in PRINT_CITY:
        for char in line:
            print(char, end=' ')
        print()
    print()

    return

def isArea1(point, origin, left, N):
    oi, oj = origin
    li, lj = left
    pi, pj = point

    if 0 <= pi < li and 0 <= pj <= oj and  (oj-lj) * (pi - oi) + (oj - pj) * (oi - li) < 0:
        return True

    return False

def isArea2(point, origin, right, N):
    oi, oj = origin
    ri, rj = right
    pi, pj = point

    if 0 <= pi <= ri and oj < pj < N and (oj - rj) * (pi - oi) + (oj - pj) * (oi - ri) > 0:
        return True

    return False

def isArea3(point, bottom, left, N):
    bi, bj = bottom
    li, lj = left
    pi, pj = point

    if li <= pi < N and 0 <= pj < bj and (bj - lj) * (pi - bi) + (bj - pj) * (bi - li) > 0:
        return True

    return False

def isArea4(point, bottom, right, N):
    bi, bj = bottom
    ri, rj = right
    pi, pj = point

    if ri < pi < N and bj <= pj < N and (bj - rj) * (pi - bi) + (bj - pj) * (bi - ri) < 0:
        return True

    return False

def calcDividePersonCount(origin, left, right, bottom, CITY):
    N = len(CITY)

    countArea1 = 0
    countArea2 = 0
    countArea3 = 0
    countArea4 = 0
    countArea5 = 0

    for i in range(N):
        for j in range(N):
            if isArea1((i, j), origin, left, N):
                countArea1 += CITY[i][j]
            elif isArea2((i, j), origin, right, N):
                countArea2 += CITY[i][j]
            elif isArea3((i, j), bottom, left, N):
                countArea3 += CITY[i][j]
            elif isArea4((i, j), bottom, right, N):
                countArea4 += CITY[i][j]
            else:
                countArea5 += CITY[i][j]

    # printMap(CITY, origin, left, right, bottom)
    # print(countArea1, countArea2, countArea3,countArea4, countArea5)
    # print(max(countArea1, countArea2, countArea3, countArea4, countArea5) - min(countArea1, countArea2, countArea3, countArea4, countArea5))
    # print()

    return max(countArea1, countArea2, countArea3, countArea4, countArea5) - min(countArea1, countArea2, countArea3, countArea4, countArea5)

def calcBottomPoint(origin, left, right):
    oi, oj = origin
    li, lj = left
    ri, rj = right

    d2 = ri - oi

    bi, bj = li + d2, lj + d2

    return (bi, bj)

def checkSidePoint(point):
    pi, pj = point

    if 1 <= pi < N-1 and 0 <= pj < N:
        return True

    return False
def squareLoop(origin, CITY):
    N = len(CITY)
    oi, oj = origin

    min_diff = 100 * 20 * 20 + 1

    # left
    for d1 in range(1, N):
        li = oi + d1
        lj = oj - d1

        if not checkSidePoint((li, lj)):
            break

        R_LIMIT = N - oj

        # right
        for d2 in range(1, R_LIMIT):
            ri = oi + d2
            rj = oj + d2

            if not checkSidePoint((ri, rj)):
                break

            bottomPoint = calcBottomPoint((oi, oj), (li, lj), (ri, rj))

            min_diff = min(min_diff, calcDividePersonCount((oi, oj), (li, lj), (ri, rj), bottomPoint, CITY))

    return min_diff

def solution(N, CITY):
    min_diff = 100 * 20 * 20 + 1

    for i in range(N-2):
        for j in range(1, N-1):
            min_diff = min(min_diff, squareLoop((i, j), CITY))

    return min_diff

N = int(input())
CITY = [list(map(int, input().split())) for _ in range(N)]

ans = solution(N, CITY)

print(ans)