if __name__ == '__main__':
  n = int(input())
  arr = []
  for _ in range(n):
    arr.append(list(map(int, input().split())))

  pre_index = arr[0].index(max(arr[0]))

  for i in range(1, n):
    index_arr = set([0, 1, 2])
    index_arr.remove(pre_index)

    can1 = index_arr.pop()
    can2 = index_arr.pop()

    for j in range(3):
      if can1 == j:
        arr[i][j] += arr[i-1][can2]
      elif can2 == j:
        arr[i][j] += arr[i-1][can1]
      else:
        arr[i][j] += min(arr[i-1][can1], arr[i-1][can2])
        
    pre_index = arr[i].index(max(arr[i]))

  print(min(arr[n-1]))