from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y) :
    queue = deque()
    queue.append((x, y))

    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                continue
            if field[nx][ny] == 1 :
                field[nx][ny] = 0
                queue.append((nx, ny))
    return True

for _ in range(T) :
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]

    for _ in range(K) :
        x, y = map(int, input().split())
        field[y][x] = 1
    ans = 0
    for x in range(N) :
        for y in range(M) :
            if field[x][y] == 1 :
                bfs(x, y)
                ans += 1
    print(ans)
