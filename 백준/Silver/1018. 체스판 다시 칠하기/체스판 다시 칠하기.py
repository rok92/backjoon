import sys

N, M = map(int, sys.stdin.readline().split())
insert = []
wcount = []

for _ in range(N) :
    insert.append(sys.stdin.readline().rstrip())

for i in range(N-7) :
    for j in range(M-7) :
        word_w = 0
        word_b = 0

        for x in range(i, i+8) :
            for y in range(j, j+8) :
                if(x+y) % 2 == 0 :
                    if insert[x][y] != 'B' :
                        word_b += 1
                    if insert[x][y] != 'W' :
                        word_w += 1
                else :
                    if insert[x][y] != 'W' :
                        word_b += 1
                    if insert[x][y] != 'B' :
                        word_w += 1
        wcount.append(word_w)
        wcount.append(word_b)
print(min(wcount))