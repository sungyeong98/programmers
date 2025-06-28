from collections import deque
import math

class Tree:
    def __init__(self, value):
        self.parent = None
        self.node = value
        self.children = deque()

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

def move(node):
    if not node.children:
        return node
    
    while node.children:
        next_node = node.children.popleft()
        node.children.append(next_node)
        node = next_node
    
    return node

def solution(edges, target):
    root = generate(edges, target)[0]
    order = []
    order_cnt = {i: 0 for i in range(len(target))}
    
    while True:
        cur_node = move(root).node
        order.append(cur_node)
        order_cnt[cur_node] += 1

        if any(order_cnt[i] > target[i] for i in range(len(target))):
            return [-1]
        
        if all(order_cnt[i] >= math.ceil(target[i] / 3) for i in range(len(target))):
            break

    result = [1] * len(order)
    
    for i in order:
        target[i] -= 1
    
    for i in range(len(order) - 1, -1, -1):
        idx = order[i]
        if target[idx] >= 2:
            result[i] += 2
            target[idx] -= 2
        elif target[idx] == 1:
            result[i] += 1
            target[idx] -= 1
    
    return result
