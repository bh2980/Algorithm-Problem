stack = []

def DFS(start, N, M):
  if len(stack) == M:
    for num in stack:
      print(num, end=' ')
    print()

    return

  for index in range(start, N+1):
    stack.append(index)
    DFS(index, N, M)
    stack.pop()
    
if __name__ == '__main__':
  N, M = map(int, input().split())

  DFS(1, N, M)