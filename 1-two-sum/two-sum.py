"""
[1,2,3,4] 4 -> [0,2]
[2,7,11,15] 9 -> [0,1]
[2,-2,5,-1] 1 -> [0,3]



# Constraints
 2 <= nums.length <= 10^4
 -10^9 <= nums[i] <= 10^9
 -10^9 <= target <= 10^9

# Assumptions
only 1 solution
without replacement
any order


# Approaches
brute force Time O(n^2) Space O(1)
store complements. Time O(n) Space O(n)
"""

# [2,-2,5,-1] 1 -> [0,3]
# complement = {-1:0,3:1,-4:2,}
# idx 3
# num -1
# [3,0]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement = {} # dict mapping complement:og_index

        for idx, num in enumerate(nums):
            # check if num is in dict
            if num in complement:
                return [idx, complement[num]]     # return curr_index and og_index
            
            # add complement of num to dict
            complement[target-num] = idx
        
        return None # should never reach here
            

        