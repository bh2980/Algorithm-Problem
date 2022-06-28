def solution():
  T = int(input())

  for i in range(T):
    n, string = input().split()

    for char in string:
      print(char * int(n), end='')
    print()

solution()