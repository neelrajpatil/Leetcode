"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


adjList = [[2,4],[1,3],[2,4],[1,3]] -> [[2,4],[1,3],[2,4],[1,3]]

"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Approach 1: Time O(V + E) Space(V)
        if not node:
            return node
        visited = set()
        oldToNew = {}

        # DFS to create all nodes
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            new_node = Node(node.val)
            oldToNew[node] = new_node
            for nei in node.neighbors:
                # if nei not in visited:
                    new_node.neighbors.append(dfs(nei))
            
            return new_node

        # run DFS
        return dfs(node)

        # One pass to create all edges

        