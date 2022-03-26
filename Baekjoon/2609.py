def gcd(a, b):
  if b == 0:
    return a

  return gcd(b, a%b)

if __name__ == '__main__':
  A, B = map(int, input().split())

  if A < B:
    A, B = B, A

  G = gcd(A, B)
  L = A * B//G

  print(G)
  print(L)