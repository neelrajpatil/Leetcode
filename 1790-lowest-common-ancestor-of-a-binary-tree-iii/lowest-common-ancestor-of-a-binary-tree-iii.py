"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Approach 2:

        p_copy = p
        q_copy = q

        while p_copy != q_copy:
            p_copy = p_copy.parent if p_copy.parent != None else q
            q_copy = q_copy.parent if q_copy.parent != None else p
        
        return p_copy
        
        # Apporach 1: Time O(n) Space O(n)
        # seen = set()

        # while p:
        #     seen.add(p)
        #     p = p.parent
        
        # while q:
        #     if q in seen:
        #         return q
        #     q = q.parent

        