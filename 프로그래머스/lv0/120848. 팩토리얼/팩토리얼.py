import math

def solution(n):
    answer = 0
    arr = []
    for i in range(1,11):
        arr.append(math.factorial(i))
    print(arr)
    for i in range(len(arr)):
        if n == arr[i]:
            return i+1
        elif n > arr[i] and n < arr[i+1]:
            return i+1