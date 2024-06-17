def solution(scores):
    answer = 1
    temp,s,sv=scores[0],scores[1:],0
    for i,j in sorted(s,key=lambda x:(-x[0],x[1])):
        if temp[0]<i and temp[1]<j:
            return -1
        if sv<=j:
            sv=j
            if temp[0]+temp[1]<i+j:
                answer+=1
    return answer