def solution(r):
    answer,temp=0,-30001
    r.sort(key=lambda x:x[1])
    for i in r:
        if i[0]>temp:
            answer+=1
            temp=i[1]
    return answer