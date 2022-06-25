h, m = map(int, input().split())
add_m = int(input())

m += add_m

print((h + m//60) % 24 if (h + m//60) >= 24 else (h + m//60), m%60)