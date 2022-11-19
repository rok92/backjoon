from collections import OrderedDict

def solution(my_string):
    answer = ''.join(OrderedDict.fromkeys(my_string))
    return answer