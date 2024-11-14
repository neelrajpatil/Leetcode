class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        return the largerst subarray in nums where
            - the number of 1 is equal to number of 0
        
        Test Cases
            - nums = [0,1,0] -> 2

        constraints
            1 <= nums.length <= 10^5
            nums[i] = 0 or 1

        Assumptions
            if no subarray found, returns 0
            subarray of size 1 is valid
        
        """

        # Approach 1: # One pass, cal sum, store sum, if encountered prior, consider new subarray
        # - nums = [0,1,0] -> 2
        result = 0 # 2
        sum = 0
        sum_idx = {} # {-1:0, 0:1, }

        for i, num in enumerate(nums): # 2,0
            sum += 1 if num == 1 else -1 #-1
            if sum not in sum_idx:
                sum_idx[sum] = i

            if sum == 0 and (i+1)>result:
                result = i+1
            elif i-sum_idx[sum] > result: #2
                result = i-sum_idx[sum] 
            

        return result #2

        