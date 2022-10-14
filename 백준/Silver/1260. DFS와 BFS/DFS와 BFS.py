import sys
from collections import deque

def bfs(graph, s, visited) :
    q = deque([s])
    visited[s] = True
    while q : 
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v] :
            if not visited[i] :
                q.append(i)
                visited[i] = True
def dfs(graph, s, visited) : 
    visited[s] = True
    print(s, end=' ')
    for i in graph[s] : 
        if not visited[i] :
            dfs(graph, i, visited)
    

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for i in range(M) :
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1) :
    graph[i].sort()
visited = [False]*(N+1)

dfs(graph, V, visited)
print()

visited = [False]*(N+1)
bfs(graph, V, visited)
