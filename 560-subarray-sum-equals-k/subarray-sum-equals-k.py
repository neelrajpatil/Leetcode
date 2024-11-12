class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Test Cases
            - [1,1,1] 2
                2
            - [1,2,3] 3
                2
            - [3,2,2] 3
                1
            - []
        Constraints
            - Contiguous non empty sequence
            - 1 <= nums.length <= 2 * 10^4
            - -1000 <= nums[i] <= 1000
            - -10^7 <= k <= 10^7
        Assumptions
            - Subarray can be of len 1 example: [3]

        """
        # Approach 3: I don't understand this fully, Do it again
        mapp = defaultdict(int)
        prefixSum = 0
        count = 0
        mapp[0] = 1

        for i in range(len(nums)):
            prefixSum += nums[i]
            diff = prefixSum - k
            count += mapp[diff]
            mapp[prefixSum] += 1
        
        return count
            



        # # Approach 2: Brute force with cumulative sum O(n^2)
        # # [1,2,3,4]
        # cumulative_sums = [] #[1,3,6,10]
        # sum = 0
        # for i in range(len(nums)):
        #     sum += nums[i]
        #     cumulative_sums.append(sum)
        # cumulative_sums.append(0) # for case when start = 0, so -1 index cu_sum will give 0
        

        # count = 0
        # for start in range(len(nums)):
        #     for end in range(start,len(nums)):
        #         if cumulative_sums[end]-cumulative_sums[start-1] == k:
        #             count += 1
        # return count



        # # Approach 1: Brute Force O(n^3)
        # # nums= [1,1,1] k = 2
        # count = 0
        # # check each subarray
        # for start in range(len(nums)): # 1                  <3
        #     for end in range(start, len(nums)): # 2                 <3
        #         # if sub array sum == target
        #         sum = 0
        #         for i in range(start,end+1): #1 < 3
        #             sum += nums[i]
        #         if sum == k:
        #             count += 1
        # return count


        
        
