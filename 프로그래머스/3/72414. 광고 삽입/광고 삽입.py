def convert_time_to_int(t):
    h,m,s=t.split(':')
    return int(h)*3600+int(m)*60+int(s)
def convert_time_to_str(t):
    h=t//3600
    h='0'+str(h) if h<10 else str(h)
    t=t%3600
    m=t//60
    m='0'+str(m) if m<10 else str(m)
    t=t%60
    s='0'+str(t) if t<10 else str(t)
    return h+':'+m+':'+s
def solution(play_time, adv_time, logs):
    play_time,adv_time=convert_time_to_int(play_time),convert_time_to_int(adv_time)
    time_line=[0 for _ in range(play_time+1)]
    for i in logs:
        start,end=i.split('-')
        start,end=convert_time_to_int(start),convert_time_to_int(end)
        time_line[start]+=1
        time_line[end]-=1
    for i in range(1,len(time_line)):
        time_line[i]+=time_line[i-1]
    for i in range(1,len(time_line)):
        time_line[i]+=time_line[i-1]
    max_view,max_time=0,0
    for i in range(adv_time-1,play_time):
        if i>=adv_time:
            if max_view<time_line[i]-time_line[i-adv_time]:
                max_view=time_line[i]-time_line[i-adv_time]
                max_time=i-adv_time+1
        else:
            if max_view<time_line[i]:
                max_view=time_line[i]
                max_time=i-adv_time+1
    return convert_time_to_str(max_time)