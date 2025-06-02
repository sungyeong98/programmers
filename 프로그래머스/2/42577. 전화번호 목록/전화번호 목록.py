def solution(phone_book):
    pb, n = sorted(phone_book), len(phone_book)     # 전화번호 목록을 사전순으로 정렬
    
    for i in range(1, n):
        # 이전의 번호와 비교하여 만약 현재 번호가 이전 번호로 시작을 한다면 false 반환
        if pb[i-1] == pb[i][:len(pb[i-1])]:    return False
    
    return True