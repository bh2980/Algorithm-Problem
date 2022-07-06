n = int(input())

a = n // 5

while True:
  if a < 0:
    print(-1)
    break
    
  new_N = n - a * 5
  if new_N % 3 == 0:
    print(a + new_N // 3)
    break

  a -= 1