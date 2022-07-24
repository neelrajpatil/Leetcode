class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        int r_max = matrix.size();
        int c_max = matrix[0].size();
            
        int row = r_max - 1;
        int col = 0;
        int current;
        
        while ((0<=row) && (col<c_max)){
            
            current = matrix[row][col];
            
            if (current == target)
                return true;
            else if (current < target)
                col++;
            else
                row--;
        }
        
        return false;
    }
};