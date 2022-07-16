class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find pivot
        pivot = findMinIndex(nums)
        
        length = len(nums)
        right = length - 1
        left = 0
        
        while(left<=right):
            mid = (left + right) // 2
            if (nums[newIndex(mid,pivot,length)] == target):
                return newIndex(mid,pivot,length)
            if  nums[newIndex(mid,pivot,length)] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return -1

def newIndex(oldIndex,pivot,length):
    return (pivot + oldIndex) % length

def findMinIndex(nums):
    left = 0
    right = len(nums)-1

    
    while(left<=right):
        mid = (left + right) // 2
        
        if nums[left] < nums[right] or left==right:
            return left
        
        if nums[mid-1]>nums[mid]:
            return mid
        elif nums[left] > nums[mid]: #search left
            right = mid - 1
        else:                        #search right
            left = mid + 1
    