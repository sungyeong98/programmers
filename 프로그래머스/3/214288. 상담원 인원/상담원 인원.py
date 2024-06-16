from itertools import combinations_with_replacement,permutations
from heapq import heappush, heappop
def solution(k,n,reqs):
    answer=int(1e9)
    waiting_list=[[] for _ in range(k)]
    case_list=set()
    for start_time,end_time,consult_type in reqs:
        waiting_list[consult_type-1].append([start_time,start_time+end_time])
    for i in combinations_with_replacement([x for x in range(1,n-k+2)],r=k):
        if sum(i)==n:
            for j in permutations(i,k):
                case_list.add(j)
    def query_calculate_wait_time(waiting_list,people):
        total_time,heap=0,[]
        for _ in range(people):
            heappush(heap,0)
        for start_time,duration in waiting_list:
            prev_end=heappop(heap)
            if start_time>prev_end:
                heappush(heap,duration)
            else:
                wait_time=prev_end-start_time
                total_time+=wait_time
                heappush(heap,duration+wait_time)
        return total_time

    for i in case_list:
        time=0
        for j in range(k):
            time+=query_calculate_wait_time(waiting_list[j],i[j])
        answer=min(answer,time)
    return answer