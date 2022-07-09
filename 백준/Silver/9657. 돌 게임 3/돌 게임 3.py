n = int(input())

winner = ['SK' for _ in range(n+1)]
try:
  winner[2] = 'CY'
except:
  pass

for i in range(5, n+1):
  if 'CY' in [winner[i-4], winner[i-3], winner[i-1]]:
    winner[i] = 'SK'
  else:
    winner[i] = 'CY'

print(winner[n])