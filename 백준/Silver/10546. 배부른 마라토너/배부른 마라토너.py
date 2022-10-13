import sys

n = int(sys.stdin.readline().rstrip())
runner_record = set()

for i in range(2 * n - 1):
  runner = sys.stdin.readline().rstrip()

  if runner in runner_record:
    runner_record.remove(runner)
  else:
    runner_record.add(runner)

print(runner_record.pop())