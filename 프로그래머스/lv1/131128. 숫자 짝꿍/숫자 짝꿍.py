def solution(X, Y):
    answer = []
    array = set(X) & set(Y)
    for i in array :
        for j in range(min(X.count(i), Y.count(i))) :
            answer.append(i)
    answer.sort(reverse = True)
    if len(answer) == 0 : return "-1"
    if answer[0] == "0" : return "0"
    return ''.join(answer)