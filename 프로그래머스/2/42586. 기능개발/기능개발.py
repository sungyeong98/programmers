def solution(progresses, speeds):
    temp = [(100 - p)//s if (100 - p)%s == 0 else (100 - p)//s + 1 for p, s in zip(progresses, speeds)]
    result, max_day = [], 0
    
    for day in temp:
        if day>max_day:
            max_day = day
            result.append(1)
        else:
            result[-1]+=1
    
    return result
# temp = 남은 작업 시간 정보를 담고 있는 리스트
# result = 결과 리스트
# max_day = 이전 작업들 중 소요된 최대 시간

# temp를 for문으로 순회
# 만약 현재 소요시간이 max_day보다 크다면, max_day를 갱신 + 결과 리스트에 1 추가(배포가 새로 됐다는 의미)
# 아니라면, 결과 리스트의 마지막 값에 +1 (앞에 있는 작업이 오래 걸려서 같이 배포됐다는 의미)