n, k = map(int, input().split())

dp = [1 for _ in range(n+1)]

for i in range(1, n+1):
  dp[i] = (dp[i-1] * i)

print(int((dp[n] // (dp[n-k] * dp[k]))  % 10007))