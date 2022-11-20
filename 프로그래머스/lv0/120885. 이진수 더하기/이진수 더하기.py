def solution(bin1, bin2):
    answer = 0
    a = int(bin1, 2)
    b = int(bin2, 2)
    answer = format(a + b, 'b')
    
    return answer