def solution(targets):
    t=sorted(targets,key=lambda x:x[1])
    answer,temp = 0,-1
    for i in t:
        if i[0]>temp:
            answer+=1
            temp=i[1]-0.5
    return answer