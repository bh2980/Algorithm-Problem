from collections import deque
import sys

def input():
    return sys.stdin.readline().strip()

class Tree:
    def __init__(self, r, c, age):
        self.coordinate = (r, c)
        self.age = age

    def __lt__(self, other):
        if self.age <= other.age:
            return True
        else:
            return False

class GroundInfo:
    def __init__(self, r, c):
        self.coordinate = (r, c)
        self.food = 5
        self.alive_tree_list = deque()
        self.dead_tree_list = deque()

    def plantTree(self, tree):
        self.alive_tree_list.appendleft(tree)

    def growTree(self):
        origin_alive_tree_list = self.alive_tree_list
        new_alive_tree_list = deque()
        
        while len(origin_alive_tree_list) > 0:
            tree = origin_alive_tree_list.popleft()
            
            if tree.age <= self.food:
                self.food -= tree.age
                tree.age += 1
                new_alive_tree_list.append(tree)
            else:
                origin_alive_tree_list.appendleft(tree)
                break

        self.dead_tree_list = origin_alive_tree_list
        self.alive_tree_list = new_alive_tree_list

        return (len(self.alive_tree_list), len(self.dead_tree_list))

    def clearDeadTree(self):
        while len(self.dead_tree_list) > 0:
            tree_object = self.dead_tree_list.pop()
            self.food += (tree_object.age // 2)

def Autumn(ground, alive_tree_tile_set):
    # 살아있는 나무들 중 수명이 5인 아이들을 대상으로 주위에 나이가 1인 나무 추가

    n = len(ground)
    diff = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for r, c in alive_tree_tile_set:
        ground_info = ground[r][c]

        for tree in ground_info.alive_tree_list:
            if tree.age % 5 == 0:
                # 주위 8칸에 새 나무 심기
                for dr, dc in diff:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < n:
                        ground[nr][nc].plantTree(Tree(nr, nc, 1))

    return

def SpringSummgerWinter(ground, food_map):
    # 다른 타일에 영향을 미치지 않는 작업들은 한 번에
    n = len(ground)

    alive_tree_tile_set = set()

    for r in range(n):
        for c in range(n):
            if len(ground[r][c].alive_tree_list) > 0:
                #Spring
                alive_tree_count, dead_tree_count = ground[r][c].growTree()

                if alive_tree_count > 0:
                    alive_tree_tile_set.add((r, c))

                # Summer
                if dead_tree_count > 0:
                    ground[r][c].clearDeadTree()

            # Winter
            ground[r][c].food += food_map[r][c]

    return alive_tree_tile_set

def calcAliveTree(ground):
    count = 0

    for r in range(len(ground)):
        for c in range(len(ground)):
            count += len(ground[r][c].alive_tree_list)

    return count

def solution(n, m, k, food_map, tree_info):
    ground = [[GroundInfo(r, c) for c in range(n)] for r in range(n)]

    # 땅에 나무 심기
    for r, c, age in tree_info:
        # 땅에 나무를 심는다.
        r -= 1
        c -= 1

        ground[r][c].plantTree(Tree(r, c, age))

    for _ in range(k):
        alive_tree_tile_set = SpringSummgerWinter(ground, food_map)
        Autumn(ground, alive_tree_tile_set)

    return calcAliveTree(ground)

n, m, k = map(int, input().split())
food_map = [list(map(int, input().split())) for _ in range(n)]
tree_info = sorted([list(map(int, input().split())) for _ in range(m)], reverse = True)

print(solution(n, m, k, food_map, tree_info))