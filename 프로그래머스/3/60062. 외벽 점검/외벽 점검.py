from itertools import permutations
def solution(n, weak, dist):
    answer = len(dist)+1
    l=len(weak)
    for i in range(l):
        weak.append(weak[i]+n)
    for i in range(l):
        for j in list(permutations(dist,len(dist))):
            count=1
            temp=weak[i]+j[0]
            for k in range(i,i+l):
                if temp<weak[k]:
                    count+=1
                    if count>len(dist):
                        break
                    temp=weak[k]+j[count-1]
            answer=min(answer,count)
    if answer>len(dist):
        return -1
    return answer