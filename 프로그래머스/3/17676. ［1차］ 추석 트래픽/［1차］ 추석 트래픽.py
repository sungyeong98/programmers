def cal_time(t):
    h,m,s,ms=t[:2],t[3:5],t[6:8],t[9:]
    return (int(h)*3600+int(m)*60+int(s))*1000+int(ms)
def solution(lines):
    answer = 0
    time_s,time_e=[],[]
    for i in lines:
        i=i[11:].split(' ')
        end_time=cal_time(i[0])
        start_time=end_time-int(float(i[1][:-1])*1000)+1
        time_s.append(start_time)
        time_e.append(end_time)
    for i in range(len(lines)):
        current_time,cnt=time_e[i],0
        for j in range(i,len(lines)):
            if current_time>time_s[j]-1000:
                cnt+=1
            answer=max(answer,cnt)
    return answer