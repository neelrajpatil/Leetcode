class Solution:

    def __init__(self, nums: List[int]): 
        self.vals = nums  # [1,2,3,3,3]
        self.indices = defaultdict(list) # {1:[0],2:[1],3:[2,3,4]}
        for idx, val in enumerate(self.vals):
            self.indices[val].append(idx) 

    def pick(self, target: int) -> int:
        """
        finds target in vals, returns 1 of the index

        Test Cases
            self.vals = [1,2,3,3,3] , 3 -> 2 or 3 or 4
        
        Constraints

        """
        # Approach 1:
        # get indices
        curr_indices = self.indices[target]
        # pick random index
        r = math.floor(random.uniform(0,len(curr_indices)))
        return curr_indices[r]


        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)