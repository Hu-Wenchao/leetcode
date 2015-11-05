"""
Given an integer n, generate a square matrix filled
with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution(object):
    def generateMatrix(self, n):
        # this one is the first edition, it is correct but ugly
        # see better version on the bottom
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.matrix=[]
        for i in range(0,n):
            self.matrix.append([])
            for j in range(0,n):
                self.matrix[i].append(0)
        self.num = 1
        self.direction = "right"
        self.size = n
        self.row = 0
        self.column = 0
        if n < 0:
            return
        if n == 1:
            return [[1]]
        if n == 2:
            return [[1, 2], [4, 3]]
        while self.num <= n**2:
            self.isTurningPoint(self.row, self.column)
            self.matrix[self.row][self.column] = self.num
            self.next()
            self.num += 1
        return self.matrix
            
    def isTurningPoint(self, row, column):
        if (self.direction is "right") and \
           (column == (self.size-1) or self.matrix[row][column+1] != 0):
            self.direction = "down"
        elif (self.direction is "down") and \
             (row == (self.size-1) or self.matrix[row+1][column] != 0):
            self.direction = "left"
        elif (self.direction is "left") and \
             (column == 0 or self.matrix[row][column-1] != 0):
            self.direction = "up"
        elif (self.direction is "up") and self.matrix[row-1][column] != 0:
            self.direction = "right"

    def next(self):
        if self.direction is "right":
            self.column += 1
        elif self.direction is "down":
            self.row += 1
        elif self.direction is "left":
            self.column -= 1
        elif self.direction is "up":
            self.row -= 1

    def generateMatrix2(self, n):
        # this one is the first edition, it is correct but ugly
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = []
        for i in range(n):
            matrix.append([])
            for j in range(n):
                matrix[i].append(0)
        num = 1
        direction = "right"
        row = 0
        column = 0
        for num in range(1, n**2+1):
            matrix[row][column] = num
            if direction is "right":
                column += 1
                if column >= n-1 or matrix[row][column+1] != 0:
                    direction = "down"
            elif direction is "down":
                row += 1
                if row >= n-1 or matrix[row+1][column] != 0:
                    direction = "left"
            elif direction is "left":
                column -= 1
                if column <= 0 or matrix[row][column-1] != 0:
                    direction = "up"
            elif direction is "up":
                row -= 1
                if matrix[row-1][column] != 0:
                    direction = "right"
        return matrix
