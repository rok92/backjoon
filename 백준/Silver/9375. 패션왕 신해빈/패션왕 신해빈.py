T = int(input())
for _ in range(T) :
    ot = {}

    N = int(input())
    for _ in range(N) :
        a,b = input().split()
        if b not in ot.keys() :
            ot[b] = 1
        else :
            ot[b] += 1
    ans = 1
    for i in ot :
        ans *= (ot[i] + 1)
    print(ans-1)