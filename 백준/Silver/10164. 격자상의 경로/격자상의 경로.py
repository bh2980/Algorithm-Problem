def calcWay(start, end, map):
  s_x, s_y = start
  e_x, e_y = end

  for i in range(s_x, e_x + 1):
    map[i][s_y] = map[s_x][s_y]

  for j in range(s_y, e_y + 1):
    map[s_x][j] = map[s_x][s_y]

  for i in range(s_x+1, e_x + 1):
    for j in range(s_y+1, e_y + 1):
      map[i][j] = map[i-1][j] + map[i][j-1]

  return map[e_x][e_y]

n, m, k = map(int, input().split())

map = [[1 for _ in range(m)] for _ in range(n)]

if k != 0:
  #k 위치의 좌표 구하기
  k -= 1
  
  row = k // m
  col = k % m

  calcWay((0, 0), (row, col), map)
  print(calcWay((row, col), (n-1, m-1), map))
  
else:#필수 칸이 없는 경우
  print(calcWay((0, 0), (n-1, m-1), map))