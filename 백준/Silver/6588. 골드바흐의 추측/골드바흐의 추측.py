def Goldbach(n, prime_set):
  for a in range(3, n//2 + 1):
    b = n - a
    if a in prime_set and b in prime_set:
      print('%d = %d + %d' % (n, a, b))
      return
      
if __name__ == '__main__':
  num_arr = []

  while True:
    n = int(input())
    if n == 0:
      break

    num_arr.append(n)

  max_val = max(num_arr)

  prime_set = set(i for i in range(2, max_val+1))

  for i in range(2, int(max_val**0.5) + 1):
    prime_set -= set(j for j in range(2*i, max_val + 1, i))

  for num in num_arr:
    Goldbach(num, prime_set)
    