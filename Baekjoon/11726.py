if __name__ == '__main__':
  n = int(input())
  count_arr = [0] * (n+1)

  count_arr[1] = 1
  try:
    count_arr[2] = 2
  except:
    pass

  for i in range(3, n+1):
    count_arr[i] = count_arr[i-1] + count_arr[i-2]

  print(count_arr[n] % 10007)
