class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        replace element with its index in a sorted List

        Test Cases:
            - [40,10,20,30] -> [4,1,2,3]

        constraints:
            -0 <= arr.length <= 10^5
            - -10^9 arr[i] <= 10^9
        """

        # Approach 1: Time O(n logn)
        # - [40,10,20,30] -> [4,1,2,3]
        # sort List
        sorted_arr = sorted(list(set(arr)))  # [10,20,30,40]
        # one pass to make a dict {value:rank}
        rank = {}   # {10:1,20:2,30:3,40:4}
        for i, num in enumerate(sorted_arr): # 3,40
            rank[num] = i+1
        # one pass to make new list
        result = []
        for num in arr: # 30
            result.append(rank[num])
        return result #[4,1,2,3]