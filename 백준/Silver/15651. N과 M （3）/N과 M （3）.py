stack = []

def DFS(N, M):
  if len(stack) == M:
    for num in stack:
      print(num, end=' ')
    print()

    return

  for index in range(1, N+1):
    stack.append(index)
    DFS(N, M)
    stack.pop()
    
if __name__ == '__main__':
  N, M = map(int, input().split())

  DFS(N, M)