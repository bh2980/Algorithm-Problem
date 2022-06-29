def makeNumber(current, map, output):
  i, j = current
  di = [0, 1, -1, 0, -1, -1, 1, 1]
  dj = [1, 0, 0, -1, -1, 1, -1, 1]
  mine = 0

  if map[i][j] == '*':
    return True

  for index in range(8):
    ni = i + di[index]
    nj = j + dj[index]
    
    if 0 <= ni < len(map) and 0 <= nj < len(map) and map[ni][nj] == '*':
      mine += 1

  output[i][j] = mine
  
  return False

n = int(input())
map = [list(input()) for _ in range(n)]
open = [list(input()) for _ in range(n)]
output = [list('.' for _ in range(n)) for _ in range(n)]
mine = False

for i in range(n):
  for j in range(n):
    if open[i][j] == 'x':
      mine |= makeNumber((i, j), map, output)

if mine:
  for i in range(n):
    for j in range(n):
      if map[i][j] == '*':
        output[i][j] = '*'

for line in output:
  for char in line:
    print(char, end='')
  print()