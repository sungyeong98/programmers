def solution(enroll, referral, seller, amount):
    money,temp,pp,parent=[],{},{},{}
    for i in amount:
        money.append(i*100)
    for i,j in zip(enroll,referral):
        pp[i]=0
        if j not in temp:
            temp[j]=[i]
        else:
            temp[j].append(i)
    for i,j in temp.items():
        for k in j:
            parent[k]=i
    for i,j in zip(seller,money):
        while j>0:
            if i=='-':
                break
            pp[i]+=j-j//10
            j=j//10
            i=parent.get(i)
    return list(pp.values())