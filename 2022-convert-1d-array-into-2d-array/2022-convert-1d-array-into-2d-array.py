class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if (m*n!=len(original)):
            return []
        ans = []
        
        for itr in range(0,len(original),n):
            ans.append(original[itr:itr+n])
        return ans        
        # for row in range(m):
        #     temp_row = []
        #     for col in range(n):
        #         temp_row.append(original.pop(0))
        #     ans.append(temp_row)
        