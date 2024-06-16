def solution(words):
    idx,end = 0,len(words)
    w,chk=sorted(words),[0]*end
    while idx<end-1:
        for i in range(chk[idx],len(w[idx])):
            for j in range(idx,end):
                if i>=len(w[j]):
                    break
                if w[j][i]!=w[idx][i]:
                    break
                chk[j]+=1
                if j<end-1 and chk[j]>chk[j+1]+1:
                    break
            if chk[idx]>chk[idx+1]:
                break
        idx+=1
    return sum(chk)+1