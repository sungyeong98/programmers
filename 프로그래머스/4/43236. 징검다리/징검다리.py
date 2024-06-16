def solution(distance, rocks, n):
    answer = 0
    start,end=0,distance
    rocks.sort()
    rocks.append(distance)
    while start<=end:
        mid=(start+end)//2
        current,cnt=0,0
        for i in rocks:
            if i-current<mid:
                cnt+=1
            else:
                current=i
        if cnt>n:
            end=mid-1
        else:
            answer=mid
            start=mid+1
    return answer