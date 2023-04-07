def solution(dots):
    answer = 0
    x = []
    y = []
    
    for i in dots:
        x.append(i[0])
        y.append(i[1])
    print(x)
    print(y)
    t1 = (x[0]-x[1])/(y[0]-y[1])
    t2 = (x[2]-x[3])/(y[2]-y[3])
    t3 = (x[0]-x[2])/(y[0]-y[2])
    t4 = (x[1]-x[3])/(y[1]-y[3])
    t5 = (x[0]-x[3])/(y[0]-y[3])
    t6 = (x[1]-x[2])/(y[1]-y[2])
    if t1 == t2 or t3 == t4 or t5 == t6:
        return 1
    return 0
    #t1 = (dots[0][0]-dots[1][0])/(dots[0][1]-dots[1][1])
    #t2 = (dots[2][0]-dots[3][0])/(dots[2][1]-dots[3][1])
    #t3 = (dots[0][0]-dots[2][0])/(dots[0][1]-dots[2][1])
    #t4 = (dots[1][0]-dots[3][0])/(dots[1][1]-dots[3][1])
    #t5 = (dots[0][0]-dots[3][0])/(dots[0][1]-dots[3][1])
    #t6 = (dots[1][0]-dots[2][0])/(dots[1][1]-dots[2][1])
    #if t1 == t2 or t3 == t4 or t5 == t6:
    #    return 1
    #return 0
    
        
