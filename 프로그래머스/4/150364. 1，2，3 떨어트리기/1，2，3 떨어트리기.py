from collections import deque
import math

class Tree:
    def __init__(self, value):
        self.parent = None
        self.node = value
        self.children = deque()

# 노드 별 정보 생성
def generate(edges, target):
    temp = [None] * len(target)
    
    for s, e in edges:
        if temp[s - 1] is None:
            temp[s - 1] = Tree(s - 1)
        if temp[e - 1] is None:
            temp[e - 1] = Tree(e - 1)

    for s, e in edges:
        temp[s - 1].children.append(temp[e - 1])
        temp[s - 1].children = deque(sorted(temp[s - 1].children, key=lambda x: x.node))
        temp[e - 1].parent = temp[s - 1]
    
    return temp

# 리프 노드까지 이동하는 메서드
def move(node):
    if not node.children:
        return node
    
    while node.children:
        next_node = node.children.popleft()
        node.children.append(next_node)
        node = next_node
    
    return node

def solution(edges, target):
    root = generate(edges, target)[0]                   # 루트 노드
    order = []                                          # 순번을 저장하는 리스트
    order_cnt = {i: 0 for i in range(len(target))}      # 각 노드 별로 몇 번 도달하는지 갯수 저장
    
    while True:
        cur_node = move(root).node      # 리프 노드
        order.append(cur_node)          # order에 리프 노드 번호 저장
        order_cnt[cur_node] += 1        # order_cnt에 +1

        # 값을 가질 수 없는 노드에 도달한 적이 있으면 [-1]을 리턴
        # 혹은 방문 횟수가 target 값보다 커지면 [-1]을 리턴
        if any(order_cnt[i] > target[i] for i in range(len(target))):
            return [-1]
        
        # 방문한 적이 있는 노드들에 대해서 방문 횟수가 target[i]/3의 반올림 이상이면 만족
        # 각 노드에는 최대 3까지 배정 가능
        # 타겟 값이 8이라고 가정, 최대값 3 -> ceil(8/3) = 3
        # 즉, 3번 이상 방문해야 노드에 원하는 타겟 값을 넣을 수 있음
        # 타겟값이 필요한 모든 노드의 방문횟수가 적절히 채워질 때까지 반복
        if all(order_cnt[i] >= math.ceil(target[i] / 3) for i in range(len(target))):
            break

    result = [1] * len(order)   # 초기 방문 값은 1로 통일(어차피 1은 무조건 들어가야 됨)
    
    # 타겟에서 1씩 제거 (result에 1씩 넣어줬으니까)
    for i in order:
        target[i] -= 1
    
    # 뒤에서부터 돌면서 값을 채워넣어줌
    # 적은 숫자를 사용해야 되고, 사전순으로 빠른 값을 찾아야 되기 때문
    for i in range(len(order) - 1, -1, -1):
        idx = order[i]
        if target[idx] >= 2:
            result[i] += 2
            target[idx] -= 2
        elif target[idx] == 1:
            result[i] += 1
            target[idx] -= 1
    
    return result
