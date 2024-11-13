class TicTacToe:
    """
    Game Board is n x n
    0,0 |0,1 |0,2
       |1,1|   
    2,0 |   |   


    0,0 |0,1 |0,2|0,3
    1,  |1,1 |1,2|1,3
    2,0 |2,1 |2,2|
    3,0 |    |   |3,3
    """

    def __init__(self, n: int):
        self.n = n
        self.board = [[0 for i in range(n)] for i in range(n)]
        self.win_status = 0
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Make the given move, return win_status

        Test Cases:

        Constraints:
            - 2 <= n < 100
            - player is 1 or 2
            -  0 <= row,col < n
            - (row,col) are unique for each different call
        """

        # mark the corresponding place on board with the player
        self.board[row][col] = player

        # check win_status
        return self.check_win_status(row,col,player)



    def check_win_status(self, row:int, col:int, player: int) -> int:
        """
        Assumptions:
            - Only the diagonal from the corners is considered for win status
        """
        n = self.n
        # Check Horizontal crossing current move
        for i in range(n):
            if self.board[row][i] != player:
                break
            if i == n-1:
                self.win_status = player
                return self.win_status


        # Check Vertical crossing current move
        for i in range(n):
            if self.board[i][col] != player:
                break
            if i == n-1:
                self.win_status = player
                return self.win_status

        # Check diagonal crossing current move
        # Check if current move is in path of diagonal
        if row==col or (row+col) == (n-1):
            # top left to bottom right
            for i in range(n):
                if self.board[i][i] != player:
                    break
                # last iteration
                if i == n-1:
                    self.win_status = player
                    return self.win_status
            # top right to bottom left
            for i in range(n):
                if self.board[i][n-1-i] != player:
                    break
                # last iteration
                if i == n-1:
                    self.win_status = player
                    return self.win_status
        
        return self.win_status

                






# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)