n, m = map(int, input().split())
light = list(map(int, input().split()))

for _ in range(m):
  inst, b, c = map(int, input().split())

  if inst != 1 and b > c:
    b, c = c, b

  if inst == 1:
    light[b-1] = c
  elif inst == 2:
    for i in range(b, c+1):
      light[i-1] = 1 if light[i-1] == 0 else 0
  elif inst == 3:
    for i in range(b, c+1):
      light[i-1] = 0
  else:
    for i in range(b, c+1):
      light[i-1] = 1

print(*light)