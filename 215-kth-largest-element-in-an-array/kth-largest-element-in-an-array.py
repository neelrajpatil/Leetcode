class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
# Kth Largest Element in an Array

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?
#  
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#  

# Input: [2,3,-3,4,5,6] k = 4
# 
# Constraints:
# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

# Approach 1: maxHeap  Time O(m*k+m) Space O(n)

        # Input: [2,3,-3,4,5,6] k = 4
        # nums:  [-2,-3,3,-4,-5,-6]
        # nums: [-5,-3,-4,-2,3]
        # nums: [-4,-3,-2,3] # pop -5
        # nums: [-2,3,10] # pop -4
        
            #         -3
            #     -2      3

        # initliaze the heap with nums
        for i, num in enumerate(nums):
            nums[i] = -num
        
        heapq.heapify(nums)


        # pop k-1 elements
        for i in range(k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)#3











        # # [1]
        # count = defaultdict(int) # {1:1}
        # min_val = 10001 # 1
        # max_val = -10001 # 1
        
        # # iterate in one pass and create dict
        # for num in nums: # 1
        #     count[num] += 1
        #     min_val = min(num,min_val)
        #     max_val = max(num,max_val)
        
        # for i in range(max_val,min_val-1,-1):
        #     if k <= count[i]:
        #         return i
        #     k -= count[i]
            



        