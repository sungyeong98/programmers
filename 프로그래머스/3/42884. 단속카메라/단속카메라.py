def solution(routes):
    result = 0
    temp = float("-inf")    # 카메라 설치 위치
    r = sorted(routes, key = lambda x:x[1])     # 고속도로를 빠져나오는 시간을 기준으로 정렬
    
    for start, end in r:
        if temp < start:    # 카메라의 위치보다 현재 차량의 진입 위치가 크다면, 카메라를 해당 차량의 탈출 시점에 설치
            temp = end
            result += 1
    
    return result