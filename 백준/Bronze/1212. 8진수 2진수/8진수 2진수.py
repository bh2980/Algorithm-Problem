def makeBinary(number):
  if number == 0:
    return '000'
  elif number == 1:
    return '001'
  elif number == 2:
    return '010'
  elif number == 3:
    return '011'
  elif number == 4:
    return '100'
  elif number == 5:
    return '101'
  elif number == 6:
    return '110'
  else:
    return '111'

octa = list(map(int, list(input())))
string = ''
for num in octa:
  string += makeBinary(num)

index = 0

while index < len(string) and string[index] == '0':
  index += 1

print(string[index:] if len(string[index:]) > 0 else 0)