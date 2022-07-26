class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        # Hashmap of each element O(n) time complexity and O(n) space complexity
        ans = []
        count = {}
        
        for element in nums:
            if element in count:
                count[element] += 1
                ans.append(element)
            else:
                count[element] = 1

        return ans
#         O(n) time complexity single pass and O(1) space complexity 
#         ans = []       
#         for element in nums:
#             if nums[abs(element)-1] < 0:
#                 ans.append(abs(element))
#             nums[abs(element)-1] *= -1 
#         return ans
        
    
        
        
        