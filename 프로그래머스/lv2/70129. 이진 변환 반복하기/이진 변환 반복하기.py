def solution(s):
    answer = []
    zero_c = 0
    count = 0
    while s != '1':
        if '0' in s:
            zero_c += s.count('0')
            s = s.replace('0', '')
            
        length = len(s)
        s = str(format(length, 'b'))
        count += 1
    
    answer.append(count)
    answer.append(zero_c)
    return answer