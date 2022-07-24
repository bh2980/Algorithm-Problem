n = int(input())
char_dict = dict()

for _ in range(n):
  string = input()

  i = 0
  for char in string:
    if i in char_dict:
      if char_dict[i] != char:
        char_dict[i] = '?'
    else:
      char_dict[i] = char
    
    i += 1

print(''.join(char_dict.values()))