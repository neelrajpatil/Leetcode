# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        sum up all numbers from root to leafs

        Test Cases:
            [1,2,3] -> 25
            [4,9,0,5,1,] ->  1026   because 495+491+40        

        Constraints:
            1 < noOfNodes < 1000
            0 <= node.val <= 9
            depth of the tree <= 10
        """
        if not root:
            return None
        # Approach 1: DFS, keep track of prefix, when you reach leaf node, append to nums
        nums = self.findNumbers(root,[])
        print(nums)
        return sum(nums)

    def findNumbers(self,node:Optional[TreeNode],prefix:List[str]) -> List[int]:

        prefix.append(str(node.val))
        if node.left == None and node.right == None:
            num = int("".join(prefix))
            return [num]
        
        res = []
        
        if node.left:
            res.extend(self.findNumbers(node.left,prefix.copy()))
        if node.right:
            res.extend(self.findNumbers(node.right,prefix.copy()))
        
        return res




        