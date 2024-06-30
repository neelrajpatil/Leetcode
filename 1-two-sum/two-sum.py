class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}
        for idx, num in enumerate(nums):
            # check 
            if num in compliment.keys():
                return (idx, compliment[num])
            # Add compliment
            compliment[target-num] = idx
        return ()
