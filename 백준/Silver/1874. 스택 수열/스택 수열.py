if __name__ == '__main__':
  string = []
  stack = []
  arr = []

  n = int(input())

  wait_list = [i for i in range(n, 0, -1)]

  for i in range(n):
    string.append(int(input()))

  string = string[::-1]

  stack.append(wait_list.pop())
  arr.append('+')

  while len(wait_list) or len(stack):
    if len(stack) == 0 or stack[-1] < string[-1]:
      num = wait_list.pop()
      stack.append(num)
      arr.append('+')
    elif stack[-1] == string[-1]:
      stack.pop()
      string.pop()
      arr.append('-')
    else:
      break

  if string == stack:
    for char in arr:
      print(char)
  else:
    print('NO')
  