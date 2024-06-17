from collections import defaultdict
def solution(tickets):
    answer,temp,v = [],defaultdict(list),['ICN']
    for start,end in tickets:
        temp[start].append(end)
    for i in temp:
        temp[i].sort(reverse=True)
    while v:
        current=v[-1]
        if current not in temp or len(temp[current])==0:
            answer.append(v.pop())
        else:
            v.append(temp[current].pop())
    return answer[::-1]