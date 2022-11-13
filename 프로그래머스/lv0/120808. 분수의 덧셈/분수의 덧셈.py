import math

def solution(denum1, num1, denum2, num2):
    son = denum1*num2 + denum2*num1
    mom = num1*num2
    n = math.gcd(son, mom)
    if n == 1 :
        return [son, mom]
    else :
        return [son/n, mom/n]