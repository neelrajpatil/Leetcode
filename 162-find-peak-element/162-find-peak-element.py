class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)       
        left = 0
        right = n - 1
        
        #single number
        if left==right:
            return left
        
        #first number is peak
        if nums[left] > nums[left+1]:
            return left
        #last number is peak
        elif nums[right - 1] < nums[right]:
            return right
        
        while left<=right:
            mid = (left + right) // 2
            
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]: #follow the peak of the slope, since peak is to right of mid
                left = mid + 1
            else: #since peak is to left of mid
                right = mid - 1
