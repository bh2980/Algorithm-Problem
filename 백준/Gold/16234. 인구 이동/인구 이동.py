
from collections import defaultdict, deque
def solution(N, L, R, country_map):
    # 한 칸에 한나라, 인구이동은 하루에 한 번
    # 두 나라 사이의 인구 차가 L 이상 R 이하이면, 국경선 OPEN
    # 국경선을 모두 연 다음에 인구 이동 시작
    # 국경선이 열린 나라들끼리 연합
    # 인구 이동 = 연합 인구 / 연합 이루는 나라 수 (소수점 버림)

    # 인구이동이 발생한 일자

    day = 0
    four_dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while True:
        country_line_count = 0

        # visited 따로 선언 후 방문한 나라 제외
        visited = [[False for _ in range(N)] for _ in range(N)]

        # 각 나라별로 열린 국경선 BFS로 탐색해서 연합 목록 만듬
        unions = []

        for r in range(N):
            for c in range(N):
                if visited[r][c]: #중복 방문 방지
                    continue

                union_people = 0
                union_list = []

                BFS_queue = deque([(r, c)])
                visited[r][c] = True

                while len(BFS_queue) > 0:
                    #나라 꺼내기
                    cr, cc = BFS_queue.popleft()

                    # 연합 인구에 더하기
                    union_people += country_map[cr][cc]
                    # 연합 목록에 추가
                    union_list.append((cr, cc))

                    # 상하좌우 나라 체크
                    for dr, dc in four_dir:
                        nr, nc = cr + dr, cc + dc

                        if not 0 <= nr < N or not 0 <= nc < N:  # 범위 밖이면 pass
                            continue

                        if visited[nr][nc]: # 방문했던 나라면 pass
                            continue

                        m_people = country_map[cr][cc]
                        o_people = country_map[nr][nc]

                        # 인구수가 적당히 차이나면 연합에 포함
                        if L <= abs(m_people - o_people) <= R:
                            # 방문 체크 (큐 중복 방지)
                            visited[nr][nc] = True
                            # 국경선 개수 + 1
                            country_line_count += 1
                            # BFS 큐에 추가
                            BFS_queue.append((nr, nc))

                # 인구수 // 길이 -> 리스트 나라 순회하면서 대입
                avg_people = union_people // len(union_list)

                #연합들에 추가
                unions.append([union_list, avg_people])

        # 열린 국경선 없으면 return day
        if country_line_count == 0:
            return day

        # 인구 분배
        for countries, avg_people in unions:
            for con_r, con_c in countries:
                country_map[con_r][con_c] = avg_people

        # 하루 종료
        day += 1

N, L, R = map(int, input().split())
country_map = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, L, R, country_map))