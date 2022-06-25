if __name__ == '__main__':
  n, m = map(int, input().split())
  board = []
  for i in range(n):
    board.append(list(map(int, input().split())))

  blocks = [[(0,0), (0,1),(0,2),(0,3)],[(0,0), (1,0), (2,0), (3,0)], [(0,0), (0,1), (1,0), (1,1)], [(0, 0), (1, 0), (2, 0), (2, 1)], [(0,0), (0,1), (0, 2), (-1, 2)], [(0, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (1, 0), (0, 1), (0,  2)], [(0, 0), (1, 0), (2, 0), (2, -1)], [(0, 0), (0, 1), (0, 2), (1, 2)], [(0, 0), (0, 1), (1, 0), (2, 0)], [(0, 0), (1, 0), (1, 1), (1, 2)], [(0,0), (1, 0), (1, 1), (2, 1)], [(0, 0), (0, 1), (-1, 1), (-1, 2)], [(0, 0), (1, 0), (1, -1), (2, -1)], [(0, 0), (0, 1), (1, 1), (1, 2)], [(0, 0), (1, -1), (1, 0), (1, 1)], [(-1, 0), (0, 0), (1, 0), (0, 1)], [(0, -1), (0, 0), (0, 1), (1, 0)], [(0, 0), (-1, 0), (1, 0), (0, -1)]]


  max_val = 0

  for i in range(n):
    for j in range(m):
      for b in blocks:
        val = 0
        try:
          for dx, dy in b:
            if i+dx < 0 or j+dy < 0:
              continue
              
            val += board[i+dx][j+dy]
        except:
          pass

        if val > max_val:
          max_val = val

  print(max_val)
          