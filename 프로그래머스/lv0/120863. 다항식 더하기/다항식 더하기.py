def solution(polynomial):
    a = (polynomial.replace(' ', '').split('+'))
    xcnt = 0
    num = 0
    for i in a:
        if 'x' in i:
            if len(i) > 1:
                xcnt += int(i[:-1])
            else:
                xcnt += 1
        else:
            num += int(i)
    if xcnt == 0:
        return '{}'.format(num)
    elif xcnt == 1:
        if num == 0:
            return 'x'
        else:
            return 'x + {}'.format(num)
    elif xcnt > 1:
        if num == 0:
            return '{}x'.format(xcnt)
        else:
            return '{}x + {}'.format(xcnt, num)
    

