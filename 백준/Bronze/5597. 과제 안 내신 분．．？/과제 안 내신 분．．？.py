submit = set()
all = set([i for i in range(1, 31)])

for i in range(28):
  submit.add(int(input()))

print(min(all-submit))
print(max(all-submit))