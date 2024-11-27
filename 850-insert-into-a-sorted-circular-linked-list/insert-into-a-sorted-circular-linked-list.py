"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        """
        
        Input: 
            randomNode

        Test Cases:
            2  | 
            [1,2,3,4] -> [1,2,2,3,4]

            4  | 
            [3,1,2,2] -> [3,4,1,2,2]

            3  | 
            [7,1,2,4] -> [7,1,2,3,4]

            0  | 
            [7,8,9,1,2,4] -> [7,8,9,0,1,2,4]

        Constraints:
            head can be None
            -10^6 <= insertVal <= 10^6
            0 <= noOfNodes <= 50000
        """
        newNode = Node(val=insertVal, next=None)

        # empty list
        if not head:
            newNode.next = newNode
            return newNode

        curr = head

        while curr.next != head:
            # test case 1
            if curr.val <= insertVal <= curr.next.val:
                newNode.next = curr.next
                curr.next = newNode
                return head
            # test case 4
            if curr.val > curr.next.val:
                if curr.val <= insertVal or insertVal <= curr.next.val:
                    newNode.next = curr.next
                    curr.next = newNode
                    return head
            curr = curr.next
        
        newNode.next = curr.next
        curr.next = newNode
        return head
            
            














#         """
# # Definition for a Node.
# class Node:
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next
# """

# class Solution:
#     def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
#         """
#         insert a new node in the parsed circular linked list sorted in ascending order

#         head might not be the smallest value in the 
#         duplicates? insert anywhere

#         constraints:
#             -10^6 <= insertVal <= 10^6
#             0 <= numberOfNode <= 50000
#         """
#         # newNode = Node(insertVal, None)
#         # if not head:
#         #     newNode.next = newNode
#         #     return newNode

#         # curr = head
#         # while curr.next != head:
#         #     if curr.val <= insertVal <= curr.next.val:
#         #         newNode.next = curr.next
#         #         curr.next = newNode
#         #         return head
            
#         #     elif curr.val >= curr.next.val and curr.val <= newNode.val <= curr.next.val: 
#         #         newNode.next = curr.next
#         #         curr.next = newNode
#         #         return head
            
#         #     curr = curr.next
        
#         # newNode.next = head
#         # curr.next = newNode
#         # return head







#         # # if not head:
#         # #     head = Node(insertVal, None)
#         # #     return head
        
#         # # curr = head
#         # # prev = None
#         # # while True:
#         # #     # if insert 5 [1,2,3,4]
#         # #     if curr.val < insertVal: # keep going right
#         # #         if curr.next.val < curr.val: # if looping back i.e. curr == 4
#         # #             new_node = Node(insertVal, curr.next)
#         # #             curr.next = new_node
#         # #         else:
#         # #             curr = curr.next

#         # # # if insert 5 [3,4,5,1,2,2,3]