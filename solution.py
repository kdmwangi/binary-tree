class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def solution(h,q):
    # create the root node and handle the other different nodes separately
    leaf = 0

    root = Node(1)

    nodes = 2 ** (h-1)
    for n in range(nodes):

        root.left = Node(n)
        root.right = Node(n)
    print(root)

solution(3, [1, 4, 7])