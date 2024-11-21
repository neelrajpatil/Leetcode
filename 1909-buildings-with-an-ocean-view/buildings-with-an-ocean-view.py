class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        max_height = float('-inf')
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > max_height:
                res.append(i)
            max_height = max(max_height, heights[i])

        return [res[i] for i in range(len(res)-1,-1,-1)]