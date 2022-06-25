if __name__ == '__main__':
  T = int(input())

  for i in range(T):
    num = int(input())
  
    for index in range(len(bin(num))):
      if bin(num)[::-1][index] == '1':
        print(index, end=' ')
    print()