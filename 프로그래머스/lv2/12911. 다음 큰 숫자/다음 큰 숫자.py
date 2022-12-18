def solution(n):
    binaryNum = format(n, 'b').count('1')
    while True:
        n += 1
        if binaryNum == format(n, 'b').count('1'):
            break
    return n