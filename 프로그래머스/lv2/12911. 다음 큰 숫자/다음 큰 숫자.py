def solution(n):
    _2jin = format(n, 'b').count('1')
    print(_2jin)
    while True:
        n += 1
        if _2jin == format(n, 'b').count('1'):
            break
    return n