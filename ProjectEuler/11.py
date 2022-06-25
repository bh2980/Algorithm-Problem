def solution():
  prime_set = set(i for i in range(2, 2000000))

  for i in range(2, int(2000000*0.5) + 1):
    prime_set -= set(j for j in range(i*2, 2000000, i))

  print(sum(prime_set))

if __name__ == '__main__':
  solution()