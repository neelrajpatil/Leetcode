class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        for itr in range(length):
            if (nums[itr] != itr):
                return (itr)
        return length        