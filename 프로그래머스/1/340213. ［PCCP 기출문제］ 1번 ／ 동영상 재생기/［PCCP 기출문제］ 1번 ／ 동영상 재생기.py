def solution(video_len, pos, op_start, op_end, commands):
    total_time = minute_to_second(video_len)
    start = minute_to_second(op_start)
    end = minute_to_second(op_end)
    current_time = query_skip(minute_to_second(pos), start, end)
    
    for command in commands:
        if command == "next":   current_time = query_next(current_time, total_time)
        else:                   current_time = query_prev(current_time)
        current_time = query_skip(current_time, start, end)
    
    return second_to_minute(query_skip(current_time, start, end))

def minute_to_second(time):
    minute, second = time.split(":")
    return int(minute) * 60 + int(second)
    
def second_to_minute(time):
    minute = str(time // 60)
    second = str(time % 60)
    
    if len(minute) == 1:    minute = "0" + minute
    if len(second) == 1:    second = "0" + second
    return minute + ":" + second
    
def query_prev(time):
    return time - 10 if time - 10 >= 0 else 0

def query_next(time, end):
    return time + 10 if end - time >= 10 else end

def query_skip(time, start, end):
    return end if start <= time <= end else time