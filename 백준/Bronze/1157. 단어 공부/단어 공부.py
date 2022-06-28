def solution():
  string = input()
  if len(string) == 1:
    print(string.upper())
    return

  string = list(map(lambda x:x.upper(), list(string)))
    
  dictionary = dict([char, 0] for char in string)
  
  for char in string:
    dictionary[char] += 1
  
  dictionary = sorted(dictionary.items(), key = lambda x:x[1], reverse=True)
  
  print('?' if dictionary[0][1] == dictionary[1][1] else dictionary[0][0])

solution()