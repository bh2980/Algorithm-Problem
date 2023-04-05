from collections import defaultdict

EMPTY = 0
WALL = 6
VIEWED = '#'

viewed_area = 0
min_val = float('inf')
def calcUnlookCCTVArea(office, cctv_list, total_empty):
    cctv_type = dict([
        [1, [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]]],
        [2, [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]],
        [3, [[(0, -1), (-1, 0)], [(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)]]],
        [4, [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)],
             [(1, 0), (0, -1), (-1, 0)]]],
        [5, [[(0, 1), (0, -1), (1, 0), (-1, 0)]]]])

    N = len(office)
    M = len(office[0])

    def recursiveDFS(office, cctv_list):
        global viewed_area
        global min_val

        if len(cctv_list) == 0:
            min_val = min(min_val, total_empty - viewed_area)

            return

        #office와 cctv list를 받는다
        #cctv_list => point, type
        #반복문으로 가능한 가짓수에 대해 돌린다.
        #돌리면서 다음 cctv idx를 호출한다.
        #마지막에 도달했을 경우 return한다.

        point, type = cctv_list[0]
        cctv_r, cctv_c = point

        # 하나의 바라보는 방향을 선택
        for dir_list in cctv_type[type]:
            # 바라보는 방향에 office에서 # 표시
            # OR set에 넣음. -> set에 넣을 경우 set도 내려줘야함.

            change_list = []

            for dr, dc in dir_list:
                nr = cctv_r + dr
                nc = cctv_c + dc

                # 시야 채워넣기
                while 0 <= nr < N and 0 <= nc < M and office[nr][nc] != WALL: # 범위 밖으로 나가거나 벽에 닿을 때까지
                    if office[nr][nc] == EMPTY: #EMPTY 칸이라면
                        office[nr][nc] = VIEWED # 시야 표시
                        change_list.append((nr, nc))
                        viewed_area += 1

                    # 위치 이동
                    nr += dr
                    nc += dc

            recursiveDFS(office, cctv_list[1:])

            for change_r, change_c in change_list:
                office[change_r][change_c] = 0

            viewed_area -= len(change_list)

    recursiveDFS(office, cctv_list)

    return min_val
def solution(N, M, office):
    # 1번 1방향            4개
#   # 2번 서로 반대 방향     2개
    # 3번 서로 직각         4개
    # 4번 3방향            4개
    # 5번 4방향            1개

    # CCTV는 벽을 넘을 수 없으나, CCTV는 넘을 수 있다.

    # 최소 사각지대

    # DFS로 할 수 있지 않을까?
    # CCTV 하나 할 떄마다 1 depth씩 깊어지게
    # 모든 CCTV 완료 후 최솟값 갱신

    total_empty = 0

    cctv_list = defaultdict(lambda : [])

    # cctv 모두 찾기, 빈 칸 개수 계산
    for i in range(N):
        for j in range(M):
            if office[i][j] == WALL:
                continue

            if office[i][j] == EMPTY:
                total_empty += 1
                continue

            cctv_list[(i, j)] = office[i][j]

    print(calcUnlookCCTVArea(office, list(cctv_list.items()), total_empty))

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

solution(N, M, office)