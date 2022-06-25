num_arr = []

while True:
  try:
    num_arr.append(int(input()))
  except:
    break

max_val = max(num_arr)
max_index = num_arr.index(max_val) + 1

print(max_val)
print(max_index)