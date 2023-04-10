from math import factorial

def solution(balls, share):
    answer = 0
    n = factorial(balls)
    m = factorial(share)
    n_m = factorial(balls-share)
    answer = n // (n_m * m)
    return answer