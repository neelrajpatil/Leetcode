class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0 
        
        for curr in nums:
            if (curr-1) not in nums:
                itr = curr + 1
                while itr in nums:
                    itr += 1
                count = max(count, itr-curr)
        return count

    