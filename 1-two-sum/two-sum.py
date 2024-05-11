class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store the complement as the key and the index of the og as the value in the key

        prev = {}

        for i in range(len(nums)):
            if (target - nums[i]) in prev:
                return [i,prev[(target - nums[i])]]
            prev[nums[i]] = i

        return []

