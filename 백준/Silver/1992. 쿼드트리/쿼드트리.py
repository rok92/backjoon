import sys

N = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

ans = ''

def video(x, y, N) :
    bw = a[x][y]
    global ans
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if bw != a[i][j] :
                ans += '('
                video(x, y, N//2)
                video(x, y+N//2, N//2)
                video(x+N//2, y, N//2)
                video(x+N//2, y+N//2, N//2)
                ans += ')'
                return
    if bw == 0 :
        ans += '0'
    else :
        ans += '1'
video(0, 0, N)
print(ans)