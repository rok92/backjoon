def solution(elements):
    
    elementSet = set()
    doubleE = elements*2
    for i in range(len(elements)):
        for j in range(len(elements)):
            elementSet.add(sum(doubleE[j:j+i+1]))
    answer = len(elementSet)
    return answer