# from typing import List
# class Matrix:
#     def __init__(self,mat:List[List[int]]):
#         self.mat = mat
#         # mat = [[1,2,3],[4,5,6,],[7,8,9]]
#         # 1,  2,   3,   4
#         # 5,  6,   7,   8,
#         # 9,  10,  11,   12
#         # 13, 14,  15,   16
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
    # def diagnoalTraverse(self)-> List[int]:
        """
        return diagonal 


        constraints:


        """


        # Approach 1: BFS
        m = len(mat)
        n = len(mat[0])
        added = set() # ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
        q = deque([[0,0,1]]) # [[row,col,depth]] [,[2,0,3],[1,1,3],[0,2,3]]
        added.add((0,0))
        curr_res = [] # [4,2]
        final_res = [] # [1]
        prev_depth = None # 2
        
        def valid_pos(row,col) -> bool:
            if -1 < row < m and -1 < col < n:
                return True
            return False


        while q:
            row, col, depth = q.popleft() # [0,1,2]
            print(f" {row} {col} {depth}")
            # append down if not in added
            down = (row+1,col) # (1,1)
            if down not in added and valid_pos(*down):
                q.append([*down,depth+1])
                added.add(down)

            # append right if not in added
            right = (row,col+1) # 0,2
            if right not in added and valid_pos(*right):
                q.append([*right,depth+1])
                added.add(right) 

            # if depth changes
            if prev_depth != depth and prev_depth != None:
                # if prev_depth is even
                if prev_depth % 2 == 0:
                    # reverse curr_res & append curr_res to final_res
                    final_res.extend(reversed(curr_res))
                else:
                    final_res.extend(curr_res)
                curr_res = []
                

            # append curr to curr_res
            curr_res.append(mat[row][col])
            prev_depth = depth

        final_res.extend(curr_res)
        return final_res