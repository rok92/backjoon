from collections import deque

def bfs(s, visited, tree):
    q = deque([s])
    ans = 1
    visited[s] = True
    while q:
        current = q.popleft()
        for i in tree[current]:
            if visited[i] == False:
                ans += 1
                q.append(i)
                visited[i] = True
    return ans


def solution(n, wires):
    answer = n
    tree = [[] for _ in range(n+1)]
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)
    for s, nv in wires:
        visited = [False] * (n+1)
        visited[nv] = True
        ans = bfs(s, visited, tree)
        if abs(ans - (n-ans)) < answer:
            answer =  abs(ans - (n-ans))
        
    return answer