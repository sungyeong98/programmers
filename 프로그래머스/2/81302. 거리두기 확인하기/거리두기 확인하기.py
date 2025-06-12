from itertools import combinations
def solution(places):
    result = []
    
    for room in places:
        room_info = [list(room[i]) for i in range(5)]
        person_info = find_person_index(room_info)
        result.append(check_distance(person_info, room_info))
        
    return result
        
# 사람의 위치를 반환해주는 함수
def find_person_index(room_info):
    temp = []
    
    for i in range(5):
        for j in range(5):
            if room_info[i][j] == "P":  temp.append((i, j))
    
    return temp

# 방에 있는 모든 인원이 거리두기를 하고 있는지 확인
def check_distance(person_info, room_info):
    for comb in combinations(person_info, 2):
        (x1, y1), (x2, y2) = comb
        
        if not is_valid_distance(x1, y1, x2, y2):
            if not is_valid_position(x1, y1, x2, y2, room_info):    return 0
    return 1

# 충분한 거리를 두고 앉아있는지 확인
def is_valid_distance(x1, y1, x2, y2):
    return True if abs(x1 - x2) + abs(y1 - y2) > 2 else False

# 거리두기를 준수하여 앉아 있는지 확인
def is_valid_position(x1, y1, x2, y2, room_info):
    # 가로로 앉아 있는 경우를 확인 (P X P 로 앉아 있는지 확인)
    if x1 == x2 and room_info[x1][min(y1, y2) + 1] != "X":
        return False
    # 세로로 앉아 있는 경우를 확인
    elif y1 == y2 and room_info[min(x1, x2) + 1][y1] != "X":
        return False
    # 대각선으로 앉아 있는 경우를 확인
    elif abs(x1 - x2) == 1 and abs(y1 - y2) == 1 and (room_info[x1][y2] != "X" or room_info[x2][y1] != "X"):
        return False
    return True