import sys
sys.setrecursionlimit(10**6)

def DFS(current, matrix):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  x, y = current

  if matrix[x][y] <= 0:
    return 0
  else:
    matrix[x][y] = -1
    
    for i in range(4):
      if 0 <= x + dx[i] < len(matrix) and 0 <= y + dy[i] < len(matrix[0]):
        DFS((x+dx[i], y+dy[i]), matrix)

    return 1
  
if __name__ == '__main__':
  T = int(input())
  
  for i in range(T):
    row, col, count = map(int, input().split())
    cabbage = [list(map(int, input().split())) for _ in range(count)]
    matrix = [[0] * col for _ in range(row)]
    ans = 0

    for node in cabbage:
      x, y = node
      matrix[x][y] = 1

    for node in cabbage:
      ans += DFS(node, matrix)

    print(ans)
    