n = int(input())

dp = [0, 0, 2, 3] + [0 for _ in range(n-3)]

for i in range(4, n+1):
  dp[i] = (dp[i-2] + dp[i-1]) % 10

print(dp[n])