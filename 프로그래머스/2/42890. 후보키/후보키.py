from itertools import combinations
def solution(relation):
    row,col=len(relation),len(relation[0])
    temp,unique=[],[]
    for i in range(1,col+1):
        temp.extend(combinations(range(col),i))
    for i in temp:
        tmp=[tuple([item[x] for x in i]) for item in relation]
        if len(set(tmp))==row:
            unique.append(i)
    answer=set(unique)
    for i in range(len(unique)):
        for j in range(i+1,len(unique)):
            if len(unique[i])==len(set(unique[i])&set(unique[j])):
                answer.discard(unique[j])
    return len(answer)