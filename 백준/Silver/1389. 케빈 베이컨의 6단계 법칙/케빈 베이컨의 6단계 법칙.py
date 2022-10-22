import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split()) # 유저, 관계의 수
graph = [[INF] * (N+1) for _ in range(N+1)]

for a in range(1, N+1) :
    for b in range(1, N+1) :
        if a == b:
            graph[a][b] = 0
for _ in range(M) :
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
    
for k in range(1, N+1) :
    for a in range(1, N+1) :
        for b in range(1, N+1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

num = 0
nums = []
for a in range(1, N+1) :
    for b in range(1, N+1) :
        if graph[a][b] == INF or graph[a][b] == 0 :
            continue
        else :
            num += graph[a][b]
    nums.append(num)
    num = 0
num = min(nums)
mini = nums.index(num)
print(mini + 1)
        
    
    