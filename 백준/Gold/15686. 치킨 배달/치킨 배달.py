def makePointToKey(r, c):
    return f'{r}-{c}'

def makeKeyToPoint(key):
    return map(int, key.split('-'))

# def combinations(list, count):
#     visited = [False] * len(list)
#     combi_list = []
# 
#     def makeCombinations(list, count, temp_combi = []):
#         if count == 0:
#             combi_list.append([i for i in temp_combi])
#             return
# 
#         for i in range(len(list)):
#             if not visited[i]:
#                 temp_combi.append(list[i])
#                 visited[i] = True
#                 makeCombinations(list, count - 1)
#                 temp_combi.pop()
#                 visited[i] = False
# 
#     makeCombinations(list, count)
# 
#     return combi_list
from itertools import combinations

def calcManhattanDis(p1, p2):
    ar, ac = p1
    br, bc = p2

    return abs(ar - br) + abs(ac - bc)

def solution(n, m, city_map):
    BLANK = 0
    HOME = 1
    CHICKEN = 2

    homeList = dict() #집의 좌표 key로 각 치킨집 별 거리를 계산 치킨집 좌표 - 거리
    chickenList = []

    # N^2
    for i in range(n):
        for j in range(n):
        # 집과 치킨집을 모두 찾아 좌표화 시킨다.
            if city_map[i][j] == HOME:
                homeList[makePointToKey(i, j)] = dict()
            elif city_map[i][j] == CHICKEN:
                chickenList.append((i, j))

    # N^2
    # 각 집에서 모든 치킨집까지의 거리를 모두 구한다.
    for cr, cc in chickenList:
        for key in homeList.keys():
            hr, hc = makeKeyToPoint(key)

            homeList[key][makePointToKey(cr, cc)] = calcManhattanDis((cr, cc), (hr, hc))

    min_dis = float("inf")

    # 치킨집의 조합을 만든다.
    combi_list = combinations(chickenList, m)

    for combi in combi_list:
        acc_dis = 0

        for value in homeList.values():
            each_min_dis = float("inf")

            for point in combi:
                cr, cc = point

                if value[makePointToKey(cr, cc)] < each_min_dis:
                    each_min_dis = value[makePointToKey(cr, cc)]

            acc_dis += each_min_dis

        if acc_dis < min_dis:
            min_dis = acc_dis

    return min_dis

n, m = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, m, city_map))