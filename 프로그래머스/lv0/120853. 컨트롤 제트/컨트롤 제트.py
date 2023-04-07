def solution(s):
    answer = []
    list_s = list(s.split(' '))
    for i in range(len(list_s)):
        if list_s[i] != "Z":
            answer.append(list_s[i])
        else:
            answer.remove(list_s[i-1])
    num_list = list(map(int, answer))
    return sum(num_list)