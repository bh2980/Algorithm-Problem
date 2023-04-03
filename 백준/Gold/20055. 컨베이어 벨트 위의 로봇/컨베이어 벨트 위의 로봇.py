def solution(n, k, endurance):
    step = 0
    robot_location = [0] * (2 * n)
    OFF_LOCATION = n - 1
    ON_LOCATION = 0

    while k > 0:
        # 단계 시작
        step += 1

        # 벨트 이동
        last_element = endurance.pop()
        endurance.insert(0, last_element)

        last_robot = robot_location.pop()
        robot_location.insert(0, last_robot)

        # 내리는 위치 검사
        if robot_location[OFF_LOCATION]:
            robot_location[OFF_LOCATION] = 0

        # 로봇 이동
        for i in range(OFF_LOCATION - 1, -1, -1):
            #벨트 위 영역에 대해서 로봇이 있는 곳에서 로봇이 이동 가능하다면
            if robot_location[i] and not robot_location[i + 1] and endurance[i + 1] > 0:
                # 로봇 이동
                robot_location[i] = 0
                robot_location[i + 1] = 1
                endurance[i + 1] -= 1

                # 이동한 타일의 내구도가 0이면 k 감소
                if endurance[i + 1] == 0:
                    k -= 1

        # 내리는 위치 검사
        if robot_location[OFF_LOCATION]:
            robot_location[OFF_LOCATION] = 0

        if k <= 0:
            break

        # 시작 위치에 로봇을 올릴 수 있다면,
        if not robot_location[ON_LOCATION] and endurance[ON_LOCATION] > 0:
            robot_location[ON_LOCATION] = 1
            endurance[ON_LOCATION] -= 1

            # 로봇을 올린 타일의 내구도 검사
            if endurance[ON_LOCATION] == 0:
                k -= 1

    return step

n, k = map(int, input().split())
endurance = list(map(int, input().split()))

print(solution(n, k, endurance))