def solution(id_list, report, k):
    answer = []
    r=list(set(report))
    ban={}
    for i in r:
        a=i.split(' ')
        if a[1] in ban:
            ban[a[1]]+=1
        else:
            ban[a[1]]=1
    info={}
    for i in r:
        a=i.split(' ')
        if a[0] not in info:
            if ban[a[1]]>=k:
                info[a[0]]=1
            else:
                info[a[0]]=0
        else:
            if ban[a[1]]>=k:
                info[a[0]]+=1
    for i in id_list:
        if i not in info:
            answer.append(0)
        else:
            answer.append(info[i])
        
    return answer