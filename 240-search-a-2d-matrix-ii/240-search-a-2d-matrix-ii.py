class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_max, c_max = len(matrix), len(matrix[0])
        
        row, column = len(matrix) - 1 , 0
        
        while 0 <= row < r_max and 0 <= column < c_max:
            current = matrix[row][column]
            
            if target == current:
                return True
            elif target < current:
                row -= 1
            else:
                column += 1
        return False