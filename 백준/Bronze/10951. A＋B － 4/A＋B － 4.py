while True:
  try:
    a, b = map(int, input().split())
    print(sum([a, b]))
  except:
    break