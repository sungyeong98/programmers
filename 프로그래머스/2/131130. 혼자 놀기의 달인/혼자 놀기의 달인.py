def solution(cards):
    answer = 0
    chk=[0 for _ in range(len(cards))]
    score=[]
    for idx,num in enumerate(cards):
        if chk[idx]==0:
            cnt=1
            chk[idx]=1
            nidx=num-1
            while True:
                if chk[nidx]==0:
                    cnt+=1
                    chk[nidx]=1
                    nidx=cards[nidx]-1
                else:
                    break
            score.append(cnt)
    score.sort(reverse=True)
    if len(score)>1:
        answer=score[0]*score[1]
    else:
        answer=0
    return answer