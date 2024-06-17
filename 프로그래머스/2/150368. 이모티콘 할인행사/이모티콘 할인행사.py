from itertools import product
def solution(users, emoticons):
    rate=[10,20,30,40]
    r=list(product(rate,repeat=len(emoticons)))
    result=[]
    for i in r:
        total_people,total_money=0,0
        for j in users:
            sale,price=j
            total=0
            for ii,jj in zip(i,emoticons):
                if sale<=ii:
                    total+=int(jj*(100-ii)/100)
            if total>=price:
                total_people+=1
            else:
                total_money+=total
        result.append([total_people,total_money])
    result.sort(reverse=True,key=lambda x:(x[0],x[1]))
    return result[0]