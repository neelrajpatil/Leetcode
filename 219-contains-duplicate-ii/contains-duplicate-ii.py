class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Returns:
            True if there are two duplicates at index i,j AND abs(i-j) < k
        
        Test Case:
            [1,2,3,1] k= 3 ->
        

        Constraints:
            1 <= nums.length <= 10^5
            -10^9 <= nums[i] <= 10^9
            0 <= k <= 10^5
        """

        # Approach 1: Brute Force using 2 for loops. Time O(n^2)

        # # Approach 2: Make a dict {value:List[indices]} in one pass. Check dict.values for k condition
        # # [1,2,3,1] k= 3 ->
        # dup = defaultdict(list) # {1:[0,3],2:[1],3:[2]}
        # for i, num in enumerate(nums): # 3,1
        #     dup[num].append(i)
        
        # for val in dup.values(): # [0,3]
        #     if len(val)>=2:
        #         for i in range(len(val)-1): # 0
        #             for j in range(i+1,len(val)): #1
        #                 if abs(val[i]-val[j]) <= k: #3 <=3
        #                     return True

        # return False

        # Approach 3: Sliding Window

        window = set()

        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        
        return False