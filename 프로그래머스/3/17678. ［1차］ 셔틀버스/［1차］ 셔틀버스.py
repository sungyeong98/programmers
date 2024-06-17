def solution(n, t, m, timetable):
    answer = ''
    start=540
    temp=[]
    for i in timetable:
        if i!='23:59':
            ti=int(i[:2])*60+int(i[3:])
            temp.append(ti)
    temp.sort()
    chk=start
    cnt=0
    p=0
    while chk<=start+(n*t)-1:
        if len(temp)>0 and cnt<m and p<len(temp) and temp[p]<=chk:
            p+=1
            cnt+=1
        else:
            chk+=t
            if chk>start+(n*t)-1:
                chk-=t
                break
            cnt=0
    
    if cnt<m:
        a=chk
        h=str(a//60) if a//60>=10 else '0'+str(a//60)
        m=str(a%60) if a%60>=10 else '0'+str(a%60)
        answer=h+':'+m
    else:
        a=temp[p-1]-1
        h=str(a//60) if a//60>=10 else '0'+str(a//60)
        m=str(a%60) if a%60>=10 else '0'+str(a%60)  
        answer=h+':'+m
    return answer