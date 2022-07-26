class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        
        for element in nums:
            if nums[abs(element)-1] < 0:
                ans.append(abs(element))
            
            nums[abs(element)-1] *= -1 
        return ans
        
        