import math

def solution(arr):
    return sum(arr) // len(arr) if sum(arr) % len(arr) == 0 else sum(arr) / len(arr)
    