if __name__ == '__main__':
  people = 0
  max_p = 0
  
  while True:
    try:
      minus, plus = map(int, input().split())
      people = people - minus + plus
      if max_p < people:
        max_p = people
    except:
      break

  print(max_p)