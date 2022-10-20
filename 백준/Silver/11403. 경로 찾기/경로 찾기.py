import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
graph = []

for _ in range(N) :
    graph.append(list(map(int, input().split())))

for k in range(N) :
   for a in range(N) :
       for b in range(N) :
           if graph[a][k] == 1 and graph[k][b] ==1 : 
              graph[a][b] = 1

for a in graph :
    for b in a :
        print(b, end = " ")
    print()