import math

for a in range(1, 1000):
  for b in range(a, 1000):
    c = 1000 - (a + b)

    if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
      print(a*b*c)
      break