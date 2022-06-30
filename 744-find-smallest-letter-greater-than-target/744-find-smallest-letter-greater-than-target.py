class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters)-1
        mid = int((start+end)/2)
        ans= ''
        
        if(letters[-1]<=target):
            return letters[0]
        
        while(start<=end):
            mid = int((start+end)/2)
            
            if(letters[mid]==target):
                if(start==end):
                    return ans
                for idx in range(mid,end+1):
                    if (letters[idx]>target):
                        return letters[idx]
            elif(letters[mid]<target):
                start = mid+1
            elif(letters[mid]>target):
                ans = letters[mid]
                end = mid - 1

        return ans
            
                