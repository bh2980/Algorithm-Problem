data = list(map(int, input()))

max = 0
start = 0
end = 13

# 13개씩 잘라서 곱한다.
# max와 비교해서 크면 넣는다.
for point in range(end, len(data)):
  numlist = data[start:point]

  print(numlist)
  
  gop = 1
  for number in numlist:
    gop *= number

  if max < gop:
    max = gop

  start += 1

print(max)