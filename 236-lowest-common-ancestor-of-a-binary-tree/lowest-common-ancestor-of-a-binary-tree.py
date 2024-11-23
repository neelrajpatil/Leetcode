# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Assumptions:
            No Duplicates
        """
        if not root:
            return None
        
        # DFS pre-order | search
        if root.val == p.val or root.val ==q.val:
            return root
        
        found_left = self.lowestCommonAncestor(root.left,p,q)
        found_right = self.lowestCommonAncestor(root.right,p,q)
        
        if found_left != None and found_right != None:
            return root
        elif found_right != None:
            return found_right
        elif found_left != None:
            return found_left
        else:
            return None

