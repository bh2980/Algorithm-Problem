# def drawMap(fireball_location, n):
#     draw_map = [[[] for _ in range(n)] for _ in range(n)]
#
#     for point, fireball_list in fireball_location.items():
#         for fireball in fireball_list:
#             i, j, = point
#             draw_map[i][j].append(fireball.mass)
#
#     for i in range(n):
#         for j in range(n):
#             if len(draw_map[i][j]) > 0:
#                 print('%10s' % ','.join(map(str, draw_map[i][j])), end='|')
#             else:
#                 print('%10s' % ' ', end= '|')
#         print()
#     print('----------------------------------------------')
#
#     # for line in draw_map:
#     #     print(line)
#     # print()


from collections import defaultdict

DIRECTION = dict([[0, (-1, 0)], [1, (-1, 1)], [2, (0, 1)], [3, (1, 1)], [4, (1, 0)], [5, (1, -1)], [6, (0, -1)], [7, (-1, -1)]])

class Fireball:
    def __init__(self, mass, direction, speed):
        self.mass = mass
        self.direction = direction
        self.speed = speed

def solution(n, m, k, fireball_info_list):
    # 파이어볼이 있는 좌표
    # 여기서 좌표를 pop해서 fireball 정보에 맞게 이동시킨 후 다시 넣는다
    fireball_location = defaultdict(lambda : [])

    for info in fireball_info_list:
        r, c, m, s, d = info
        fireball_location[(r - 1, c - 1)].append(Fireball(m, d, s))

    # k번 반복 while
    while k > 0:
        # 파이어볼 이동
        move_fireball_location = defaultdict(lambda : [])

        # fireball_location에서 좌표와 파이어볼 list를 꺼낸다
        for point, fireball_list in fireball_location.items():
            # 파이어볼 리스트에서 파이어볼을 pop하고 이동시킨다.
            # 이동한 곳에서 다시 이동하는건 안됨. -> 다시 만든다

            while len(fireball_list) > 0:
                fireball = fireball_list.pop()

                dr, dc = DIRECTION[fireball.direction]
                fr, fc = point

                nr, nc = (fr + dr * fireball.speed) % n, (fc + dc * fireball.speed) % n

                if nr < 0:
                    nr += n
                elif nr >= n:
                    nr -= n

                if nc < 0:
                    nc += n
                elif nc >= n:
                    nc -= n

                # 새로운 좌표에 추가한다.
                move_fireball_location[(nr, nc)].append(fireball)

        # 2개 이상 있는 파이어볼 처리
        for point, fireball_list in move_fireball_location.items():
            if len(fireball_list) < 2:
                continue
            # 내부의 파이어볼들을 분리하거나 소멸시킨다.

            total_mass = 0
            total_speed = 0
            odd_count = 0
            even_count = 0

            while len(fireball_list) > 0:
                fireball = fireball_list.pop()

                total_mass += fireball.mass
                total_speed += fireball.speed
                if fireball.direction % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1

            each_mass = total_mass // 5
            each_speed = total_speed // (odd_count + even_count)

            if each_mass == 0: # 질량이 0이면 무시
                continue

            # 방향 구분
            each_dir = [0, 2, 4, 6] if even_count == 0 or odd_count == 0 else [1, 3, 5, 7]

            # 4개 생성 후 point에 삽입
            for i in range(4):
                move_fireball_location[point].append(Fireball(each_mass, each_dir[i], each_speed))

        # 업데이트
        fireball_location = move_fireball_location
        k -= 1  # 횟수 감소

    mass_list = []
    for fireball_list in fireball_location.values():
        for fireball in fireball_list:
            mass_list.append(fireball.mass)

    return sum(mass_list)


n, m, k = map(int, input().split())
fireball_info_list = [list(map(int, input().split())) for _ in range(m)]

print(solution(n, m, k, fireball_info_list))