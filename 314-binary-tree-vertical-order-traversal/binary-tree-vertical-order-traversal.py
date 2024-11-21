# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        delta_val = defaultdict(list)
        max_x = float('-inf')
        min_x = float('inf')
        
        # BFS
        queue = collections.deque([(0,root)])

        while len(queue) > 0:
            # add curr to delta_val
            x, node = queue.popleft()
            delta_val[x].append(node.val)
            min_x = min(x, min_x)
            max_x = max(x, max_x)

            # append children to queue
            if node.left:
                queue.append((x-1,node.left))
            if node.right:
                queue.append((x+1,node.right))



        # Compute answer
        res = []

        for i in range(min_x,max_x+1):
            res.append(delta_val[i])
        return res



        