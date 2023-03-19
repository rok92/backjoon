com = int(input())
conn = int(input())

graph = [[] for _ in range(com+1)]
visited = [False]*(com+1)

for _ in range(conn):
  a, b = map(int, input().split())
  graph[a] += [b]
  graph[b] += [a]

def dfs(v):
  visited[v] = 1
  for i in graph[v]:
    if visited[i] == 0:
      dfs(i)
dfs(1)
print(sum(visited)-1)