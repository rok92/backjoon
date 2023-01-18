def solution(sizes):
    answer = 0
    w_size = 0
    h_size = 0
    for i in range(len(sizes)):
        sizes[i].sort()
        w_size = max(w_size, sizes[i][0])
        h_size = max(h_size, sizes[i][1])
    answer = w_size * h_size
        
    return answer