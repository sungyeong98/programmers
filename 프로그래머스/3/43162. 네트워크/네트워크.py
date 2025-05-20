from collections import defaultdict, deque
def solution(n, computers):
    # 네트워크 연결 상태를 저장하는 딕셔너리
    # ex) networks = {0: [1, 2]} -> 0번 컴퓨터는 1번, 2번 컴퓨터와 연결되어 있음
    networks = defaultdict(list)
    for idx, network_list in enumerate(computers):
        for i, val in enumerate(network_list):
            if idx != i and val == 1:
                networks[idx].append(i)
    
    visited = set()     # 방문 여부 확인용
    result = 0          # 결과 저장용
    # 총 n번 for문 반복 (컴퓨터 갯수 = n)
    for computer in range(n):
        if computer in visited:     # 이미 방문한 컴퓨터면, 넘어가기
            continue
        queue = deque([])       # bfs용 queue
        queue.append(computer)  # 현재 컴퓨터를 queue에 삽입
        
        while queue:
            cur_computer = queue.popleft()  # 현재 컴퓨터
            
            if cur_computer not in visited: # 현재 컴퓨터가 방문하지 않은 상태면
                visited.add(cur_computer)   # visited에 추가
                for next_computer in networks[cur_computer]:    # 딕셔너리에 있는 값들을 for문으로 순회
                    queue.append(next_computer)     # queue에 삽입
                    
        result += 1     # 연결되어 있는 네트워크의 갯수에 +1
    
    return result