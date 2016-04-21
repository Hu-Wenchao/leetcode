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
        valid = '123456789'
        for i in xrange(9):
            tmp = []
            for j in xrange(9):
                n = board[i][j]
                if n == '.':
                    continue
                elif n in valid and n != '.' and n not in tmp:
                    tmp.append(n)
                else:
                    return False
        for j in xrange(9):
            tmp = []
            for i in xrange(9):
                n = board[i][j]
                if n == '.':
                    continue
                elif n in valid and n != '.' and n not in tmp:
                    tmp.append(n)
                else:
                    return False
        for i in xrange(0, 9, 3):
            for j in xrange(0, 9, 3):
                tmp = []
                for k in xrange(9):
                    n = board[i+k/3][j+k%3]
                    if n == '.':
                        continue
                    elif n in valid and n != '.' and n not in tmp:
                        tmp.append(board[i+k/3][j+k%3])
                    else:
                        return False
        return True
