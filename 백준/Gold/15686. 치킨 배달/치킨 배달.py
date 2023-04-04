def combination(list, count):
    if count == 1:
        return [[i] for i in list]

    combi_list = []

    for i in range(len(list)):
        fix_element = list[i]

        for combi in combination(list[i + 1:], count - 1):
            combi_list.append([fix_element] + combi)

    return combi_list

def calcManhattanDis(p1, p2):
    ar, ac = p1
    br, bc = p2

    return abs(ar - br) + abs(ac - bc)

def solution(n, m, city_map):
    BLANK = 0
    HOME = 1
    CHICKEN = 2

    homeList = []
    chickenList = []

    # N^2
    for i in range(n):
        for j in range(n):
        # 집과 치킨집을 모두 찾아 좌표화 시킨다.
            if city_map[i][j] == HOME:
                homeList.append((i, j))
            elif city_map[i][j] == CHICKEN:
                chickenList.append((i, j))

    # 치킨집의 조합을 만든다.
    combi_list = combination(chickenList, m)

    # 최소 거리를 구한다.
    # 하나의 조합을 가져온다.
    # 모든 집에 대해서 각 조합의 집 중 가장 거리가 작은 것을 누적한다. => 해당 조합의 치킨 거리
    # min_dis와 비교해서 업데이트한다.
    min_dis = float("inf")

    for combi in combi_list:
        combi_min_dis = 0

        for home in homeList:
            # 각 집별로 가장 가까운 치킨집과의 거리를 구해 누적
            combi_min_dis += min([calcManhattanDis(home, chicken) for chicken in combi])

        if combi_min_dis < min_dis:
            min_dis = combi_min_dis

    return min_dis

n, m = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, m, city_map))