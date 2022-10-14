import sys
sys.setrecursionlimit(10**6)

def dfs(graph, v, visited) : 
    visited[v] = True
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)            

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

a = 0

for i in range(M) : 
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, N+1) :
    graph[i].sort()

visited = [False] *(N+1)
for i in range(1, N+1) :
    if visited[i] == False :
        a += 1
        dfs(graph, i, visited)
        
print(a)