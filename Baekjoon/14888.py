from itertools import permutations

def solution(num_arr, char_arr):
  per_arr = set(permutations(char_arr, len(char_arr)))

  max_val = -1000000001
  min_val = 1000000001

  for per in per_arr:
    eq = num_arr[0]
    for index in range(len(per)):
      eq = eval(eq + per[index] + num_arr[index+1])
      eq = str(int(eq))

    eq = int(eq)
    
    if min_val > eq:
      min_val = eq
      
    if max_val < eq:
      max_val = eq

  print(max_val, min_val, sep='\n')
  
if __name__ == '__main__':
  sym = ['+', '-', '*', '/']
  n = int(input())
  num_arr = input().split()
  temp = list(map(int, input().split()))
  char_arr = []
  
  for index in range(4):
    char_arr += [sym[index]] * temp[index]

  solution(num_arr, char_arr)