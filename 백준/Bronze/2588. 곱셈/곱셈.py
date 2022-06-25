A, B = [input() for _ in range(2)]
total = 0
weight = 1

for num in B[::-1]:
  C = eval(A + '*' + num)
  print(C)
  total += C * weight
  weight *= 10
  
print(total)