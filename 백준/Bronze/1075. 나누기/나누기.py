def solution(n, f):
    max_n = int(str(n)[:-2] + '99')
    min_n = int(str(n)[:-2] + '00')

    for i in range(min_n, max_n + 1):
        if i % f == 0:
            return str(i)[-2:]

n = int(input())
f = int(input())

print(solution(n, f))