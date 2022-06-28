def solution():
  _list = list(map(int, input().split()))

  if _list == [1, 2, 3, 4, 5, 6, 7, 8]:
    print('ascending')
  elif _list == [8, 7, 6, 5, 4, 3, 2, 1]:
    print('descending')
  else:
    print('mixed')

solution()