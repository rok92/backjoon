import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
  command = sys.stdin.readline().split()
  # 각 경우의 수
  if command[0] == 'push':
    q.append(command[1])
  elif command[0] == 'pop':
    if q:
      print(q.popleft())
    else:
      print(-1)
  elif command[0] == 'size':
    print(len(q))
  elif command[0] == 'empty':
    if len(q) == 0:
      print(1)
    else:
      print(0)
  elif command[0] == 'front':
    if not q:
      print(-1)
    else:
      print(q[0])
  else:
    if not q:
      print(-1)
    else:
      print(q[-1])