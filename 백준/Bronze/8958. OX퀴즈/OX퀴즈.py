def solution():
  T = int(input())

  for i in range(T):
    sum = 0
    
    ox = list(input())

    pre = ''
    pre_score = 0

    for char in ox:
      if char == 'O':
        if pre == char:
          sum += pre_score + 1
          pre_score = pre_score + 1
        else:
          sum += 1
          pre_score = 1
      else:
        pre_score = 0

      pre = char

    print(sum)

solution()