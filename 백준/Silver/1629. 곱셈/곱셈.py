def Solution(L, B, C):
  if B == 1:
    return L % C

  d = Solution(L, B//2, C)

  d = d**2 if B % 2 == 0 else d**2 * (L%C)

  return d % C

if __name__ == '__main__':
  A, B, C = map(int, input().split())

  L = A % C

  print(Solution(L, B, C))
  