import sys
sys.setrecursionlimit(10**6)

def dfs(graph, v, visited) :
    visited[v] = True
    next_path = path[v]
    if not visited[next_path] : 
        dfs(graph, next_path, visited)

T = int(sys.stdin.readline())

for _ in range(T) :
    N = int(sys.stdin.readline())
    path = [0] + list(map(int, sys.stdin.readline().split()))
    graph = [[0] for _ in range(N+1)]
    visited = [True] + [False] * N
    A = 0
    for i in range(1, N+1) :
        if not visited[i] :
            dfs(graph, i, visited)
            A += 1
    print(A)
          