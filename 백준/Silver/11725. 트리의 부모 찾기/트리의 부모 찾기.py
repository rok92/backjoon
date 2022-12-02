import sys
sys.setrecursionlimit(10**9)

def dfs(v):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      parent[i] = v
      dfs(i)

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
parent = [0 for _ in range(n+1)]


for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(1)
for i in range(2, len(parent)):
  print(parent[i])
