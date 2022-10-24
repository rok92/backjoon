import sys

N, M = map(int, sys.stdin.readline().split())
poketmon = []
poke = {}

for i in range(N) :
    p = sys.stdin.readline().rstrip()
    poketmon.append(p)
    poke[p] = i + 1

for _ in range(M) :
    result = sys.stdin.readline().rstrip()
    if result.isdigit() :
        print(poketmon[int(result)-1])
    else :
        print(poke[result])