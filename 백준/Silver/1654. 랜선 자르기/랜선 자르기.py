import sys
def input():
    return sys.stdin.readline().rstrip()

def calcCutLopeCount(length_list, cut_length):
    answer = 0

    for lope in length_list:
        answer += lope // cut_length

    return answer

def binarySearch(start, end, target, length_list):
    mid = (start + end) // 2

    if start == mid: # start + 1 == end
        return mid

    cut_lope_count = calcCutLopeCount(length_list, mid)

    if cut_lope_count < target:
        # 자른 개수의 총 합이 목표 개수보다 작으므로, 길이를 줄여야한다. -> 작은 쪽 탐색
        return binarySearch(start, mid, target, length_list)
    elif cut_lope_count >= target:
        # 자른 개수의 총 합이 목표 개수보다 크므로, 길이를 늘려야한다 -> 큰 쪽 탐색
        # cut_lope_count가 target이 나와도 cut_length는 더 커질 수 있다. -> 같은 쪽 포함
        return binarySearch(mid, end, target, length_list)

def solution(k, target, length_list):
    # 주어진 끈 들은 동일한 길이로 잘라 목표 개수만큼 만들어야한다.

    # 길이와 목표 개수가 주어질 때, 목표 개수로 만들 수 있는 잘린 길이의 최대 길이를 구하시오

    # 2^31 - 1이므로 이진 탐색
    # max_int_length를 구해서 1~max_length 사이에서 이진 탐색을 수행한다.
    # 가운데 길이를 가져와서
    # 각자 로프에 대해 나눈 몫의 총합을 구함 -> 전체 잘린 개수를 의미함.
    # target보다 작다면, target을 못 채운 것이므로 길이를 줄여야한다. -> 작은 쪽 탐색
    # target보다 크다면, target을 채우고 남은 것이므로 길이를 늘려야한다. -> 큰 쪽 탐색

    # target과 같다면 일단 큰 쪽을 탐색해보고 안되면, 최댓값을 갱신한다.

    max_length = sum(length_list) // target

    start = 1
    end = max_length + 1

    return binarySearch(start, end, target, length_list)

k, target = map(int, input().split())
length_list = [int(input()) for _ in range(k)]

print(solution(k, target, length_list))