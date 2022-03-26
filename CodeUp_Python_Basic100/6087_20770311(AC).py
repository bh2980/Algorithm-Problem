a=int(input())
for i in range(1,a+1):
    if((i//10+i%10)%3!=0):print(i,end=' ')
