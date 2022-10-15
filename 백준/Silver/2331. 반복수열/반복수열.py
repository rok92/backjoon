import sys

A, P = map(int, sys.stdin.readline().split())
D = [A]
K = 0


while True : 
    H = 0
    for i in list(str(D[K])) :
        H += int(i) ** P
    if D.count(H) >= 1 :
        break
    else :
        D.append(H)
    K += 1

H = 0
for j in list(str(D[-1])) :
    H += int(j) ** P
if D.index(H) != 0 :
    print(D.index(H))
else :
    print(0)