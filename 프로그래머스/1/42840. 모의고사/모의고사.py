def solution(answers):
    temp1 = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
    temp2 = {0: 2, 1: 1, 2: 2, 3: 3, 4: 2, 5: 4, 6: 2, 7: 5}
    temp3 = {0: 3, 1: 3, 2: 1, 3: 1, 4: 2, 5: 2, 6: 4, 7: 4, 8: 5, 9: 5}
    result = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == temp1[i % 5]: result[0]+=1
        if answers[i] == temp2[i % 8]: result[1]+=1
        if answers[i] == temp3[i % 10]: result[2]+=1
    
    return [idx + 1 for idx, val in enumerate(result) if max(result) == val]