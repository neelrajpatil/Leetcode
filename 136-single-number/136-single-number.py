class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    
        #Bit Manipulation O(1) space complexity and O(n) time complexity
        ans = 0
        for num in nums:
            ans ^= num
        return ans
        
        
        # O(1) space complexity O(nlogn + n) time complexity
        # nums.sort()
        # i=0
        # length = len(nums)
        # while(i<length):
        #     if (i+1 == length):
        #         return nums[i]
        #     if nums[i]==nums[i+1]:
        #         i = i+2
        #     else:
        #         return nums[i]
        
        
        # O(n) space complexity O(n) time complexity
        # ans = []
        # for num in nums:
        #     if num not in ans:
        #         ans.append(num)
        #     else:
        #         ans.remove(num)
        # return ans[0]
        