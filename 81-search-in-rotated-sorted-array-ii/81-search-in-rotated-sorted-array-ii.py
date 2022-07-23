class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        
        while (left<=right):
            mid = (left + right) // 2
            
            if nums[mid] == target or nums[left] == target or nums[right] == target:
                return True
            
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    #search left
                    right = mid - 1
                else:
                    #search right
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    #search right
                    left = mid + 1
                else:
                    #search left
                    right = mid - 1
                    
        return False