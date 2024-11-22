class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # [1]
        count = defaultdict(int) # {1:1}
        min_val = 10001 # 1
        max_val = -10001 # 1
        
        # iterate in one pass and create dict
        for num in nums: # 1
            count[num] += 1
            min_val = min(num,min_val)
            max_val = max(num,max_val)
        
        for i in range(max_val,min_val-1,-1):
            if k <= count[i]:
                return i
            k -= count[i]
            



        