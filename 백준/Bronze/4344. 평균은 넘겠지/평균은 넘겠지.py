for _ in range(int(input())):
  n, *score = list(map(int, input().split()))
  total = sum(score)
  upper = [s for s in score if s > total/n]
  print('{:.3f}%'.format(len(upper)*100/n))