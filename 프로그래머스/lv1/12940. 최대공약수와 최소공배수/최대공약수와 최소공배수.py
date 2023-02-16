def solution(n, m):
    a = n
    b = m
    
    while m%n:
        r = m%n
        m = n
        n = r
    return [n, a*b/n]