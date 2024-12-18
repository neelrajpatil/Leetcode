# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        # BFS Solution
        res = 0
        queue = collections.deque()
        for curr in nestedList:
            queue.append((1, curr))
        
        while queue:
            depth, element = queue.popleft()
            if element.isInteger():
                res += element.getInteger() * depth
            else:
                for curr in element.getList():
                    queue.append((depth+1, curr))
        
        return res
        
        
        # DFS SOLUTION
        # def process_element(element: 'NestedInteger', depth: int) -> int:
        #     if element.isInteger():
        #         return element.getInteger() * depth
        #     else:
        #         total = 0
        #         for item in element.getList():
        #             total += process_element(item, depth + 1)
        #         return total
        
        # total_sum = 0
        # for nested in nestedList:
        #     total_sum += process_element(nested, 1)
        # return total_sum

        