def solution(jobs):
    answer,n,j,current_time = 0,len(jobs),sorted(jobs,key=lambda x:x[1]),0
    while j:
        for i in range(len(j)):
            if j[i][0]<=current_time:
                current_time+=j[i][1]
                answer+=current_time-j[i][0]
                j.pop(i)
                break
            if i==len(j)-1:
                current_time+=1
    return answer//n