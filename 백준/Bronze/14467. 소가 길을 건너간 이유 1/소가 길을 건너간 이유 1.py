n = int(input())
cows = dict()

for _ in range(n):
  cow, loc = map(int, input().split())
  try:
    if cows[cow][0] != loc:
      cows[cow][0] = loc
      cows[cow][1] += 1
  except:
    cows[cow] = [loc, 0]

print(sum(list(map(lambda x:x[1], cows.values()))))