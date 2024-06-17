def solution(n, k, cmd):
    answer = ''
    data={}
    dd=[]
    for i in range(n):
        a,b=i-1,i+1
        if i-1<0:
            a='null'
        if i+1>=n:
            b='null'
        data[i]=[a,b]
    for i in cmd:
        if i[0]=='D':
            move=int(i[2:])
            for j in range(move):
                k=data[k][1]
        elif i[0]=='U':
            move=int(i[2:])
            for j in range(move):
                k=data[k][0]
        elif i[0]=='C':
            dd.append(k)
            if data[k][1]!='null' and data[k][0]!='null':
                data[data[k][0]][1]=data[k][1]
                data[data[k][1]][0]=data[k][0]
            elif data[k][0]=='null':
                data[data[k][1]][0]='null'
            elif data[k][1]=='null':
                data[data[k][0]][1]='null'
            if data[k][1]=='null':
                k=data[k][0]
            else:
                k=data[k][1]
        elif i[0]=='Z':
            temp=dd.pop()
            if data[temp][0]!='null' and data[temp][1]!='null':
                data[data[temp][0]][1]=temp
                data[data[temp][1]][0]=temp
            elif data[temp][1]=='null':
                data[data[temp][0]][1]=temp
            elif data[temp][0]=='null':
                data[data[temp][1]][0]=temp
    chk={x:1 for x in dd}
    answer=''.join('X' if i in chk else 'O' for i in range(n))
    return answer