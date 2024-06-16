def solution(s):
    answer = []
    for i in s:
        temp=[]
        cnt,idx=0,-1
        for j in i:
            temp.append(j)
            while len(temp)>2 and temp[-1]=='0' and temp[-2]=='1' and temp[-3]=='1':
                cnt+=1
                temp.pop()
                temp.pop()
                temp.pop()
        for k in range(len(temp)-1,-1,-1):
            if temp[k]=='0':
                idx=k+1
                break
        else:
            answer.append('110'*cnt+''.join(temp))
            continue
        a=''.join(temp)
        answer.append(a[:idx]+'110'*cnt+a[idx:])
    return answer