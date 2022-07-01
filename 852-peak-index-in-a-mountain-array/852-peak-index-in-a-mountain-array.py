class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr)-1
        
        
        while(start<end):
            mid = (start+end)//2
            if(arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]):   #mid is peak
                return mid
            elif(arr[mid-1]<arr[mid] and arr[mid]<arr[mid+1]): #mid is left of the peak
                start = mid+1
            elif(arr[mid-1]>arr[mid] and arr[mid]>arr[mid+1]): #mid is right of the peak
                end = mid
        
        return mid