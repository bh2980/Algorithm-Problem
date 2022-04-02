def drawLine(ineq_arr, target_arr):
  n = len(ineq_arr)
  
  if ineq_arr[n-1] == '>':
    target_arr[n] = 'B'
  else:
    target_arr[n] = 'R'

  prev = ''

  for i in range(n):
    if prev != ineq_arr[i]:
      if ineq_arr[i] == '<': # ><
        target_arr[i] = 'B'
      else:
        target_arr[i] = 'R'

    prev = ineq_arr[i]

def setNumber(target_arr, min_max):
  if min_max == 'max':
    num_set = [str(i) for i in range(9, 9-n-1, -1)]
    startLine = 'B'
    stopLine = 'R'
  else:
    num_set = [str(i) for i in range(n+1)]
    startLine = 'R'
    stopLine = 'B'

  i = n
  while num_set and i >= 0:
    if target_arr[i] == startLine:
      target_arr[i] = num_set.pop()
      
      index = i + 1
      while -1 < index <= n :
        if target_arr[index] == stopLine:
          target_arr[index] = num_set.pop()
          break
          
        target_arr[index] = num_set.pop()
        index += 1
      
      index = i - 1
      while -1 < index <= n and target_arr[index] != stopLine:
        target_arr[index] = num_set.pop()
        index -= 1

    i -= 1

  if num_set:
    target_arr[0] = num_set.pop()

  print(''.join(target_arr))


if __name__ == '__main__':
  n = int(input())
  ineq_arr = input().split()
  min_arr = [0] * (n+1)
  max_arr = [0] * (n+1)

  drawLine(ineq_arr, max_arr)
  drawLine(ineq_arr, min_arr)
  setNumber(max_arr, 'max')
  setNumber(min_arr, 'min')