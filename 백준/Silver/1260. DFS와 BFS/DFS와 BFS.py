from collections import deque
import sys

kk = sys.stdin.readline

def dfs(graph, s, visited):
  visited[s] = True
  print(s, end = ' ')
  for i in graph[s]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, s, visited):
  q = deque([s])
  visited[s] = True
  while q:
    a = q.popleft()
    print(a, end = ' ')
    for i in graph[a]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
  

n, m, v = map(int, kk().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
  w, e = map(int, kk().split())
  graph[w].append(e)
  graph[e].append(w)
for i in range(1, n+1):
  graph[i].sort()
visited = [False] * (n+1)
dfs(graph, v, visited)
print()

visited = [False] * (n+1)
bfs(graph, v, visited)
  