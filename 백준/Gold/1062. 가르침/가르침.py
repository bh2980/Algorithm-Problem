from itertools import combinations

def solution(n, k, word_list):
    # n개의 단어가 있고 k개의 글자를 가르칠 거임
    # 모든 단어는 anta로 시작하고, tica로 끝남.
    # 단어 내의 모든 글자를 알고 있다면 단어를 읽을 수 있음.
    # 1 <= n <= 50
    # 1 <= k <= 26
    # 영어 단어는 소문자로만 구성, 8 <= 길이 <= 15

    # 학생들이 읽을 수 있는 단어의 최댓값

    # a, n, t, i, c는 꼭 가르쳐야한다.
    # a, n, t, i, c는를 제외하고 k - 5개를 골라서 가장 많이 읽을 수 있는 단어의 수를 구해야 함.

    # 풀이
    # 각 단어가 가지고 있는 글자의 집합을 구한다. - a c i n t
    # 각 집합을 모두 합집합한 전체 글자 집합을 구한다.
    # 전체 글자 집합에서 k - 5개를 뽑는다.
    # 글자 조합에 대해서 몇 개의 글자를 배울 수 있는지 반복한다. -> 최댓값 갱신 (만약 전체 단어수와 같다면 return)

    # 비트 마스킹
    # 각 알파벳은 1 << (ord(char) - 96)

    # 제외 글자
    except_char_set = set(['a', 'c', 'i', 'n', 't'])

    # 각 단어가 가지고 있는 글자의 집합을 구한다.
    # 각 집합을 모두 합집합한 전체 글자 집합을 구한다.

    union_set = 0b0
    union_char_set = set()
    word_set_list = []

    for word in word_list:
        word_set = 0b0

        for char in word:
            if char in except_char_set:
                continue

            word_set |= 1 << (ord(char) - 96)
            union_char_set.add(char)

        word_set_list.append(word_set)

        union_set |= word_set

    # 가르칠 수 있는 글자가 없다.
    if k - 5 < 0:
        return 0

    # 모든 글자를 다 가르칠 수 있다.
    if len(union_char_set) <= k - 5:
        return n

    # 글자 조합에 대해서 몇개의 글자를 배울 수 있는지 반복한다. -> 최댓값 갱신 (만약 전체 단어수와 같다면 return)
    # 전체 글자 집합에서 k - 5개를 뽑는다.
    max_val = 0

    for combi in combinations(union_char_set, k - 5):
        count = 0
        combi_set = 0b0

        for char in combi:
            combi_set |= 1 << (ord(char) - 96)

        for word_set in word_set_list:
            if word_set & combi_set == word_set:
                count += 1

        max_val = max(max_val, count)

    return max_val

n, k = map(int, input().split())
word_list = [input() for _ in range(n)]

print(solution(n, k, word_list))