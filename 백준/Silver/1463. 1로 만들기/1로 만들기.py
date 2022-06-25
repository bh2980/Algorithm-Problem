if __name__ == '__main__':
  n = int(input())
  step = [0] * (n+1)

  INF = 10e6 + 5
  
  for i in range(2, n+1):
    A = step[i // 3] if i % 3 == 0 else INF
    B = step[i // 2] if i % 2 == 0 else INF
    C = step[i - 1]

    step[i] = min(A, B, C) + 1

  print(step[n])