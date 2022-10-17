def binary_search(array, start, end, target) :
    while start <= end :
        mid = (start + end) // 2
        if array[mid] == target :
            return 1
        elif array[mid] > target :
            end = mid - 1
        else :
            start = mid + 1
    if start > end :
        return 0

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()
for i in B :
    print(binary_search(A, 0, N-1, i))