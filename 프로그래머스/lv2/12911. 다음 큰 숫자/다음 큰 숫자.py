def solution(n):
    binary = format(n, 'b').count('1')
    while True:
        n += 1
        if binary == format(n, 'b').count('1'):
            break
    return n