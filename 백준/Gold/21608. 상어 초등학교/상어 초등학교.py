class Seat:
  def __init__(self, point):
    self.point = point
    self.around = set()
    self.empty = 4
    self.student = None

class Student:
  def __init__(self, n, friends):
    self.number = n
    self.friends = set(friends)
    self.seat = None

def r0PreSetSeat(number, students, _class, empty_list, n):
  #탐색 범위를 줄이는 함수
  #친구가 앉아있다면 친구 주위의 상하좌우 자리 set을 return하는 함수
  #친구가 한 명도 앉아있지 않다면 빈자리 set을 return하는 함수
  
  r0_set = set()
  dx = [-1, 0, 0, 1]
  dy = [0, -1, 1, 0]

  for friend in students[number].friends:#number에 친구들에 대해서
    if students[friend].seat:#친구가 앉아있다면,
      for index in range(4):#친구 자리의 상좌우하 자리를 r0_set에 넣음.
        x, y = students[friend].seat
        nx, ny = x + dx[index], y + dy[index]

        if 0 < nx <= n and 0 < ny <= n and () and (nx, ny) in empty_list:
          r0_set.add((nx, ny))
      
  if len(r0_set) > 0:#r0_set에 값이 있다면 r0_set return
    return r0_set
  else:#r0_set에 값이 없다면 None return
    return empty_list
    
def r1r2MostFriendsEmpty(search_seat, friends, _class):
  #좋아하는 학생이 상하좌우에 가장 많은 자리 return하는 함수
  #자리 set을 받고, 상하좌우에 좋아하는 학생의 수를 기준으로 정렬
  #가장 많은 자리들을 return

  r1_dict = dict()
  max_val = -1

  for seat in search_seat:
    r1_dict[seat] = [len(_class[seat].around & friends), _class[seat].empty]
    if max_val < r1_dict[seat][0]:
      max_val = r1_dict[seat][0]

  r1_sort = sorted(r1_dict.items(), key=lambda x:x[1], reverse=True)
  r1_set = set()

  max_friends = r1_sort[0][1][0]
  max_empty = r1_sort[0][1][1]
  
  for key, value in r1_sort:
    friends, empty = value

    if friends == max_friends and empty == max_empty:
      r1_set.add(key)
    else:
      break

  return r1_set

def r3RowCol(search_row_col):
  #자리를 받아서 행->열 순으로 정렬
  #첫번째 성분 return
  return sorted(search_row_col)[0]

def updateSeat(number, seat, students, _class, empty_list, n):
  #students, _class, empty_list 업데이트 하는 함수
  
  students[number].seat = seat
  _class[seat].student = number
  
  empty_list.remove(seat)

  dx = [-1, 0, 0, 1]
  dy = [0, -1, 1, 0]

  for index in range(4):
    x, y = seat
    nx, ny = x + dx[index], y + dy[index]

    if 0 < nx <= n and 0 < ny <= n and (nx, ny) in empty_list:
      _class[(nx, ny)].empty -= 1
      _class[(nx, ny)].around.add(number)

def calcSatisfaction(students, _class, n):
  dx = [-1, 0, 0, 1]
  dy = [0, -1, 1, 0]
  satisfaction = 0

  for key, value in students.items():
    friends = value.friends
    seat = value.seat
    near_set = set()
    
    for index in range(4):
      x, y = seat
      nx, ny = x + dx[index], y + dy[index]
  
      if 0 < nx <= n and 0 < ny <= n:
        near_set.add(_class[(nx, ny)].student)

    near_friends = len(friends & near_set)

    if near_friends == 1:
      satisfaction += 1
    elif near_friends == 2:
      satisfaction += 10
    elif near_friends == 3:
      satisfaction += 100
    elif near_friends == 4:
      satisfaction += 1000

  return satisfaction

def solution():
  n = int(input())
  _class = dict([[(i+1, j+1), Seat((i+1, j+1))] for j in range(n) for i in range(n)])
  empty_list = set((i+1, j+1) for j in range(n) for i in range(n))
  students = dict()
  
  for i in range(n*n):
    stu, *friends = map(int, input().split())
    students[stu] = Student(stu, friends)

  for i in range(1, n+1):
    _class[(1, i)].empty -= 1
    _class[(n, i)].empty -= 1
    _class[(i, 1)].empty -= 1
    _class[(i, n)].empty -= 1

  for number in students.keys():
    r0_set = r0PreSetSeat(number, students, _class, empty_list, n)
    r1_set = r1r2MostFriendsEmpty(r0_set, students[number].friends, _class)
    seat = r3RowCol(r1_set)
    updateSeat(number, seat, students, _class, empty_list, n)
  
  print(calcSatisfaction(students, _class, n))

solution()