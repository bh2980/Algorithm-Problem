import sys

def solution(gears, rot_count, rot_way):
  # 서로 마주 보는 극이 다르면 상대 기어는 반대 방향으로 회전
  # 서로 마주 보는 극이 같다면 상대 기어는 회전하지 않음

  # 12시 방향이 N극이면 0, S극이면 1의 합을 2**번째와 곱해서 return

  pointer = [0, 0, 0, 0]
  
  # 시계방향으로 돌리면 p를 -1
  # 반시계방향으로 돌리면 p를 +1

  for nth, dir in rot_way:
    #모든 기어의 pointer 기준으로 +2번과 +6번을 뽑는다
    nth -= 1
    dir *= -1

    right_gear = []
    left_gear = []

    for i in range(4):
      right_target_pointer = pointer[i] + 2 if pointer[i] + 2 < 8 else (pointer[i] + 2) % 8
      left_target_pointer = pointer[i] + 6 if pointer[i] + 6 < 8 else (pointer[i] + 6) % 8
      
      right_gear.append(gears[i][right_target_pointer])
      left_gear.append(gears[i][left_target_pointer])

    pointer[nth] += dir

    # dir의 방향을 톱니마다 바꿔줌
    temp_dir = dir

    # nth를 기준으로 오른쪽으로 가는 아이들은 왼6과 오2를 비교
    for i in range(nth, 3):
      if right_gear[i] != left_gear[i+1]: #둘이 다른 극이라면
        pointer[i+1] -= temp_dir
        temp_dir *= -1
      else:
        break

    temp_dir = dir

    # 왼쪽으로 가는 아이들은 왼2와 오6을 비교
    for i in range(nth, 0, -1):
      if left_gear[i] != right_gear[i-1]:
        pointer[i-1] -= temp_dir
        temp_dir *= -1
      else:
        break

    # pointer 순환처리
    for i in range(4):
      if pointer[i] < 0:
        pointer[i] = 7

      if pointer[i] > 7:
        pointer[i] = 0

  return sum([gears[i][pointer[i]] * (2 ** i) for i in range(4)])

def input():
  return sys.stdin.readline().rstrip()
  
gears = [list(map(int, list(input()))) for _ in range(4)]

rot_count = int(input())
rot_way = [list(map(int, input().split())) for _ in range(rot_count)]

answer = solution(gears, rot_count, rot_way)

print(answer)