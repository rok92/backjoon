def solution(priorities, location):
    answer = 0
    idx = list(range(len(priorities)))
    print(idx)
    while True:
        if priorities[0] == max(priorities):
            answer += 1
            
            if idx[0] == location:
                return answer
                break
            else:
                priorities.pop(0)
                idx.pop(0)
        else:
            priorities.append(priorities.pop(0))
            idx.append(idx.pop(0))
                
            
            
