class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        if (m*n!=len(original)):
            return []
        for row in range(m):
            temp_row = []
            for col in range(n):
                temp_row.append(original.pop(0))
            ans.append(temp_row)
        return ans        