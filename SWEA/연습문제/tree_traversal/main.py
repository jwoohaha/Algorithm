import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')


class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


def preorder(T, visited):
    '''
    root -> left -> right 순으로 tree를 탐색
    param T: Node
    return: visited[list] 순회 순서
    '''
    if T:
        visited.append(T.item)
        preorder(T.left, visited)
        preorder(T.right, visited)
    return visited


def inorder(T, visited):
    '''
    left -> root -> right 순으로 tree를 탐색
    '''
    if T:
        inorder(T.left, visited)
        visited.append(T.item)
        inorder(T.right, visited)
    return visited


def postorder(T, visited):
    '''
    left -> right -> root 순으로 tree를 탐색
    '''
    if T:
        postorder(T.left, visited)
        postorder(T.right, visited)
        visited.append(T.item)
    return visited


V = int(input())  # 정점의 개수
E = V - 1  # 간선의 개수
edges = list(map(int, input().split()))

# node 인스턴스 생성
nodes = []
for i in range(V+1):
    nodes.append(Node(i))
    str(i) = Node(1)
root = nodes[1]


for i in range(E):
    parent = edges[i*2]
    child = edges[i*2+1]
    if nodes[parent].left:
        nodes[parent].right = nodes[child]
    else:
        nodes[parent].left = nodes[child]

pre_visited = []
in_visited = []
post_visited = []
print(*preorder(root, pre_visited))
print(*inorder(root, in_visited))
print(*postorder(root, post_visited))

