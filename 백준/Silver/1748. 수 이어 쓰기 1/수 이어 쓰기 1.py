if __name__ == '__main__':
  n = input()
  length = len(n)
  try:
    down_n = int("9" * (length - 1))
  except:
    down_n = 0
  ans = 0

  for i in range(1, length):
    try:
      ans += (int('9' * i) - int('9' * (i-1))) * i
    except:
      ans += int('9' * i) * i

  ans += (int(n) - down_n) * length

  print(ans)