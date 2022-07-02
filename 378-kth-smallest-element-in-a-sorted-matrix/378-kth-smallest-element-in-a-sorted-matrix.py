class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        
        left = matrix[0][0]
        right = matrix[n-1][n-1]
        
        ans = -1
        
        while left<=right:
            mid = (left+right) // 2
            if count_less_than_or_equal(matrix,mid)>=k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

def count_less_than_or_equal(matrix, x) -> int:
    count = 0
    col_idx = len(matrix)-1
    for row_idx in range(len(matrix)):
        while col_idx>=0 and matrix[row_idx][col_idx]>x:
            col_idx -= 1
        count += col_idx+1
            
    return count
        