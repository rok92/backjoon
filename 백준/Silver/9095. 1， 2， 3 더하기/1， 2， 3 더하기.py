def plus(N) :
    if N == 1 :
        return 1
    elif N == 2 :
        return 2
    elif N == 3 :
        return 4
    else :
        return plus(N-1) + plus(N-2) + plus(N-3)

T = int(input())
for i in range(T) :
    N = int(input())
    print(plus(N))