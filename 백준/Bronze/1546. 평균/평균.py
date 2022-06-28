def solution():
  n = int(input())
  score = list(map(int, input().split()))

  max_score = max(score)

  new_score = list(map(lambda x:x/max_score*100, score))

  print(sum(new_score)/n)

solution()