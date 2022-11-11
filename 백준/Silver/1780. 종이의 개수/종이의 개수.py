import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

zero = []
minus = []
plus = []

def cut(x, y, n) :
    check = paper[x][y]
    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if paper[i][j] != check :
                for a in range(3) :
                    for b in range(3) :
                        cut(x+n//3*a, y+n//3*b, n//3)
                return
    if check == 0 :
        zero.append(n)
    elif check == 1 :
        plus.append(n)
    else :
        minus.append(n)

cut(0, 0, N)
print(len(minus))
print(len(zero))
print(len(plus))
