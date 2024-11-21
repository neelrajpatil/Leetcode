# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """

        Test Cases
            

        """
        if root == None:
            return []
        # dict mapping delta to values
        delta_to_vals = defaultdict(list)
        min_x = float('inf')
        max_x = float('-inf')
        # BFS
        queue = collections.deque([(0,root)])
        while len(queue) > 0:
            x, node = queue.popleft()
            min_x = min(min_x, x)
            max_x = max(max_x, x)

            delta_to_vals[x].append(node.val)
            
            if node.left:
                queue.append((x-1,node.left))
            if node.right:
                queue.append((x+1,node.right))
    
        # iterate thru dict for ans range(min_x, max_x)
        result = []
        for i in range(min_x,max_x+1):
            result.append(delta_to_vals[i])
        return result