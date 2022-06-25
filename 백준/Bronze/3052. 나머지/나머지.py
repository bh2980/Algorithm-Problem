if __name__ == '__main__':
  left = set()
  for i in range(10):
    num = int(input())
    left.add(num % 42)

  print(len(left))