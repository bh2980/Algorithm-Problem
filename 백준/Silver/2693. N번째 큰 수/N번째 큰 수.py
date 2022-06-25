if __name__ == '__main__':
  num_arrs = [sorted(list(map(int, input().split()))) for _ in range(int(input()))]

  for num_arr in num_arrs:
    print(num_arr[-3])