def solution(number, k):
    temp = []
    
    for num in number:
        while temp and temp[-1] < num and k > 0:
            temp.pop()
            k -= 1
        temp.append(num)
    
    return "".join(temp) if k == 0 else "".join(temp[:-k])