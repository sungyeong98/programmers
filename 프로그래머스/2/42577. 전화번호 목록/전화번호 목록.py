def solution(phone_book):
    pb, n = sorted(phone_book), len(phone_book)
    
    for i in range(1, n):
        if pb[i-1] == pb[i][:len(pb[i-1])]:    return False
    
    return True