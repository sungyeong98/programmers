def solution(s):
    answer = 0
    for i in range(0,len(s)):
        temp=''
        for j in range(i,len(s)):
            temp+=s[j]
            if temp==temp[::-1] and len(temp)>answer:
                answer=len(temp)
                
    return answer