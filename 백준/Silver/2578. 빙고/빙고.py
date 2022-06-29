bingo = [list(map(int, input().split())) for _ in range(5)]
call = []
count = 0

for _ in range(5):
  call += list(map(int, input().split()))

rows = [set(row) for row in bingo]
cols = [set(bingo[i][j] for i in range(5)) for j in range(5)]
cross = [set(bingo[i][i] for i in range(5)), set(bingo[4-i][i] for i in range(5))]

for i in range(25):
  call_num = call[i]
  
  for j in range(5):
    try:
      rows[j].remove(call_num)
      if len(rows[j]) == 0:
        del rows[j]
        count += 1
    except:
      pass
      
    try:
      cols[j].remove(call_num)
      if len(cols[j]) == 0:
        del cols[j]
        count += 1
    except:
      pass
      
    try:
      if j < 2 :
        cross[j].remove(call_num)
        
      if len(cross[j]) == 0:
        del cross[j]
        count += 1
    except:
      pass

    if count >= 3:
      break

  if count >= 3:
    print(i + 1)
    break