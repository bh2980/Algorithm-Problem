if __name__ == '__main__':
  n = int(input())
  fibo = [0] * (n+1)

  try:
    fibo[1] = 1
  except:
    pass

  for i in range(2, n+1):
    fibo[i] = fibo[i-2] + fibo[i-1]

  print(fibo[n])