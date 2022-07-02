hours = []

while True:
  h = int(input())
  if h == -1:
    break

  hours.append(h)

max_hour = max(hours)

dp = [0 for _ in range(max_hour + 1)]
dp[1] = 1

for index in range(2, max_hour + 1):
  dp[index] = dp[index-1] + dp[index-2]

for hour in hours:
  print(f'Hour {hour}: {dp[hour]} cow(s) affected')