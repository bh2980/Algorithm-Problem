from heapq import heappush, heappop
import sys

INSERT = 'I'
DELETE = 'D'

DELETE_MAX = 1
DELETE_MIN = -1

class Node:
    def __init__(self, value):
        self.value = value
        self.valid = True

def solution(operations):
    answer = []

    min_heap = []
    max_heap = []

    # operation 실행
    for operation in operations:
        oper, num = operation.split()
        num = int(num)

        if oper == INSERT:
            # 삽입 시, Node를 생성해서, min, max 힙에 넣는다.
            new_node = [num, True]
            heappush(min_heap, (num, new_node))
            heappush(max_heap, (-num, new_node))

        else:  # oper == DELETE
            if num == DELETE_MAX:
                # valid한 노드를 꺼낼 때까지 반복한다.
                # heap의 길이가 0보다 클 동안

                while len(max_heap) > 0:
                    order, pop_node = heappop(max_heap)
                    pop_value, pop_valid = pop_node

                    if pop_valid:
                        # valid하다면, invalid로 바꾼다.
                        pop_node[1] = False
                        break
            elif num == DELETE_MIN:
                while len(min_heap) > 0:
                    order, pop_node = heappop(min_heap)
                    pop_value, pop_valid = pop_node

                    if pop_valid:
                        pop_node[1] = False

                        break

    # answer 갱신

    # 최댓값 추가
    # while로 빼면서 valid한 값이 나오면 추가
    # 최솟값이 있다면 무조건 최댓값도 있음(같을수도)

    while len(max_heap) > 0:
        order, pop_node = heappop(max_heap)
        pop_value, pop_valid = pop_node

        if pop_valid and len(answer) == 0:
            answer.append(pop_value)
            break

    if len(answer) == 0:
        print('EMPTY')
        return

    # 최솟값 추가
    # while로 빼면서 valid한 값이 나오면 추가
    # 만약에 없으면, return [0, 0]

    while len(min_heap) > 0:
        order, pop_node = heappop(min_heap)
        pop_value, pop_valid = pop_node

        if pop_valid:
            answer.append(pop_value)
            break

    print(answer[0], answer[1])
    
T = int(input())

for _ in range(T):
    n = int(input())
    operation_list = []

    for _ in range(n):
        operation_list.append(sys.stdin.readline().rstrip())

    solution(operation_list)