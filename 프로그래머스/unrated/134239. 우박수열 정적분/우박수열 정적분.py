def solution(k, ranges):
    answer = []
    cola = [k]
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        cola.append(k)
    print(cola)
    for a, b in ranges:
        if a > len(cola) + b - 1:
            answer.append(-1)
        else:
            z = 0
            for i in range(a, len(cola)+b-1):
                z += (cola[i] + cola[i+1]) / 2
            answer.append(z)
    return answer