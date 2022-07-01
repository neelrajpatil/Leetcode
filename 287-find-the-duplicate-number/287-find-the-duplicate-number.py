class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        start = 1
        end = len(nums)-1
        
        while(start<=end):
            mid = (start+end)//2
            
            count = 0 
            
            count = sum(num <= mid for num in nums)            
            
            if (count>mid):  #mid is duplicate number or duplicate is to the left of mid
                duplicate = mid
                end = mid -1
            else:                                                  
                start = mid+1
        
        return duplicate
        
 