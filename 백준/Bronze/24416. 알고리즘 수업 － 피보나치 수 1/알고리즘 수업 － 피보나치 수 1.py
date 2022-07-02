dp = 0

def dp_fib(n):
  global dp
  fibo = [0 for _ in range(n + 1)]
  fibo[1] = 1
  fibo[2] = 1

  for i in range(3, n+1):
    dp += 1
    fibo[i] = fibo[i-2] + fibo[i-1]

  return fibo[n]

n = int(input())
recur = dp_fib(n)

print(recur, dp)

