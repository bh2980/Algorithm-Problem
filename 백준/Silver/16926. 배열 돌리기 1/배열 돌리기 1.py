def Solution(arr, TL, BR, R, bound_length):
  x1, y1 = TL
  x2, y2 = BR

  x = x1
  y = y1
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  index = 0

  bound_list = []

  for _ in range(bound_length):
    if x == x2 and y == y1:
      index+=1
    elif x == x2 and y == y2:
      index+=1
    elif x == x1 and y == y2:
      index+=1
      
    bound_list.append(arr[x][y])
    
    x += dx[index]
    y += dy[index]

  bound_list = bound_list[R :] + bound_list[: R]

  x = x1
  y = y1
  index = 0

  for element in bound_list:
    if x == x2 and y == y1:
      index+=1
    elif x == x2 and y == y2:
      index+=1
    elif x == x1 and y == y2:
      index+=1
      
    arr[x][y] = (element)
    
    x += dx[index]
    y += dy[index]

if __name__ == '__main__':
  N, M, R = map(int, input().split())
  arr = [list(map(int, input().split())) for i in range(N)]

  s_x, s_y, e_x, e_y = 0, 0, N-1, M-1

  for i in range(min(N, M) // 2):
    bound_length = (e_x - s_x + 1) * 2 + (e_y - s_y + 1) * 2 - 4
    left = R % bound_length
    Solution(arr, (s_x, s_y), (e_x, e_y), left, bound_length)
    s_x += 1
    s_y += 1
    e_x -= 1
    e_y -= 1
    
  for line in arr:
    for element in line:
      print(element, end=' ')
    print()