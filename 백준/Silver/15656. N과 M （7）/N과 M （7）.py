stack = []

def DFS(num_list, N, M):
  if len(stack) == M:
    for num in stack:
      print(num_list[num], end=' ')
    print()

    return

  for index in range(N):
    stack.append(index)
    DFS(num_list, N, M)
    stack.pop()
    
if __name__ == '__main__':
  N, M = map(int, input().split())
  num_list = list(map(int, input().split()))
  num_list.sort()

  DFS(num_list, N, M)