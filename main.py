# binary tree in python
# A python
class Node:

    def __init__(self,key):
        self.right = None
        self.left = None
        self.val = key
# create such a tree
#         1
#        / \
#       2   3
#      / \ / \
#     4 None None None
#    / \
#    None None'''
# create a key or root 1 as an object
root = Node(1)
# assign the left and right nodes, which should be instances of Node class
root.left = Node(2)
root.right = Node(3)
# the left node has a leaf 4
root.left.left = Node(4)
print(root.left.left.val)
print(root)