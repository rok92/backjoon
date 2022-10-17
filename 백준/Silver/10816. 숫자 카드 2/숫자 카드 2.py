import sys
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value) :
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


N = int(sys.stdin.readline())
carda = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
cardb = list(map(int, sys.stdin.readline().split()))

carda.sort()
for i in range(len(cardb)) :
    print(count_by_range(carda, cardb[i], cardb[i]), end = ' ')