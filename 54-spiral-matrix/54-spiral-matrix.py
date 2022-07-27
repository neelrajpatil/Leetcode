class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        bottom = len(matrix) - 1 
        right = len(matrix[0]) - 1
        top = 0
        left = 0
        
        ans = []
        
        while (True):
            #right
            for c in range(left, right+1):
                ans.append(matrix[top][c])
            top += 1
            if top > bottom or left > right:
                break
            
            #down
            for r in range(top,bottom+1):
                ans.append(matrix[r][right])
            right -= 1
            if top > bottom or left > right:
                break
                
            #left
            for c in range(right, left-1, -1):
                ans.append(matrix[bottom][c])
            bottom -= 1
            if top > bottom or left > right:
                break
            
            #up
            for r in range(bottom, top-1, -1):
                ans.append(matrix[r][left])
            left += 1
            if top > bottom or left > right:
                break
            
        return ans