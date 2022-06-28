answer = [-1 for _ in range(26)]
string = input()

for i in range(len(string)):
  index = ord(string[i]) - 97
  if answer[index] == -1:
    answer[index] = i

print(*answer)