# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        return the values one can see if they are standing to the right of the binary tree

        Test cases
            [1,2,3,null,5,null,4] -> [1,3,4]
            [1,2,3,4,null,null,null,5,] -> [1,3,4,5]

        Constraints
            root can be None
            0 <= noOfNodes <= 100
        """
        if not root:
            return []
        
        res = []
        # Approach 1: BFS Time O(n) Space O(n)
        q = deque([[root,1]]) # [[node,depth]]
        prevNode = None
        prevDepth = 1
        # BFS
        while q:
            currNode, currDepth = q.popleft()
            if currDepth == prevDepth+1:
                res.append(prevNode.val)
            if currNode.left:
                q.append([currNode.left,currDepth+1])
            if currNode.right:
                q.append([currNode.right,currDepth+1])
        
            prevNode = currNode
            prevDepth = currDepth
        
        res.append(prevNode.val)
        return res
            
            
            # print everything when we move down a depth

        