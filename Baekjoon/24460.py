def DFS(arr, start, end):
  start_x, start_y = start
  end_x, end_y = end
  
  if end_x - start_x == 1:
    return sorted([arr[start_x][start_y], arr[start_x][end_y], arr[end_x][start_y], arr[end_x][end_y]])[1]

  mid_x = int((start_x + end_x) // 2) + 1
  mid_y = int((start_y + end_y) // 2) + 1

  return sorted([DFS(arr, (start_x, start_y), (mid_x-1, mid_y-1)), DFS(arr, (start_x, mid_y), (mid_x - 1, end_y)), DFS(arr, (mid_x, start_y), (end_x, mid_y-1)), DFS(arr, (mid_x, mid_y), (end_x, end_y))])[1]

if __name__ == '__main__':
  n = int(input())
  arr = []
  
  for _ in range(n):
    arr.append(list(map(int, input().split())))

  if len(arr) == 1:
    print(arr[0][0])
  else:
    print(DFS(arr, (0, 0), (len(arr)-1, len(arr)-1)))