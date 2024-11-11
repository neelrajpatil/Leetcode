class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = [] #[[index,value]]
        for i in range(len(nums)):
            if nums[i] != 0:
                self.pairs.append([i,nums[i]])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        Test Cases
            - [1,0,0,2,3], [0,3,0,4,8]
                8
            - [0,1,0,0,0] [0,0,0,0,2]
                0
            - [0,1,0,0,2,0,0] [1,0,0,0,3,0,4]

        Constraints
            - n == self.nums.length == vic.nums.length
            - 1 <= n <= 10^5
            - 0 self.nums[i], vic.nums[i]<= 100
            - Store EFFICIENTLY

        Assumptions
            - Storage efficiency is coming at a cost of computational efficiency

        """
        result = 0
        self_p = 0
        vec_p = 0
        
        # iterate through the pointers
        while self_p < len(self.pairs) and vec_p < len(vec.pairs):
            self_i , self_val = self.pairs[self_p]
            vec_i, vec_val = vec.pairs[vec_p]
            # if both indices are the same
            if self_i == vec_i:
                result += self_val * vec_val
                vec_p += 1
                self_p += 1
            
            # if self is ahead
            elif self_i > vec_i:
                vec_p += 1
            # if vec is ahead
            elif vec_i > self_i:
                self_p += 1
                
        
        return result
        
        


# Approach 1: Try to compress and store, and compress in such a way that dot product can be performed without decompressing
    # # 1a. Brute Force (store in array, usual dot produxt)
    # def __init__(self, nums: List[int]):
    #     self.array = nums 

    # # Return the dotProduct of two sparse vectors
    # def dotProduct(self, vec: 'SparseVector') -> int:
    #     """
    #     Test Cases
    #         - [1,0,0,2,3], [0,3,0,4,8]
    #             8
    #         - [0,1,0,0,0] [0,0,0,0,2]
    #             0
    #         - [0,1,0,0,2,0,0] [1,0,0,0,3,0,4]

    #     Constraints
    #         - n == self.nums.length == vic.nums.length
    #         - 1 <= n <= 10^5
    #         - 0 self.nums[i], vic.nums[i]<= 100
    #         - Store EFFICIENTLY

    #     Assumptions
    #         - Storage efficiency is coming at a cost of computational efficiency

    #     """
    #     result = 0
    #     for num1, num2 in zip(self.array, vec.array):
    #         result += num1*num2
    #     return result
    # # 1b. Hash Table (Store in a dict {'index':num,...}) (Dot product, iterate through one dict check if val is in other dict)
    #     def __init__(self, nums: List[int]):
    #     self.values = {}
    #     self.len = len(nums)
    #     for i in range(len(nums)):
    #         if nums[i] != 0:
    #             self.values[i] = nums[i]

    # # Return the dotProduct of two sparse vectors
    # def dotProduct(self, vec: 'SparseVector') -> int:
    #     """
    #     Test Cases
    #         - [1,0,0,2,3], [0,3,0,4,8]
    #             8
    #         - [0,1,0,0,0] [0,0,0,0,2]
    #             0
    #         - [0,1,0,0,2,0,0] [1,0,0,0,3,0,4]

    #     Constraints
    #         - n == self.nums.length == vic.nums.length
    #         - 1 <= n <= 10^5
    #         - 0 self.nums[i], vic.nums[i]<= 100
    #         - Store EFFICIENTLY

    #     Assumptions
    #         - Storage efficiency is coming at a cost of computational efficiency

    #     """
    #     result = 0
    #     # iterate through the items in one dict
    #     for index, val in self.values.items():
    #         if index in vec.values.keys(): # if the same index is in other dict
    #             result += self.values[index] * vec.values[index] # dot product
                
        
    #     return result
    # 1c. Two Pointer (Store index, value pairs) two pointers in each array 

# Approach 2: Compress and store, decompress right before dot product
    # Compression: Store nums list [1,2,0,0,0,2] as [1,2,tuple(3),2]
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)