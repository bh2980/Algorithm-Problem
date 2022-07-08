T = int(input())

for _ in range(T):
  n, m = map(int, input().split())

  dp = [1 for _ in range(m+1)]

  for i in range(2, m+1):
    dp[i] = dp[i-1] * i

  print(int(dp[m]/(dp[m-n]*dp[n])))
  