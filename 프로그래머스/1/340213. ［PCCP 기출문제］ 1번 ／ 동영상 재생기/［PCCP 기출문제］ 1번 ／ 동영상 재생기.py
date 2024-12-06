def solution(video_len, pos, op_start, op_end, commands):
    video_len, pos, op_start, op_end = convert(video_len), convert(pos), convert(op_start), convert(op_end)
    
    if op_start<=pos<=op_end:
        pos=op_end
    
    for i in commands:
        if i=='next':
            pos+=min(10, video_len-pos)
        if i=='prev':
            pos-=min(10, pos)
        if op_start<=pos<=op_end:
            pos=op_end
    
    minute, second = str(pos//60), str(pos%60)
    
    if len(minute)==1:
        minute = "0"+minute
    if len(second)==1:
        second = "0"+second
    return minute + ":" + second
    
def convert(time):
    minute, second = time.split(':')
    return int(minute)*60 + int(second)
    