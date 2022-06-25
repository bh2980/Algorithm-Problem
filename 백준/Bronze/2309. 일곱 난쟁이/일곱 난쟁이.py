stack = []

def solution(arr, index):
  L = len(stack)
  S = sum(stack)
  
  if L == 7 and S != 100:
    return False
  elif L == 7 and S == 100:
    return True
  else:
    for i in range(index+1, len(arr)):
      stack.append(arr[i])
      
      if solution(arr, i):
        break
      
      stack.pop()
  
if __name__ == '__main__':
  dwarfs = []

  for i in range(9):
    dwarfs.append(int(input()))

  solution(dwarfs, -1)
  
  for dwarf in sorted(stack):
    print(dwarf)