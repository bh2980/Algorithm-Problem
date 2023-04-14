import sys

n = int(input())
my_set = 0b0

for _ in range(n):
    instrction = sys.stdin.readline().rstrip().split()

    if len(instrction) == 2:
        inst, num = instrction
        num = int(num)

        if inst == 'add':
            # num을 표시하려면 num 번째 숫자를 1로 만들어서 기존과 합집합
            # 543210 : <- 방향으로 0번째부터
            my_set |= 1 << num # num번째에 저장
        elif inst == 'remove':
            # num 번쨰만 0이고 나머지는 1인 숫자를 교집합
            my_set &= ~(1 << num)
        elif inst == 'check':
            # 있는지 검사
            # 2 ^ num이 더해져있다는 소리
            # 교집합? -> 2 ^ num이면 되는거 아닌감?
            if my_set & (1 << num) == (1 << num):
                print(1)
            else:
                print(0)
        elif inst == 'toggle':
            if my_set & (1 << num) == (1 << num):
                my_set &= ~(1 << num)
            else:
                my_set |= 1 << num # num번째에 저장
    else:
        inst = instrction[0]
        if inst == 'all':
            my_set = 0b111111111111111111110
        elif inst == 'empty':
            my_set = 0b0
