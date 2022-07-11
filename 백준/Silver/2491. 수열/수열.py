n = int(input())
numbers = list(map(int, input().split()))

up_same = [1 for _ in range(n)]
down_same = [1 for _ in range(n)]

pre = numbers[0]

for index in range(1, n):
  if pre <= numbers[index]:
    up_same[index] = up_same[index - 1] + 1
  else:
    up_same[index] = 1

  if pre >= numbers[index]:
    down_same[index] = down_same[index - 1] + 1
  else:
    down_same[index] = 1

  pre = numbers[index]

print(max(max(up_same), max(down_same)))