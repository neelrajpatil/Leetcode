class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        return the length of the shortest clear path to reach bottom right from top left

        Test Case
            [[0,0,0],
             [1,1,0],
             [1,1,0]
            ] -> 4

        Gauranteed Constraints
            1 <= n <= 100
        """

        # Approach 1: BFS

        # [[1,0,0],[1,1,0],[1,1,0]]
        if grid[0][0] == 1:
            return -1
         

        n = len(grid) # 3
        queue = deque([[0,0,1]]) #[[x,y,length]] # [[0,0,1], [0,1,2],]
        visited = set((0,0)) # ((0,0),(0,1),)
        directions =[   [-1,-1],[-1,0],[-1,1],
                        [0,-1],         [0,1],
                        [1,-1], [1,0], [1,1]]

        while queue:
            x,y,length = queue.popleft() # 0,0,1
            if x == n-1 and y == n-1:
                return length
            
            # add ajacent cells to the queue
            for d_x, d_y in directions: # 1,1
                curr_x = x + d_x # 1
                curr_y = y + d_y # 1
                if 0 <= curr_x and curr_x < n and curr_y < n and 0 <= curr_y  and (curr_x,curr_y) not in visited and grid[curr_x][curr_y] != 1:
                    queue.append([curr_x,curr_y,length+1])
                    visited.add((curr_x,curr_y))

        return -1




















        
        # n = len(grid)
        # q = collections.deque([(0,0,1)]) # [x,y,len]
        # visited = set()

        # directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

        # while q:
        #     x, y, length = q.popleft()

        #     if x == n-1 and y== n-1:
        #         return length
        #     if min(x,y) < 0 or max(x,y) >= n or grid[x][y] == 1:
        #         continue
            
        #     for delta_x, delta_y in directions:
        #         if (x+delta_x,y+delta_y) not in visited:
        #             q.append((x+delta_x,y+delta_y,length+1))
        #             visited.add((x+delta_x,y+delta_y))
        
        # return -1

        
