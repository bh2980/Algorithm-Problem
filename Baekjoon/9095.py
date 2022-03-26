count = 0

def recursion(n):
  global count
  
  if not n:
    count += 1
    return count

  for i in range(3, 0, -1):
    if n >= i:
      recursion(n-i)

for i in range(int(input())):
  recursion(int(input()))
  print(count)
  count = 0