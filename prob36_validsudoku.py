"""
Determine if a Sudoku is valid, according to:
Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where
empty cells are filled with the character '.'.

Note:
A valid Sudoku board (partially filled) is not necessarily
solvable. Only the filled cells need to be validated.
"""

class Solution(object):
    def isValidSudoku(self, board):
        # I don't know why this one is not accepted by leetcode.
        # For the same input the website give a different result 
        # compared to my terminal.
        # The is input is:
        #[".87654321",
        # "2........",
        # "3........",
        # "4........",
        # "5........",
        # "6........",
        # "7........",
        # "8........",
        # "9........"]
        # My terminal return True while the website says False
        # I can't explain why this happened.
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.board = board
        for i in range(9):
            for j in range(9):
                if board[i][j] is ".":
                    continue
                elif self.isValidCell(board[i][j], i, j):
                    continue
                else:
                    return False
        return True
        
    def isValidCell(self, strnum, row, column):
        for i in range(9):
            if (strnum in self.board[row][i]) and (i != column):
                return False
        for i in range(9):
            if (strnum in self.board[i][column]) and (i != row):
                return False
        tempx = row // 3
        tempy = column // 3
        for i in range(tempx*3, tempx*3+3):
            for j in range(tempy*3, tempy*3+3):
                if (strnum in self.board[i][j]) and (i != row) and (j != column):
                    return False
        return True

def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check rows
        for i in range(9):
            d = {}
            for j in range(9):
                if board[i][j] == '.':
                    pass
                elif board[i][j] in d:
                    return False
                else:
                    d[board[i][j]] = True
        # Check columns
        for j in range(9):
            d = {}
            for i in range(9):
                if board[i][j] == '.':
                    pass
                elif board[i][j] in d:
                    return False
                else:
                    d[board[i][j]] = True
        # Check sub-boxes
        for m in range(0, 9, 3):
            for n in range(0, 9, 3):
                d = {}
                for i in range(n, n + 3):
                    for j in range(m, m + 3):
                        if board[i][j] == '.':
                            pass
                        elif board[i][j] in d:
                            return False
                        else:
                            d[board[i][j]] = True
        return True
