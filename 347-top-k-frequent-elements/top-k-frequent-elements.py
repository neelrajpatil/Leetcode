class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Input: List[int], int
        Output: List[int]
        Test Cases
            - [1,1,1,2,2,3] 2
                [1,2]
            - [1] 1
                [1]
                

        Constraints
            1 <= nums.length <= 10^5
            -10^4 <= nums[i] <= 10^4
            k is in [1,numOfUniqElements]
            gauranteed the answer is unique
            Time complexity must be better than O(n Log n)
        

        Assumptions

        """
        # Approach 1: freq counter in one pass, get top k frequencies in one pass of dict
        # Time Complexity O(n)

        freq_c = defaultdict(int) # {value:count}
        # create freq counter
        for num in nums:
            freq_c[num] += 1

        # turn dict into list
        freq_q_list = list(freq_c.items())
        # print(freq_q_list)

        # sort list on first second element
        final_list = sorted(freq_q_list, key=lambda x:x[1], reverse = True)

        return [f[0] for f in final_list[0:k] ]
        
        


