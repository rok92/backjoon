def solution(my_string):
    my_string = ''.join([i if i.isdigit() else ' ' for i in list(my_string)])
    nlist = list(map(int, my_string.split()))
    answer = sum(nlist)
    return answer