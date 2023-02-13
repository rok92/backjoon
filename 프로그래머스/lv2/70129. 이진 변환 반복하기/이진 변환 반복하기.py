def solution(s):
    answer = []
    zero_c = 0
    count_up = 0
    while s != '1':
        if '0' in s:
            zero_c += s.count('0')
            s = s.replace('0', '')
            
        s = str(format(len(s), 'b'))
        count_up += 1
        
    answer.append(count_up)
    answer.append(zero_c)
    
    return answer