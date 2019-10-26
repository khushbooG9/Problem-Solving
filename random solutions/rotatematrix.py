class Solution(object):
    def rotateanti(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for x in range(int(l/2)):
            for y in range(x, l-1-x):
                temp = matrix[x][y]
                matrix[x][y] = matrix [y][l-1-x]
                matrix[y][l-1-x]= matrix[l-1-x][l-1-y]
                matrix[l-1-x][l-1-y] = matrix[l-1-y][x]
                matrix[l-1-y][x] = temp
        return matrix

    def rotate(self,matrix):
        l = len(matrix)
        for x in range(int(l/2)):
            for y in range(x, l-1-x):
                t = matrix[x][y]
                matrix[x][y] = matrix[l-1-y][x]
                matrix[l-1-y][x] = matrix[l-1-x][l-1-y]
                matrix[l-1-x][l-1-y] = matrix[y][l-1-x]
                matrix[y][l-1-x] = t
        return matrix
