def solution(stars, row, col, N):
  if N == 1:
    return

  div = N // 3

  #행렬 3등분
  row = [row, row+div, row+div*2]
  col = [col, col+div, col+div*2]

  #가운데를 비우는 코드
  for dx in range(row[1], row[2]):
    for dy in range(col[1], col[2]):
      stars[dy][dx] = ' '

  #등분한 배열 재귀적 호출
  for dx in row:
    for dy in col:
      solution(stars, dx, dy, div)

if __name__ == '__main__':
  N = int(input())
  stars = [['*'] * N for i in range(N)]

  solution(stars, 0, 0, N)

  #출력 코드
  for i in stars:
    for j in i:
      print(j, end='')
    print()