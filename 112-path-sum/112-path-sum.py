# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        #leaf node
        if root.left == None and root.right == None:
            #Found root-to-leaf path
            if root.val == targetSum:
                return True
            #Did not find root-to-leaf path
            return False
        
        if root.right == None:
            return self.hasPathSum(root.left, targetSum-root.val)
        if root.left == None:
            return self.hasPathSum(root.right, targetSum-root.val)
        
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)