from collections import deque
import math
class tree:
    def __init__(self,value):
        self.parent=None
        self.node=value
        self.children=deque()
def generate(edges,target):
    temp=[None]*len(target)
    for i,j in edges:
        if temp[i-1] is None:
            temp[i-1]=tree(i-1)
        if temp[j-1] is None:
            temp[j-1]=tree(j-1)
    for i,j in edges:
        temp[i-1].children.append(temp[j-1])
        temp[i-1].children=deque(sorted(temp[i-1].children,key=lambda x:x.node))
        temp[j-1].parent=temp[i-1]
    return temp
def move(node):
    if len(node.children)==0:
        return node
    while node.children:
        next_node=node.children.popleft()
        node.children.append(next_node)
        node=next_node
    return node
def solution(edges, target):
    root=generate(edges,target)[0]
    ord,ord_cnt=[],{i:0 for i in range(len(target))}
    flag=False
    while not flag:
        current_node=move(root).node
        ord.append(current_node)
        ord_cnt[current_node]+=1
        flag=True
        for i in ord_cnt:
            if ord_cnt[i]<int(math.ceil(target[i]/3)):
                flag=False
                break
            elif ord_cnt[i]>target[i]:
                return [-1]
    temp=[1]*len(ord)
    for i in ord:
        target[i]-=1
    for i in range(len(ord)-1,-1,-1):
        if target[ord[i]]>=2:
            temp[i]+=2
            target[ord[i]]-=2
        elif target[ord[i]]==1:
            temp[i]+=1
            target[ord[i]]-=1
        else:
            continue
    return temp