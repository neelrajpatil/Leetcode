"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def convert(self, curr_node:'Optional[Node]'):
        if curr_node == None:
            return


        if curr_node.left:
            self.convert(curr_node.left)
        
        
        if self.last == None:
            self.first = curr_node
            self.last = curr_node
        else:
            self.last.right = curr_node
            curr_node.left = self.last
            self.last = curr_node

        
        if curr_node.right:
            self.convert(curr_node.right)
        
        return 
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        self.first = None
        self.last = None

            
        self.convert(root)

        self.first.left = self.last
        self.last.right = self.first
        return self.first



        
