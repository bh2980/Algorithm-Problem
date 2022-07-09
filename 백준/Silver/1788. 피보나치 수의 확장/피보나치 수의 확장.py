def solution():
  n = int(input())
  
  if n == 0:
    print(0)
    print(0)
    return
    
  sign = 'MINUS' if n < 0 else 'PLUS'
  
  n = abs(n)
  dp = [0, 1] + [1 for _ in range(n-1)]
  
  for i in range(2, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 1000000000
  
  if n % 2 == 0 and sign == 'MINUS':
    print(-1)
  else:
    print(1)
  
  print(dp[n])

solution()