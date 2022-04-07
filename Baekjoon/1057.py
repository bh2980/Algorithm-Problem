if __name__ == '__main__':
  num, A, B = map(int, input().split())
  list = [i for i in range(num + 1)]
  count = 0

  while A != B:
    if A > 1:
      A = A//2 if A % 2 == 0 else (A//2) + 1
    if B > 1:
      B = B//2 if B % 2 == 0 else (B//2) + 1

    count += 1

  print(count)