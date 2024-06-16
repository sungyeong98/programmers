def solution(m, n, startX, startY, balls):
    answer,temp = [],((-startX,startY),(startX,-startY),(m*2-startX,startY),(startX,n*2-startY))
    for x,y in balls:
        a=[]
        for ex,ey in temp:
            e=(x-ex)**2+(y-ey)**2
            s=(startX-ex)**2+(startY-ey)**2
            if not (x==startX==ex or y==startY==ey) or e>s:
                a.append(e)
        answer.append(min(a))
    return answer