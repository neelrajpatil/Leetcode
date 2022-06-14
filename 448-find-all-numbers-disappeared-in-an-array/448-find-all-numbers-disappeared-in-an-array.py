class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)+1
        ans = []
        nums = set(nums)
        for i in range(1,l):
            if i not in nums:
                ans.append(i)
        return ans
                