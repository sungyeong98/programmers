from itertools import chain
def solution(land, p, q):
    line=list(chain.from_iterable(land))
    line.sort()
    n=len(line)
    cost=(sum(line)-line[0]*n)*q
    answer=cost
    for i in range(1,n):
        if line[i]!=line[i-1]:
            cost=cost+((line[i]-line[i-1])*i*p)-((line[i]-line[i-1])*(n-i)*q)
            if answer<cost:
                break
            answer=min(answer,cost)
    return answer