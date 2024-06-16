def solution(n, l, r):
    answer = 0
    for i in range(l-1,r):
        def chk(n):
            if n%5==2:
                return False
            if n<5:
                return True
            return chk(n//5)
        if chk(i):
            answer+=1      
    return answer