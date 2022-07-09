n, m = map(int, input().split())
blocks = [[0 for _ in range(m+1)]]

for _ in range(n):
  blocks.append([0] + list(map(int, input().split())))

for i in range(1, n+1):
  for j in range(1, m+1):
    blocks[i][j] = max(blocks[i-1][j], blocks[i][j-1]) + blocks[i][j]

print(blocks[i][j])