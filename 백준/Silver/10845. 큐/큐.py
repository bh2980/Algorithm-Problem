from collections import deque
import sys

queue = deque()

def qInst(inst):
  if inst == 'pop':
    return queue.popleft() if queue else -1
  elif inst == 'size':
    return len(queue)
  elif inst == 'empty':
    return 0 if queue else 1
  elif inst == 'front':
    return queue[0] if queue else -1
  elif inst == 'back':
    return queue[-1] if queue else -1
  else:
    push, n = inst.split()
    queue.append(n)

n = int(input())
for i in range(n):
  ret = qInst(sys.stdin.readline().rstrip())
  if ret != None:
    print(ret)