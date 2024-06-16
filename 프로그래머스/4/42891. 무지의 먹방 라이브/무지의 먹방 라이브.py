from heapq import heappop,heappush
def solution(food_times, k):
    answer,temp,food_num,previous_time = -1,[],len(food_times),0
    for idx,val in enumerate(food_times):
        heappush(temp,(val,idx+1))
    while temp:
        time=(temp[0][0]-previous_time)*food_num
        if k>=time:
            k-=time
            previous_time,_=heappop(temp)
            food_num-=1
        else:
            idx=k%food_num
            temp.sort(key=lambda x:x[1])
            answer=temp[idx][1]
            break
    return answer