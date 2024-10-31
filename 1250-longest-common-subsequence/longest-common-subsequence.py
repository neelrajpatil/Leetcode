class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #  t e x t 2
        # t
        # e
        # x
        # t
        # 1
    
        saved = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        
        for row in range(len(text1)-1,-1,-1):
            for col in range(len(text2)-1,-1,-1):
                if text1[row] == text2[col]:
                    saved[row][col] = 1 + saved[row+1][col+1]
                else:
                    saved[row][col] = max(saved[row+1][col],saved[row][col+1])
             
        
        return saved[0][0]