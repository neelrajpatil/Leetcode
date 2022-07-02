class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while(left<=right):
            mid = (left+right)//2
            
            if(nums[left]<nums[right] or left==right):
                return nums[left]
            
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            elif nums[mid]>nums[right]: #min is between mid and right
                left = mid + 1
            else:                       #min is between left and mid
                right = mid - 1
        
                