def solution(world):
  sum = 0

  for line in world:
    count = 0
    ing = False
    for box in line:
      if not ing and box == 1:#counting 시작
        ing = True
      elif ing and box == 1:#counting 중 벽 만나면 update
        sum += count
        count = 0
      elif ing and box == 0:#counting 중
        count += 1

  return sum

if __name__ == '__main__':
  n, m = map(int, input().split())
  height = list(map(int, input().split()))
  world = []

  for i in range(n):
    width = []
    for j in range(m):
      if i < height[j]:
        width.append(1)
      else:
        width.append(0)

    world.append(width)

  print(solution(world))