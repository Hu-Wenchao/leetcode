"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.val = self.PossibleVals()
        self.Solver()

    def PossibleVals(self):
        a = "123456789"
        d, val = {}, {}
        for i in xrange(9):
            for j in xrange(9):
                ele = self.board[i][j]
                if ele != ".":
                    d[("r", i)] = d.get(("r", i), []) + [ele]
                    d[("c", j)] = d.get(("c", j), []) + [ele]
                    d[(i//3, j//3)] = d.get((i//3, j//3), []) + [ele]
                else:
                    val[(i,j)] = []
        for (i,j) in val.keys():
            inval = d.get(("r",i),[])+d.get(("c",j),[])+d.get((i/3,j/3),[])
            val[(i,j)] = [n for n in a if n not in inval ]
        return val
    
    def Solver(self):
        if len(self.val)==0:
            return True
        kee = min(self.val.keys(), key=lambda x: len(self.val[x]))
        nums = self.val[kee]
        for n in nums:
            update = {kee:self.val[kee]}
            if self.ValidOne(n, kee, update): # valid choice
                if self.Solver(): # keep solving
                    return True
            self.undo(kee, update) # invalid choice or didn't solve it => undo
        return False

    def ValidOne(self, n, kee, update):
        self.board[kee[0]][kee[1]] = n
        del self.val[kee]
        i, j = kee
        for ind in self.val.keys():
            if n in self.val[ind]:
                if ind[0]==i or ind[1]==j or (ind[0]/3,ind[1]/3)==(i/3,j/3):
                    update[ind] = n
                    self.val[ind].remove(n)
                    if len(self.val[ind])==0:
                        return False
        return True

    def undo(self, kee, update):
        self.board[kee[0]][kee[1]]="."
        for k in update:            
            if k not in self.val:
                self.val[k]= update[k]
            else:
                self.val[k].append(update[k])
        return None

    def solveSudoku2(self, board):
        self.rec(board, 0, 0)
        
    def rec(self, board, r, c):
        if r == 9:
            return True
        if c == 8:
            nr = r + 1
            nc = 0
        else:
            nr = r
            nc = c + 1
        if board[r][c] != '.':
            return self.rec(board, nr, nc)
        for n in range(1, 10):
            if self.isValid(board, str(n), r, c):
                board[r][c] = str(n)
                if self.rec(board, nr, nc):
                    return True
                board[r][c] = '.'
        return False
        
    def isValid(self, board, n, r, c):
        for i in range(9):
            if board[i][c] == n:
                return False
            if board[r][i] == n:
                return False
        rg = (r // 3) * 3
        cg = (c // 3) * 3
        for i in range(rg, rg + 3):
            for j in range(cg, cg + 3):
                if board[i][j] == n:
                    return False
        return True
