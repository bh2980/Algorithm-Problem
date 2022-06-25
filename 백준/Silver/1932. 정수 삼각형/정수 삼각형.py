def solution(n, arr):
  answer = [[] for _ in range(n)]

  answer[0].append(arr[0][0])
  answer[1].append(arr[0][0] + arr[1][0])
  answer[1].append(arr[0][0] + arr[1][1])

  for i in range(2, n):
    answer[i].append(answer[i-1][0] + arr[i][0])
    for j in range(0, len(answer[i-1]) - 1):
      base = answer[i-1][j] if answer[i-1][j] > answer[i-1][j+1] else answer[i-1][j+1]
      answer[i].append(base + arr[i][j+1])
    answer[i].append(answer[i-1][-1] + arr[i][-1])

  return max(answer[n-1])

if __name__ == '__main__':
  n = int(input())
  arr = []

  for _ in range(n):
    arr.append(list(map(int, input().split())))

  answer = solution(n, arr) if n > 1 else arr[0][0]
  print(answer)