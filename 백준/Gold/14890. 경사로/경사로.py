def solution(n, l, _map):
    # NxN의 지도가 주어진자
    # 모든 칸의 높이가 같으면 길
    # 경사로의 높이는 항상 1이고 높이는 L
        # 경사로는 낮은 칸에 놓고, L개의 연속된 칸에 모두 접해야함.
        # 경사로의 낮은 칸과 높은 칸의 차이는 1이어야한다.
        # 경사로를 놓을 낮은 칸의 높이는 모두 같아야하고, L개의 연속된 칸이 있어야함.

    # 지나갈 수 있는 길의 갯수

    # 경사로를 실제로 놓는게 아니라 놓았을 때 지나갈 수 있을만한 길을 찾는 것
        # 경사로를 놓음으로써 다른 길이 막힌다는 걱정은 할 필요 없음.
    # 행과 열을 탐색하면서 지나갈 수 있는 길인지 체크한다.
        # 행 or 열을 탐색하면서, 한 칸 전 값과 지금 값이 1 차이가 나면, 경사로를 놓을 수 있는지 검사한다.
            # 두 칸의 좌표를 받아서 낮은 쪽으로 L만큼 되는지 체크
    # 안되는걸 뺴는게 편할 것 같다
        # n*n 해놓고 안되면 -1

    answer = n * 2

    # 행 탐색

    for i in range(n):
        slide_point = set()

        for j in range(1, n):
            prev_value = _map[i][j-1]
            current_value = _map[i][j]
            slide = True

            if abs(prev_value - current_value) == 1:
                # 경사로 후보
                # 작은 쪽으로 길이가 L만큼 되는지 체크
                # 안되면 바로 break -> 다음 행 탐색

                if prev_value < current_value:
                    # 이전으로 돌아가야함. (0, -1)
                    for k in range(j-l, j): # l개가 prev_value랑 같아야함.
                        if k < 0 or _map[i][k] != prev_value or (i, k) in slide_point:
                            slide = False
                            break

                        slide_point.add((i, k))

                    # 끝에 닿는 경우 : PASS
                    # 바로 다음에 벽이 있는 경우 : FAIL
                    if 0 < j - l - 1 and _map[i][j - l - 1] > prev_value:
                        slide = False
                else:
                    # (0, 1)
                    for k in range(j, j+l):  # l개가 current_value랑 같아야함.
                        if n <= k or _map[i][k] != current_value or (i, k) in slide_point:
                            slide = False
                            break

                        slide_point.add((i, k))

                    # 끝에 닿는 경우 : PASS
                    # 바로 다음에 벽이 있는 경우 : FAIL
                    if j + l < n and _map[i][j + l] > current_value:
                        slide = False
            elif abs(prev_value - current_value) > 1:
                slide = False

            if not slide:
                answer -= 1
                break

    # 열 탐색
    for j in range(n):
        slide_point = set()

        for i in range(1, n):
            prev_value = _map[i-1][j]
            current_value = _map[i][j]
            slide = True

            if abs(prev_value - current_value) == 1:
                # 경사로 후보
                # 작은 쪽으로 길이가 L만큼 되는지 체크
                # 안되면 바로 break -> 다음 행 탐색

                if prev_value < current_value:
                    # 이전으로 돌아가야함. (0, -1)
                    for k in range(i-l, i): # l개가 prev_value랑 같아야함.
                        if k < 0 or _map[k][j] != prev_value or (k, j) in slide_point:
                            slide = False
                            break

                    slide_point.add((k, j))

                    # 끝에 닿는 경우 : PASS
                    # 바로 다음에 벽이 있는 경우 : FAIL
                    if 0 < i - l - 1 and _map[i - l - 1][j] > prev_value:
                        slide = False
                else:
                    # (0, 1)
                    for k in range(i, i+l):  # l개가 current_value랑 같아야함.
                        if n <= k or _map[k][j] != current_value or (k, j) in slide_point:
                            slide = False
                            break

                        slide_point.add((k, j))

                    # 끝에 닿는 경우 : PASS
                    # 바로 다음에 벽이 있는 경우 : FAIL
                    if i + l < n and _map[i + l][j] > current_value:
                        slide = False
            elif abs(prev_value - current_value) > 1:
                slide = False

            if not slide:
                answer -= 1
                break


    return answer

n, l  = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, l, _map))