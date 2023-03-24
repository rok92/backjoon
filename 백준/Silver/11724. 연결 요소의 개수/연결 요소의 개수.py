import sys
sys.setrecursionlimit(10**6)

n, m = map(int,sys.stdin.readline().split())
graph = [[0] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
answer = 0

for _ in range(m):
  x, y = map(int, sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(graph, v, visited):
  visited[v] = True
  for i in graph[v]:
    if visited[i] == False:
      dfs(graph, i, visited)

for i in range(1, n+1):
  if visited[i] == False:
    answer += 1
    dfs(graph, i, visited)

print(answer)