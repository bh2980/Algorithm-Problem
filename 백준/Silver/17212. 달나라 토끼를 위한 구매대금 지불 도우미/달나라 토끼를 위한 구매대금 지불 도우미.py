n = int(input())

dp = [1 for _ in range(n + 1)]
dp[0] = 0

for i in range(3, n+1):
  value_list = []
  for coin in [1, 2, 5, 7]:
    if i - coin >= 0 :
      value_list.append(dp[i-coin])
    else:
      break

  dp[i] = min(value_list) + 1

print(dp[n])