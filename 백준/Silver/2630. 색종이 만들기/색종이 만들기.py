N = int(input())
square = [list(map(int, input().split())) for _ in range(N)]
result = []

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
        result.append(1)
    else :
        result.append(0)
    return

paper(0, 0, N)
print(result.count(0))
print(result.count(1))       