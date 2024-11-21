class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # Monotonic Stack
        stack = [] # [(height,index)]
        for i in range(len(heights)):
            while stack and stack[-1][0] <= heights[i]:
                stack.pop()
            stack.append((heights[i],i))
            
        return [s[1] for s in stack]



        # res = []
        # max_height = float('-inf')
        # for i in range(len(heights)-1,-1,-1):
        #     if heights[i] > max_height:
        #         res.append(i)
        #     max_height = max(max_height, heights[i])

        # return [res[i] for i in range(len(res)-1,-1,-1)]