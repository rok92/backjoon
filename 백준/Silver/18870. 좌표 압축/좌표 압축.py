import sys

N = int(sys.stdin.readline())
qq = list(map(int, sys.stdin.readline().split()))
dic = {}

sq = sorted(set(qq))

for i in range(len(sq)) :
    dic[sq[i]] = i
for i in qq :
    print(dic[i], end=" ")