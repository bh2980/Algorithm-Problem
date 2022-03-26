if __name__ == '__main__':
  n = int(input())
  stairs = [int(input()) for _ in range(n)]
  
  score_arr = [[0, 0] for _ in range(n + 1)]

  score_arr[1][0] = stairs[0]
  score_arr[1][1] = stairs[0]

  if n >= 2:
    for i in range(2, n+1):
      score_arr[i][0] = max(score_arr[i-2][0], score_arr[i-2][1]) + stairs[i-1]
      
      score_arr[i][1] = score_arr[i-1][0] + stairs[i-1]

  print(max(score_arr[n][0], score_arr[n][1]))