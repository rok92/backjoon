import sys
input = sys.stdin.readline
INF = int(1e9)

C = int(input()) # 컴퓨터갯수
L = int(input()) # 연결된 컴퓨터 갯수

graph = [[INF] * (C+1) for _ in range(C+1)]

count = 0
for a in range(1, C+1) :
    for b in range(1, C+1) :
        if a == b :
            graph[a][b] = 0
for _ in range(L) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
for k in range(1, C+1) :
    for a in range(1, C+1) :
        for b in range(1, C+1) :
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, C+1) :
    if graph[1][a] == INF or graph[1][a] == 0 :
        continue
    else :
        count += 1
print(count)
