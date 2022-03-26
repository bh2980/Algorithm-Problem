a = int(input())

for i in range(1, a+1):
    # 나머지가 3, 6, 9이거나
    # 몫이 3, 6, 9이거나
    if (i//10 == 3 or i//10 == 6 or i//10 == 9) and (i%10 == 3 or i%10 == 6 or i%10 == 9) :
        print("XX", end=' ')
    elif i//10 == 3 or i//10 == 6 or i//10 == 9 :
        print("X", end=' ')
    elif i%10 == 3 or i%10 == 6 or i%10 == 9 :
        print("X", end=' ')
    else:
        print(i, end=' ')
