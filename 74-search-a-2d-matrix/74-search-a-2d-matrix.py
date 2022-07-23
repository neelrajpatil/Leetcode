class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = (m*n) - 1
        
        while (left<=right):
            mid = (left + right) // 2
            
            if element_at_idx(mid,matrix) == target:
                return True
            elif element_at_idx(mid,matrix) < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        
def element_at_idx(idx, matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    row = idx // n  
    column = idx % n
    
    return matrix[row][column]
    