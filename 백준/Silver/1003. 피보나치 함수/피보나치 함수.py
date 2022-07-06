T = int(input())

for _ in range(T):
  n = int(input())
  dp = [[0 for _ in range(n+1)] for _ in range(2)]

  try:
    dp[0][0] = 1
    dp[1][1] = 1
  except:
    pass

  for i in range(2, n+1):
    dp[0][i] = dp[0][i-1] + dp[0][i-2]
    dp[1][i] = dp[1][i-1] + dp[1][i-2]

  print(dp[0][n], dp[1][n])
    