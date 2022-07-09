n = int(input())

FIRST_START = 1
LAST_START = 2

winner = [FIRST_START for _ in range(n+1)]
try:
  winner[2] = LAST_START
except:
  pass

for i in range(5, n+1):
  if LAST_START in [winner[i-4], winner[i-3], winner[i-1]]:
    winner[i] = FIRST_START
  else:
    winner[i] = LAST_START

print('CY' if winner[n] == LAST_START else 'SK')