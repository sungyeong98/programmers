def solution(operations):
    answer = []
    temp=[]
    for i in operations:
        if "I" in i:
            temp.append(int(i[2:]))
        elif i=='D 1':
            if temp:
                del temp[temp.index(max(temp))]
        else:
            if temp:
                del temp[temp.index(min(temp))]
    if not temp or len(temp)==1:
        return [0,0]
    else:
        answer.append(max(temp))
        answer.append(min(temp))
    return answer