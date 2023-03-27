import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque()
for i in range(1, n+1):
  q.append(i)
arr = []
while q:
  for i in range(k-1):
    q.append(q.popleft())
  arr.append(q.popleft())
print(str(arr).replace('[', '<').replace(']', '>'))