"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        make a deep copy of linkedList

        constraints:
           0 <= n <= 1000
           -10000 <= node.val <= 10000
        
        Test Case
              |           
            [[2,4],[3,5]]

        """
        # Approach 2:
        if not head:
            return head

        # 1st Pass
        # Make a node by node copy, map exit node to new node
        oldToNew = {} # oldNode: newNode
        curr = head
        while curr != None:
            newNode = Node(x=curr.val, next=None, random = None)
            oldToNew[curr] = newNode
            curr = curr.next

        # 2nd Pass
        # for each node, make the connection to next and random node
        curr = head
        while curr != None:
            newNode = oldToNew[curr]
            
            newNode.next = oldToNew[curr.next] if curr.next else None
            newNode.random = oldToNew[curr.random] if curr.random else None
            curr = curr.next
        
        return oldToNew[head]



        # # Approach 1:
        # if not head:
        #     return head

        # # store index for each
        # created = set() # set(node1, node2)
        # visited = set()
        
        
        # # first pass
        # curr = head
        # prev = None
        # while curr != None:
            
        #     newNode = Node(x=curr.x, next=None,random=None)
        #     if prev:
        #         prev.next = newNode
            

        #     prev = curr
        #     curr = curr.next

        # # recursively make a copy of each next node

        # # second pass
        # # 
