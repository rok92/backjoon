def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

def solution(arr):
    arr.sort()
    answer = arr[0]
    for i in arr:
        answer = answer*i // gcd(answer, i)
    return answer