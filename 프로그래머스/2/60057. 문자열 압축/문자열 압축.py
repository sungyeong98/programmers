def solution(s):
    n = len(s)
    result = n
    
    for i in range(1, n):
        temp = list(map("".join, zip(*[iter(s)] * i)))
        if n % i !=0:
            temp.append(s[n - (n % i) :])
        
        total_word = ""
        cnt = 1
        
        for j in range(len(temp) - 1):
            if temp[j] == temp[j + 1]:      cnt += 1
            else:
                if cnt > 1:     total_word += str(cnt)
                total_word += temp[j]
                cnt = 1
        
        if cnt > 1:     total_word += str(cnt)
        total_word += temp[-1]
        result = min(result, len(total_word))
        
    return result