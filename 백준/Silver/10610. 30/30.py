if __name__ == '__main__':
  n = list(input())

  if '0' not in n:
    print(-1)
  elif sum(map(int, n)) % 3 != 0:
    print(-1)
  else:
    print(''.join(sorted(n, reverse = True)))