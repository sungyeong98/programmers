def solution(k, room_number):
    answer,temp = [],{}
    for i in room_number:
        sv=[]
        while True:
            if i not in temp:
                temp[i]=i+1
                answer.append(i)
                if len(sv)>0:
                    for j in sv:
                        temp[j]=i+1
                break
            else:
                sv.append(i)
                i=temp[i]
    return answer