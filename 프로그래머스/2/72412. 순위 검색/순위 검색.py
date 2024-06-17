from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    answer,temp = [],{}
    for i in info:
        i=i.split(' ')
        item=i[:-1]
        score=int(i[-1])
        for j in range(5):
            for k in combinations(item,j):
                tmp=''.join(k)
                if tmp not in temp:
                    temp[tmp]=[score]
                else:
                    temp[tmp].append(score)
    for i in temp:
        temp[i].sort()
    for i in query:
        i=i.replace(' and ',' ')
        i=i.split(' ')
        item=i[:-1]
        score=int(i[-1])
        while '-' in item:
            item.remove('-')
        tmp=''.join(item)
        if tmp in temp:
            scores=temp[tmp]
            if scores:
                cnt=bisect_left(scores,score)
                answer.append(len(scores)-cnt)
        else:
            answer.append(0)
    return answer