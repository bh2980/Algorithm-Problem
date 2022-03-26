if __name__ == '__main__':
  date = int(input())
  consult = [[0, 0]]

  for _ in range(date):
    consult.append(list(map(int, input().split())))
    
  matrix = [[0] * (date+1) for _ in range(date+1)]

  for j in range(1, date + 1):
    for i in range(1, date + 1):
      first = matrix[i][j-1]
      score = consult[j][1] if consult[j][0] + j -1 <= i else 0
      second = matrix[j-1][j-1] + score
      matrix[i][j] = max(first, second)

  print(matrix[date][date])