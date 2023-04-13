import sys

INF = float('inf')
def solution(n, cost_matrix):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            for k in range(n):
                if i == k or k == j:
                    continue

                prev_val = cost_matrix[j][k]
                next_val = cost_matrix[j][i] + cost_matrix[i][k]

                cost_matrix[j][k] = min(prev_val, next_val)

    for line in cost_matrix:
        for num in line:
            print(num if num != INF else 0, end=' ')
        print()

n = int(input())
bus = int(input())

cost_matrix = [[INF for j in range(n)] for i in range(n)]

for _ in range(bus):
    A, B, cost = map(int, sys.stdin.readline().rstrip().split())

    cost_matrix[A - 1][B - 1] = min(cost, cost_matrix[A - 1][B - 1])

solution(n, cost_matrix)