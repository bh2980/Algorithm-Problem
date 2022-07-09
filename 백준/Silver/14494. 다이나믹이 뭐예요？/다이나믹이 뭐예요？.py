n, m = map(int, input().split())
map = [[1 for _ in range(m)] for _ in range(n)]

for i in range(1, n):
  for j in range(1, m):
    map[i][j] = (map[i-1][j] + map[i-1][j-1] + map[i][j-1]) % (1000000007)

print(map[n-1][m-1])