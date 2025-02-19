def solution(schedules, timelogs, startday):
    n = len(schedules)
    cnt = 0
    
    for p, i in enumerate(timelogs):
        flag = True
        goal_time = time_to_min(schedules[p]) + 10
        for idx, timelog in enumerate(i):
            if ((idx + startday) % 7) == 6 or ((idx + startday) % 7) == 0:
                continue 
            if time_to_min(timelog) > goal_time:
                flag = False
                break
        if flag:    cnt+=1
        
    return cnt

def time_to_min(time_value):
    hour = time_value // 100
    minute = time_value % 100
    return hour * 60 + minute