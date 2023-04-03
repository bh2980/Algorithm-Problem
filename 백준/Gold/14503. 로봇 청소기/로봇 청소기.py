import sys

def solution(n, m, r, c, d, clean_map):
  answer = 0

  NO_CLEAN = 0
  CLEAN = 2
  WALL = 1

  # (r, c)
  # 컴퓨터는 row와 column으로 하고 row -> column 순서로 찾는다.

  direction = dict([[0, [-1, 0]],[1, [0, 1]],[2, [1, 0]],[3, [0, -1]]])
  check_tile = [(0, 1), (1, 0), (-1, 0), (0, -1)]

  while True:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if clean_map[r][c] == NO_CLEAN:
      clean_map[r][c] = CLEAN
      answer += 1

    is_no_clean = False

    for ar, ac in check_tile:
      nr = r + ar
      nc = c + ac

      if 0 <= nr < n and 0 <= nc < m and clean_map[nr][nc] == NO_CLEAN:
        is_no_clean = True
        break

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    if is_no_clean:
      # 반시계 방향으로 90도 회전한다. 
      d = d - 1 if d - 1 >= 0 else 3
      # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
      mr = r + direction[d][0]
      mc = c + direction[d][1]

      if clean_map[mr][mc] == NO_CLEAN:
        r = mr
        c = mc
    else:  # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
      # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
      mr = r - direction[d][0]
      mc = c - direction[d][1]

      if clean_map[mr][mc] != WALL:
        r = mr
        c = mc
      else: # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        return answer

def input():
  return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
r, c, d = map(int, input().split())
clean_map = [list(map(int, input().split())) for i in range(n)]

answer = solution(n, m, r, c, d, clean_map)

print(answer)