#정사각형 테두리 채우기

point = None

def fillBorder(left_top, right_bottom, map, target):
  global point
  s_i, s_j = left_top
  e_i, e_j = right_bottom
  length = (e_j - s_j + 1) * 4 - 4
  number = (e_j - s_j + 1)**2

  di = [1, 0, -1, 0]
  dj = [0, 1, 0, -1]

  index = 0

  i = s_i
  j = s_j

  while True:
    if number == target:
      point = (i + 1, j + 1)

    if map[i][j] != 0:
      break
      
    map[i][j] = number
    number -= 1
    i, j = i + di[index], j + dj[index]
    
    if (i, j) in [(s_i, e_j), (e_i, e_j), (e_i, s_j)]:
      index += 1

n = int(input())
target = int(input())
map = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n//2 + 1):
  fillBorder((i, i), (n-i-1, n-i-1), map, target)

for line in map:
  print(*line)
print(*point)