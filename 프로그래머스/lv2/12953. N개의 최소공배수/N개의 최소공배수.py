from math import gcd

def solution(arr):
    arr.sort()
    answer = arr[0]
    
    for i in arr:
        answer = answer*i // gcd(answer, i)
    return answer