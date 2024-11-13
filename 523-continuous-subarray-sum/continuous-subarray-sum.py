class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        return true or false if nums has a good subarray
        good subarray:
            - len > 2
            - sum of array is a multiple of k (0 is always a multiple of k)

        Test Cases:
            - nums = [23,2,4,6,7] k = 6 -> true
            - nums = [23,2,6,4,7] k = 13 -> false

        Constraints:
            - 1<= nums.length <= 10^5
            - 0 <= nums[i] <= 10^9
            - 0 <= sum(nums[i]) <= 2^31-1
            - 1 <= k <= 2^31-1

        """

        # Approach 1: brute force
        # two pointers/two for loops 
        # third for loop to calculate the sum
        # Time O(n^3) Space O(1)

        # Approach 2: O(n) 
        # nums = [23,2,4,6,7] k = 6 -> true
        remainder_index = {0:-1} # {0:-1, 5:0, 1:1}
        cuSum = 0 #0

        for i,num in enumerate(nums): # i = 2, num = 4
            cuSum += num # 29
            rem = cuSum % k # 5

            if rem in remainder_index: #true 
                if i - remainder_index[rem] > 1: # 2-0 > 1
                    return True 
            else:
                remainder_index[rem] = i

        return False