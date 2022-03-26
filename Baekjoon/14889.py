from itertools import combinations

def calTeamScore(team, matrix):
  sum = 0

  for i in range(0, len(team)):
    for j in range(i, len(team)):
      sum += matrix[team[i]][team[j]] + matrix[team[j]][team[i]]

  return sum

if __name__ == '__main__':
  matrix = []
  n = int(input())
  visited = []

  for i in range(n):
    matrix.append(list(map(int, input().split())))

  p_combi = combinations([i for i in range(n)], n//2)
  min_val = 99999

  for team in p_combi:
    if team not in visited:
      op_team = dict([(i, i) for i in range(n)])
      for mem in team:
        del(op_team[mem])

      diff = abs(calTeamScore(team, matrix) - calTeamScore(list(op_team), matrix))

      if diff < min_val:
        min_val = diff

  print(min_val)

      
      