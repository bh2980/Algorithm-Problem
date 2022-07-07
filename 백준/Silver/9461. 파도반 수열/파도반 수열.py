T = int(input())

for _ in range(T):
  n = int(input())
  
  wave_triangle = [1 for _ in range(n+1)]

  if n >= 4:
    wave_triangle[4] = 2
    
    for i in range(5, n+1):
      wave_triangle[i] = wave_triangle[i-2] + wave_triangle[i-3]
  
  print(wave_triangle[n])