# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS Recursive
        if not root:
            return 0
        
        stack = [[root,1]]
        max_depth = 1
        
        while stack:
            node, d = stack.pop()
            max_depth = max(max_depth, d)
            if node.right:
                stack.append([node.right,d+1])
            if node.left:
                stack.append([node.left,d+1])
            
        return max_depth
                
        
        

#         #BFS
#         if not root:
#             return 0
        
#         depth = 0
#         q = deque([root])
        
#         while q:
#             for i in range(len(q)):
#                 node = q.popleft()
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             depth += 1
#         return depth
        
    
    
    
#         #DFS Recursive
#         if root == None:
#             return 0
#         return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1