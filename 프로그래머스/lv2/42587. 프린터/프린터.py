def solution(priorities, location):
    answer = 0
    idx = list(range(len(priorities)))
    idx[location] = 'target'
    while True:
        if priorities[0] == max(priorities):
            answer += 1
            
            if idx[0] == 'target':
                return answer
                break
            else:
                priorities.pop(0)
                idx.pop(0)
        else:
            priorities.append(priorities.pop(0))
            idx.append(idx.pop(0))
                
            
            
