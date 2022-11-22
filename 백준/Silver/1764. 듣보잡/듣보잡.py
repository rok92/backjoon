N, M = map(int, input().split())

listen = set()
see = set()

for i in range(N) :
    listen.add(input())
for i in range(M) :
    see.add(input())

complex = sorted(list(listen&see))
print(len(complex))
for i in complex :
    print(i)