import sys
from collections import deque

EAST = (0, 1)
WEST = (0, -1)
NORTH = (-1, 0)
SOUTH = (1, 0)

def printMap(MAP):
    for line in MAP:
        for char in line:
            print(char, end=' ')
        print()
    print()

def printDirection(dice):
    global EAST
    global WEST
    global SOUTH
    global NORTH

    if dice.direction == EAST:
        return 'EAST'
    if dice.direction == WEST:
        return 'WEST'
    if dice.direction == SOUTH:
        return 'SOUTH'
    if dice.direction == NORTH:
        return 'NORTH'

def printDice(dice):
    print(f'  {dice.NORTH}')
    print(f'{dice.WEST} {dice.TOP} {dice.EAST}')
    print(f'  {dice.SOUTH}')
    print(f'  {dice.BOTTOM}')

def input():
    return sys.stdin.readline().strip()

# N x M 지도 (0, 0)에 주사위가 위치
# 첫 방향 : 동쪽
# 처음 위 숫자 : 1, 동쪽 숫자 : 3

# 이동 방향으로 1칸 굴러감.
    # 이동 방향이 없다면 반대 방향으로 1칸 굴러감
# 점수 획득
    # 한 칸 움직인 후에 해당 칸의 숫자와 같은 숫자를 가진 인접한 칸의 개수를 구한다.
        # 칸의 개수 x 칸의 숫자 = 점수
        # 이동하지는 않는다.
# 아랫면에 있는 정수와 주사위가 있는 칸의 숫자를 비교해 이동 방향 결정
    # A > B라면, 이동 방향을 시계 방향으로 회전
    # A < B라면, 이동 방향을 반시계 방향으로 회전
    # A = B라면 이동방향 변화 X

# 점수의 누적 합 출력


# 주사위 구현
# 회전 방향에 따라 육면에 위치한 숫자를 변경해야함.
# 만약 동쪽으로 회전한다면, 상 -> 동, 동 -> 하, 하 -> 서, 서 -> 상
# 만약 서쪽으로 회전한다면, 상 -> 서, 서-> 하, 하 -> 동, 동 -> 상
# 만약 남쪽으로 회전한다면, 상 -> 남, 남 -> 하, 하 -> 북, 북 -> 상
# 만약 북쪽으로 회전한다면, 상 -> 북, 북 -> 하, 하 -> 남, 남 -> 상

class Dice:
    def __init__(self, MAP):
        self.TOP = 1
        self.BOTTOM = 6
        self.EAST = 3
        self.WEST = 4
        self.SOUTH = 5
        self.NORTH = 2
        self.direction = EAST

        self.location = (0, 0)

        self.score = 0

        self.N = len(MAP)
        self.M = len(MAP[0])

        return

    def roll(self):
        ci, cj = self.location
        di, dj = self.direction
        ni, nj = ci + di, cj + dj

        if 0 <= ni < self.N and 0 <= nj < self.M:
            pass
        else:
            self.direction = (-1 * di, -1 * dj)
            # print('방향 전환')

        di, dj = self.direction
        ni, nj = ci + di, cj + dj

        if self.direction == EAST:
            # print('동쪽으로 굴림')
            self.rollEast()
        elif self.direction == WEST:
            # print('서쪽으로 굴림')
            self.rollWest()
        elif self.direction == NORTH:
            # print('북쪽으로 굴림')
            self.rollNorth()
        elif self.direction == SOUTH:
            # print('남쪽으로 굴림')
            self.rollSouth()
        else:
            # print('Error')
            return

        self.location = (ni, nj)

    def rollEast(self):
        self.EAST, self.BOTTOM, self.WEST, self.TOP = self.TOP, self.EAST, self.BOTTOM, self.WEST

    def rollWest(self):
        self.WEST, self.BOTTOM, self.EAST, self.TOP = self.TOP, self.WEST, self.BOTTOM, self.EAST

    def rollNorth(self):
        self.NORTH, self.BOTTOM, self.SOUTH, self.TOP = self.TOP, self.NORTH, self.BOTTOM, self.SOUTH

    def rollSouth(self):
        self.SOUTH, self.BOTTOM, self.NORTH, self.TOP = self.TOP, self.SOUTH, self.BOTTOM, self.NORTH

def calcSameBlock(currentLocation, MAP, tileInfo):
    si, sj = currentLocation
    N = len(MAP)
    M = len(MAP[0])

    CURRENT_VALUE = MAP[si][sj]
    queue = deque([(si, sj)])
    visited_set = set([(si, sj)])

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    count = 1

    TEMP_ARRAY = []

    tileInfo[(si, sj)] = TEMP_ARRAY

    while len(queue) > 0:
        ci, cj = queue.popleft()

        for idx in range(4):
            ni, nj = ci + dx[idx], cj + dy[idx]

            if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in visited_set:
                if MAP[ni][nj] == CURRENT_VALUE:
                    count += 1
                    visited_set.add((ni, nj))
                    tileInfo[(ni, nj)] = TEMP_ARRAY
                    queue.append((ni, nj))

    TEMP_ARRAY.append(count)

    return count

def updateDice(dice, MAP, tileInfo):
    global EAST
    global WEST
    global SOUTH
    global NORTH

    ci, cj = dice.location
    MAP_SCORE = MAP[ci][cj]
    DICE_SCORE = dice.BOTTOM

    blockCount = 0

    # print('current location : ', (ci, cj), 'bottom : ', DICE_SCORE)

    if (ci, cj) in tileInfo:
        blockCount = tileInfo[(ci, cj)][0]
    else:
        blockCount = calcSameBlock((ci, cj), MAP, tileInfo)

    # print(f'{MAP_SCORE} * {blockCount} = {MAP_SCORE * blockCount}')
    dice.score += blockCount * MAP_SCORE

    if DICE_SCORE > MAP_SCORE:
        x, y = dice.direction
        dice.direction = (y, -x)
        # print(f'{DICE_SCORE} > {MAP_SCORE} / 시계 방향 회전')
    elif DICE_SCORE < MAP_SCORE:
        x, y = dice.direction
        dice.direction = (-y, x)
        # print(f'{DICE_SCORE} < {MAP_SCORE} / 반시계 방향 회전')
    else:
        # print(f'{DICE_SCORE} == {MAP_SCORE} / 회전 안함')
        pass

    return

def solution(N, M, K, MAP):
    global EAST
    global WEST
    global SOUTH
    global NORTH

    dice = Dice(MAP)
    tileInfo = dict()

    for _ in range(K):
        dice.roll()

        updateDice(dice, MAP, tileInfo)

        # print(f'{dice.location} / {printDirection(dice)} / {dice.score}')
        # printDice(dice)
        # print()

    return dice.score

N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

answer = solution(N, M, K, MAP)

print(answer)