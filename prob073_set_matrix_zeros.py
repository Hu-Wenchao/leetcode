"""
Given a m x n matrix, if an element is 0, set its 
entire row and column to 0. Do it in place.
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = [1] * len(matrix)
        col = [1] * len(matrix[0])
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] == 0 or col[j] == 0:
                    matrix[i][j] = 0
                    
        return


    def setZeroes2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        firstRowHasZero = False
        firstColHasZero = False
        if len(matrix)==0 or len(matrix[0]) == 0:
            return
        for col in range(0,len(matrix[0])):
            if matrix[0][col]==0:
                firstRowHasZero = True
                break
        for row in range(0, len(matrix)):
            if matrix[row][0]==0:
                firstColHasZero = True
                break
            
        for row in range(1, len(matrix)):
            for col in range(1,len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        
        for row in range(1, len(matrix)):
            for col in range(1,len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if firstRowHasZero:
            for col in range(0,len(matrix[0])):
                matrix[0][col] = 0
        
        if firstColHasZero:
            for row in range(0, len(matrix)):
                matrix[row][0] = 0
