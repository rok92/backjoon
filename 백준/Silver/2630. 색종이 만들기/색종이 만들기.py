N = int(input())
square = [list(map(int, input().split())) for _ in range(N)]
white = []
blue = []

def paper(x, y, n) :
    color = square[x][y]
    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if color != square[i][j] :
                paper(x, y, n//2)
                paper(x+n//2, y, n//2)
                paper(x, y+n//2, n//2)
                paper(x+n//2, y+n//2, n//2)
                return
    if color == 1 :
        blue.append(n)
    else :
        white.append(n)
    return

paper(0, 0, N)
print(len(white))
print(len(blue))