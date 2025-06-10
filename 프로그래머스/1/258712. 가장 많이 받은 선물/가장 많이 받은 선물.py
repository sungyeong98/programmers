from collections import defaultdict
def solution(friends, gifts):
    give_info = {key : {val : 0 for val in friends} for key in friends} # 선물을 주고 받은 정보 저장
    give_cnt = defaultdict(int)         # 선물을 준 횟수
    receive_cnt = defaultdict(int)      # 선물을 받은 횟수

    for g in gifts:
        giver, receiver = g.split()
        give_info[giver][receiver] += 1
        give_cnt[giver] += 1
        receive_cnt[receiver] += 1

    result = defaultdict(int)

    for i in range(len(friends) - 1):
        for j in range(i + 1, len(friends)):
            p1, p2 = friends[i], friends[j]
            p1_cnt = give_info[p1][p2]  # p1이 p2에게 준 선물 갯수
            p2_cnt = give_info[p2][p1]  # p2가 p1에게 준 선물 갯수
            p1_score = give_cnt[p1] - receive_cnt[p1]   # p1의 선물 지수
            p2_score = give_cnt[p2] - receive_cnt[p2]   # p2의 선물 지수

            if p1_cnt > p2_cnt:     # p1이 p2에게 더 많이 선물을 줬다면
                result[p1] += 1
            elif p1_cnt < p2_cnt:   # p2가 p1에게 더 많이 선물을 줬다면
                result[p2] += 1
            else:                   # 서로 선물을 주고 받지 않았다면
                if p1_score > p2_score:     # p1의 선물 지수가 더 높다면
                    result[p1] += 1
                elif p1_score < p2_score:   # p2의 선물 지수가 더 높다면
                    result[p2] += 1

    return max(result.values()) if result else 0