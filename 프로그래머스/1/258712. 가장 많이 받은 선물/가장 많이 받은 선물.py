from collections import defaultdict
def solution(friends, gifts):
    give_info = {key : {val : 0 for val in friends} for key in friends}
    give_cnt = defaultdict(int)
    receive_cnt = defaultdict(int)

    for g in gifts:
        giver, receiver = g.split()
        give_info[giver][receiver] += 1
        give_cnt[giver] += 1
        receive_cnt[receiver] += 1

    result = defaultdict(int)

    for i in range(len(friends) - 1):
        for j in range(i + 1, len(friends)):
            p1, p2 = friends[i], friends[j]
            p1_cnt = give_info[p1][p2]
            p2_cnt = give_info[p2][p1]
            p1_score = give_cnt[p1] - receive_cnt[p1]
            p2_score = give_cnt[p2] - receive_cnt[p2]

            if p1_cnt > p2_cnt:
                result[p1] += 1
            elif p1_cnt < p2_cnt:
                result[p2] += 1
            else:
                if p1_score > p2_score:
                    result[p1] += 1
                elif p1_score < p2_score:
                    result[p2] += 1

    return max(result.values()) if result else 0