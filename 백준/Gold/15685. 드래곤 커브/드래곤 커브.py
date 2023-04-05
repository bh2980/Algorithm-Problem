from collections import defaultdict

EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3

direction = dict([[EAST, (0, 1)], [NORTH, (-1, 0)], [WEST, (0, -1)], [SOUTH, (1, 0)]])

def makeRotatePoint(r, c, margin):
    dr, dc = margin

    # 평행 이동
    move_r, move_c = r - dr, c - dc
    # 시계 방향 회전 변환
    rot_r, rot_c = move_c, -move_r
    # 평행 이동 복구
    fin_r, fin_c = rot_r + dr, rot_c + dc

    return (fin_r, fin_c)
def makeDragonCurve(row, col, dir, gen): #x, y 반대로 넣을 것
    # 다음 세대의 드래곤 커브를 만드는 방법

    if gen == 0:
        # [끝점, 구성요소 리스트]
        dr, dc = direction[dir]
        origin_r, origin_c = row + dr, col + dc
        return [(origin_r, origin_c), [(origin_r, origin_c), (row, col)]]

    curve_points = []

    # 이전 세대 드래곤 커브를 가져온다.
    prev_endpoint, prev_point_list = makeDragonCurve(row, col, dir, gen - 1)

    # 끝점을 원점으로 이동시키는 만큼 모든 점을 이동시킨다.. -> 끝점을 알고 있어야한다.
    new_point_list = set(prev_point_list)

    for prev_row, prev_col in prev_point_list:
        # 기존 점 끝점 기준 회전변환
        new_point_list.add(makeRotatePoint(prev_row, prev_col, prev_endpoint))

    # 다음 세대의 끝점은 원점 (0, 0)이 회전 및 이동된 좌표
    new_endpoint = makeRotatePoint(row, col, prev_endpoint)

    return [new_endpoint, list(new_point_list)]

def solution(n, dragon_curves):
    # 다음 세대 드래곤 커브
        # 이전 세대 드래곤 커브의 끝 점을 기준으로 90도 시계 방향 회전
        # 그것을 끝 점에 붙인 것임
    # 격자 위에는 N개의 드래곤 커브가 존재
    # x, y, d, g

    # 1x1 크기의 정사각형의 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수

    # x -> col, y -> row
    # 드래곤 커브의 모든 점들을 합한 set을 만든다.
    # set을 리스트로 만들고 안의 점들에 대해 돌아가면서, 그 점을 포함하는 정사각형의 다른 꼭짓점이 모두 set안에 있는지 체크한다.

    total_points = set()

    for c, r, d, g in dragon_curves:
        end, points = makeDragonCurve(r, c, d, g)
        total_points |= set(points)

    square_count = 0

    # 개수 세기
    for i in range(100):
        for j in range(100):
            point1 = (i, j)
            point2 = (i + 1, j)
            point3 = (i, j + 1)
            point4 = (i + 1, j + 1)

            if point1 in total_points and point2 in total_points and point3 in total_points and point4 in total_points:
                square_count += 1

    return square_count


n = int(input())
dragon_curves = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, dragon_curves))