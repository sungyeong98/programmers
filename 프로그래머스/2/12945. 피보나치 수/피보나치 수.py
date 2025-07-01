def solution(n):
    temp = [0, 1, 1]
    
    while len(temp) < n + 1:
        temp.append(temp[-1] + temp[-2])
    
    return temp[-1] % 1234567