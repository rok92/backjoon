def solution(n):
    ans = 0
    while n > 0:
        k = n//2
        mod = n%2
        n = k
        if mod != 0:
            ans += 1
    return ans